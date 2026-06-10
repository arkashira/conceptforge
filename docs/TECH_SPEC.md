# TECH_SPEC.md
**Project:** conceptforge  
**Owner:** Axentx – Product Engineering  
**Version:** 1.0.0 (initial)  
**Last Updated:** 2026‑06‑10  

---  

## 1. Overview  

**conceptforge** is a collaborative design assistant for concept artists. It enables artists to generate original visual concepts **without directly invoking generative AI**. Instead, the system iteratively refines a lightweight, domain‑specific model using **human‑in‑the‑loop feedback**. The workflow is:

1. **Artist sketches** or uploads a rough idea.  
2. The system proposes **variations** based on a continuously‑trained “style‑aware” model.  
3. The artist **rates / edits** the suggestions.  
4. Collected feedback is stored and periodically used to **re‑train** the model, improving future suggestions while preserving uniqueness.

The product is positioned as a **creative‑partner** that respects IP concerns and avoids the “black‑box” perception of large‑scale generative AI.

---  

## 2. Architecture Diagram  

```
+-------------------+        +-------------------+        +-------------------+
|   Front‑End (SPA) | <----> |   API Gateway     | <----> |   Auth Service    |
|  React + MUI      |        |  FastAPI (uvicorn)|        |  OIDC (Keycloak) |
+-------------------+        +-------------------+        +-------------------+
          |                           |                         |
          |                           |                         |
          v                           v                         v
+-------------------+        +-------------------+        +-------------------+
|   Feedback Queue | <----> |   Model Service   | <----> |   Model Trainer   |
|   Redis Streams   |        |   FastAPI (REST)  |        |   PyTorch + SGLang|
+-------------------+        +-------------------+        +-------------------+
          |                           |                         |
          v                           v                         v
+-------------------+        +-------------------+        +-------------------+
|   Object Store    | <----> |   Metadata DB    | <----> |   Scheduler (Celery)|
|   MinIO / S3      |        |   PostgreSQL     |        |   Beat (periodic) |
+-------------------+        +-------------------+        +-------------------+
```

*All services are containerised and orchestrated via **Kubernetes** (Helm charts provided).*

---  

## 3. Core Components  

| Component | Responsibility | Tech Stack | Key Interfaces |
|-----------|----------------|------------|----------------|
| **Front‑End** | Artist UI – sketch upload, feedback UI, project dashboard | React 18, TypeScript, Material‑UI, Vite, Web‑GL canvas (fabric.js) | `GET /api/projects`, `POST /api/feedback` |
| **API Gateway** | Single entry point, request validation, rate‑limiting | FastAPI 0.110, Pydantic, Uvicorn, OpenAPI 3.1 | REST/JSON |
| **Auth Service** | User management, SSO, token issuance | Keycloak (OIDC), PostgreSQL (user store) | `/auth/token`, `/auth/refresh` |
| **Feedback Queue** | Decouples UI from model training, guarantees ordering | Redis 7 (Streams) + Redis‑JSON | `XADD feedback`, `XREAD` |
| **Model Service** | Serve low‑latency inference for variation generation | FastAPI, vLLM (lightweight inference), SGLang (structured generation) | `POST /generate` |
| **Model Trainer** | Offline batch training using collected feedback | Python 3.11, PyTorch 2.4, SGLang, Lightning, HuggingFace Datasets | CLI (`train.py`) |
| **Metadata DB** | Persistent store for projects, assets, feedback metadata | PostgreSQL 15, SQLAlchemy ORM | SQL, Alembic migrations |
| **Object Store** | Binary assets (sketches, generated images, checkpoints) | MinIO (S3‑compatible) | Presigned URLs |
| **Scheduler** | Periodic jobs: model re‑training, cleanup, analytics | Celery 5 + Redis broker, Celery‑Beat | Task definitions (`tasks.py`) |

---  

## 4. Data Model  

### 4.1 ER Diagram (simplified)

```
User ──< Project >── Image ──< Generation
   │                │                │
   │                └─< Feedback >───┘
   └─< Session >─────────────────────┘
```

### 4.2 Table Schemas  

| Table | Columns | Description |
|-------|---------|-------------|
| **users** | `id PK`, `email`, `display_name`, `hashed_pw`, `created_at` | Authenticated artists |
| **projects** | `id PK`, `owner_id FK → users.id`, `title`, `description`, `status`, `created_at` | Logical grouping of work |
| **images** | `id PK`, `project_id FK`, `type ENUM('sketch','generated')`, `uri`, `metadata JSONB`, `created_at` | Stored binary assets |
| **generations** | `id PK`, `image_id FK`, `model_version`, `seed`, `parameters JSONB`, `uri`, `created_at` | Each AI‑assisted variation |
| **feedback** | `id PK`, `generation_id FK`, `user_id FK`, `rating INT (1‑5)`, `comments TEXT`, `created_at` | Human evaluation |
| **sessions** | `id PK`, `user_id FK`, `token`, `expires_at` | Refresh‑token management |
| **model_versions** | `id PK`, `version_str`, `checkpoint_uri`, `trained_at`, `metrics JSONB` | Track model evolution |

---  

## 5. Key APIs  

All endpoints are versioned under `/api/v1/`. Authentication via Bearer JWT.

### 5.1 Project Management  

| Method | Endpoint | Request | Response |
|--------|----------|---------|----------|
| `POST` | `/projects` | `{title, description}` | `{id, created_at}` |
| `GET` | `/projects/{id}` | – | Project object + list of images |
| `PATCH` | `/projects/{id}` | `{title?, description?, status?}` | Updated object |
| `DELETE` | `/projects/{id}` | – | `{deleted:true}` |

### 5.2 Image & Generation  

| Method | Endpoint | Request | Response |
|--------|----------|---------|----------|
| `POST` | `/projects/{id}/images` | `multipart/form-data (file)` | `{image_id, uri}` |
| `POST` | `/generate` | `{image_id, parameters}` | `{generation_id, uri, seed}` |
| `GET` | `/generations/{id}` | – | Generation object |

### 5.3 Feedback  

| Method | Endpoint | Request | Response |
|--------|----------|---------|----------|
| `POST` | `/feedback` | `{generation_id, rating, comments}` | `{feedback_id}` |
| `GET` | `/generations/{id}/feedback` | – | List of feedback entries |

### 5.4 Model Service  

| Method | Endpoint | Request | Response |
|--------|----------|---------|----------|
| `POST` | `/model/predict` | `{prompt, style_embedding?, seed?, temperature?}` | `{image_uri, metadata}` |
| `GET` | `/model/version` | – | `{version, trained_at, metrics}` |

---  

## 6. Technology Stack  

| Layer | Choice | Rationale |
|-------|--------|-----------|
| **Front‑End** | React 18 + TypeScript + MUI | Modern SPA, component library, strong community |
| **API** | FastAPI + Pydantic | High performance, automatic OpenAPI docs |
| **Auth** | Keycloak (OIDC) | Enterprise‑grade SSO, easy federation |
| **Inference** | vLLM (lightweight LLM inference) + SGLang (structured generation) | Low latency, supports token‑level control for style‑aware generation |
| **Training** | PyTorch 2.4 + Lightning + SGLang | Proven research stack, easy distributed training |
| **Data Store** | PostgreSQL 15 (relational) + Redis 7 (queues) | Strong ACID guarantees + high‑throughput streaming |
| **Object Storage** | MinIO (S3‑compatible) | On‑premise, works with existing CI/CD pipelines |
| **Orchestration** | Kubernetes 1.28 + Helm | Cloud‑agnostic, auto‑scaling |
| **CI/CD** | GitHub Actions + ArgoCD | Automated testing, progressive delivery |
| **Monitoring** | Prometheus + Grafana + Loki | Metrics, logs, alerts |
| **Observability** | OpenTelemetry (Python & Node) | End‑to‑end tracing across services |

---  

## 7. Dependencies  

| Dependency | Version | License |
|------------|---------|---------|
| fastapi | 0.110.0 | MIT |
| uvicorn | 0.30.0 | BSD‑3 |
| pydantic | 2.7.0 | MIT |
| redis | 5.0.3 | BSD‑3 |
| sqlalchemy | 2.0.30 | MIT |
| alembic | 1.13.2 | MIT |
| keycloak-admin | 0.13.0 | Apache‑2.0 |
| vllm | 0.5.2 | Apache‑2.0 |
| sglang | 0.3.1 | Apache‑2.0 |
| torch | 2.4.0 | BSD‑3 |
| lightning | 2.3.0 | Apache‑2.0 |
| react | 18.3.0 | MIT |
| material‑ui | 5.15.0 | MIT |
| fabric.js | 5.3.0 | MIT |
| minio | 7.2.5 | Apache‑2.0 |
| celery | 5.4.0 | BSD‑3 |
| prometheus‑client | 0.20.0 | Apache‑2.0 |

---  

## 8. Deployment Architecture  

### 8.1 Kubernetes Namespaces  

| Namespace | Purpose |
|-----------|---------|
| `conceptforge-dev` | Development – lower‑replica counts, canary releases |
| `conceptforge-staging` | Integration testing, runs nightly training jobs |
| `conceptforge-prod` | Production – autoscaled, strict RBAC |

### 8.2 Helm Chart Structure  

```
conceptforge/
├─ charts/
│  └─ conceptforge/
│     ├─ templates/
│     │  ├─ deployment-frontend.yaml
│     │  ├─ deployment-api.yaml
│     │  ├─ deployment-model.yaml
│     │  ├─ deployment-trainer.yaml
│     │  ├─ service.yaml
│     │  └─ ingress.yaml
│     ├─ values.yaml
│     └─ Chart.yaml
```

### 8.3 CI/CD Pipeline  

1. **Push → PR** – Lint (ruff, eslint), unit tests, type checks.  
2. **Merge** – Build Docker images, push to internal registry.  
3. **ArgoCD sync** – Deploy to `dev`. Run integration tests (Postman collection).  
4. **Promote** – Manual approval → `staging` (runs nightly trainer).  
5. **Promote** – Automatic health‑check → `prod`.  

### 8.4 Scaling & Autoscaling  

| Service | HPA Target | Min Replicas | Max Replicas |
|---------|------------|--------------|--------------|
| frontend | CPU 60% | 2 | 10 |
| api-gateway | CPU 70% | 2 | 12 |
| model-service | GPU utilization 65% (NVIDIA GPU node pool) | 1 | 4 |
| trainer | CronJob (once per 24h) – runs on dedicated GPU node | 0 | 1 |

---  

## 9. Security & Compliance  

* **Transport security:** All ingress exposed via TLS (Let’s Encrypt / internal CA).  
* **Data at rest:** MinIO bucket encrypted with SSE‑S3; PostgreSQL encrypted via pgcrypto.  
* **Auth:** OIDC tokens short‑lived (15 min); refresh tokens stored HTTP‑Only Secure cookies.  
* **PII handling:** No personal data stored beyond email (hashed password).  
* **Audit logging:** All write operations logged to Loki with request IDs.  

---  

## 10. Testing Strategy  

| Layer | Tooling | Scope |
|-------|---------|-------|
| Unit | pytest, unittest, React Testing Library | Individual functions, components |
| Integration | FastAPI TestClient, Postman/Newman | End‑to‑end API flows |
| Load | Locust, k6 | Model service latency (<150 ms per request) |
| UI | Cypress | Critical user journeys (upload → generate → feedback) |
| Model | Custom evaluation script (FID, CLIP‑Score) on validation set | Ensure no regression after each training cycle |

Coverage target: **≥85 %** for backend, **≥80 %** for frontend.

---  

## 11. Roadmap (post‑MVP)  

| Milestone | Target | Description |
|-----------|--------|-------------|
| **M1 – Beta** | 2026‑08‑01 | Public beta with limited GPU quota, feedback loop fully functional |
| **M2 – Multi‑Style Models** | 2026‑11‑15 | Ability to train per‑artist style models on‑demand |
| **M3 – Plugin SDK** | 2027‑02‑01 | Expose generation API to external DCC tools (Blender, Maya) |
| **M4 – Marketplace** | 2027‑06‑01 | Artists can sell curated model checkpoints under revenue‑share |

---  

## 12. Glossary  

| Term | Meaning |
|------|---------|
| **Feedback Queue** | Redis Stream that buffers UI‑submitted feedback until the trainer consumes it. |
| **Model Version** | Immutable checkpoint identified by a semantic version string (e.g., `v0.3.1`). |
| **SGLang** | Structured Generation Language – used to enforce style constraints during inference. |
| **vLLM** | High‑throughput inference engine optimized for LLMs on GPU. |
| **ConceptForge** | The product name; the repository containing all source code. |

---  

*Prepared by:*  
Senior Product/Engineering Lead – Axentx  
*Document ID:* CF‑TECH‑SPEC‑001  

---
