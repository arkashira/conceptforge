# ConceptForge – Product Requirements Document (PRD)

**Document Version:** 1.0  
**Last Updated:** 2026‑06‑10  
**Author:** Senior Product/Engineering Lead, Axentx  

---

## 1. Problem Statement

Concept artists spend a large portion of their workflow iterating on sketches, mood‑boards, and reference collections. Existing AI‑generated image tools either:

1. **Produce generic outputs** that lack the nuanced style direction an artist needs.  
2. **Require heavy prompt engineering** and provide limited control over the creative process.  
3. **Create IP‑risk** because the generated assets are derived from proprietary datasets.

Artists therefore need a **human‑in‑the‑loop** system that blends their feedback with machine‑learning assistance, delivering **original, high‑quality concepts** while preserving artistic intent and IP ownership.

---

## 2. Target Users & Personas

| Persona | Description | Primary Pain Points |
|---------|-------------|---------------------|
| **Concept Artist (Freelance / Studio)** | Creates visual concepts for games, film, advertising. | Time‑consuming iteration, difficulty visualizing variations quickly, fear of AI‑generated plagiarism. |
| **Art Director** | Oversees visual style across a project. | Needs rapid exploration of multiple directions, consistent style enforcement, and clear version control. |
| **Creative Lead (Product/Marketing)** | Generates visual assets for pitches and campaigns. | Limited design resources, need for fresh ideas on short timelines. |

---

## 3. Goals & Success Metrics

| Goal | Success Metric (quantitative) | Target (12‑mo) |
|------|------------------------------|----------------|
| **Accelerate concept iteration** | Avg. time from initial sketch to 3 viable variations | ↓ 45% (from 4h → 2.2h) |
| **Increase originality** | % of concepts flagged as “novel” by internal reviewers (no >30% similarity to training data) | ≥ 92% |
| **Boost artist satisfaction** | Net Promoter Score (NPS) for the tool | ≥ 70 |
| **Maintain IP safety** | Zero legal complaints / IP infringement claims | 0 |
| **Revenue validation** | Paying studio sign‑ups (monthly recurring) | 12 studios @ $2,500/mo by month 12 |

---

## 4. Scope

### 4.1 In‑Scope (Features to be Delivered)

| Priority | Feature | Description | Acceptance Criteria |
|----------|---------|-------------|----------------------|
| **P0** | **Human‑Feedback Loop UI** | Web‑based canvas where artists sketch, annotate, and rate machine suggestions. | • Sketch import & free‑hand drawing tools.<br>• Real‑time “thumbs‑up/down” feedback on generated variants.<br>• Feedback persisted per session. |
| **P0** | **Guided Generation Engine** | ML model (fine‑tuned on internal “concept‑only” dataset) that takes artist feedback as conditioning signals. | • Generates ≥3 variations within 5 s of feedback.<br>• Variations respect style tags (e.g., “organic”, “mechanical”). |
| **P1** | **Style & Constraint Controls** | Sidebar with sliders for “line weight”, “color palette”, “complexity”, plus custom style‑token upload. | • Adjustments reflected in next generation pass.<br>• Tokens persist across sessions. |
| **P1** | **Versioning & Export** | Automatic version history; export to PNG, PSD, and layered SVG. | • Users can revert to any prior version.<br>• Export retains layer metadata. |
| **P2** | **Collaboration Workspace** | Multi‑user session where art director can comment and lock/unlock specific variations. | • Real‑time sync for up to 5 participants.<br>• Comment thread attached to each variation. |
| **P2** | **IP‑Safe Dataset Guardrails** | Automated similarity check against the internal “safe‑concept” corpus before presenting a variation. | • No variation exceeds 30% similarity score.<br>• Flagged outputs are regenerated automatically. |
| **P3** | **Plugin Integration** | Plug‑ins for Photoshop, Clip Studio Paint, and Blender to push/pull assets. | • One‑click import/export from supported apps. |
| **P3** | **Analytics Dashboard** | Usage stats, iteration counts, and satisfaction surveys for internal product improvement. | • Dashboard accessible to admin accounts.<br>• Data refreshed daily. |

### 4.2 Out‑of‑Scope (Post‑launch)

- Full 3‑D model generation (focus on 2‑D concept art first).  
- Marketplace for selling generated concepts.  
- Mobile‑only native app (initial release is web‑centric).  
- Integration with external large language models (e.g., GPT‑4) – we will rely on our own fine‑tuned diffusion model.

---

## 5. Functional Requirements

| ID | Requirement | Type | Priority |
|----|-------------|------|----------|
| FR‑001 | The UI must load a blank canvas within 2 s on a standard 1080p connection. | Performance | P0 |
| FR‑002 | Artists can draw with at least 5 brush types and adjustable opacity. | UI | P0 |
| FR‑003 | After each feedback action, the generation engine returns ≥3 distinct outputs within 5 s. | Latency | P0 |
| FR‑004 | Feedback (thumbs up/down, style sliders) is stored in a per‑session vector and sent to the model as conditioning. | Data | P0 |
| FR‑005 | Exported files retain original resolution and embed a hidden JSON manifest with version metadata. | Export | P1 |
| FR‑006 | Collaboration edits are merged using OT (operational transformation) to avoid conflicts. | Collaboration | P2 |
| FR‑007 | Similarity check runs on the server side using cosine similarity on the embedding space; threshold = 0.30. | Safety | P2 |
| FR‑008 | Admin dashboard shows MAU, average iterations per session, and NPS trend. | Analytics | P3 |

---

## 6. Non‑Functional Requirements

| Category | Requirement |
|----------|-------------|
| **Scalability** | System must support 500 concurrent active sessions with < 10 % CPU saturation on our baseline 8‑vCPU nodes. |
| **Reliability** | 99.5 % uptime SLA; automatic failover to a secondary region. |
| **Security** | All traffic TLS 1.3; data at rest encrypted with AES‑256. |
| **Privacy** | No artist data is stored beyond the session unless the user explicitly saves/export. |
| **Compliance** | Meet GDPR and CCPA for user‑generated content. |
| **Maintainability** | Codebase follows Axentx Runbook conventions; CI/CD pipeline with unit, integration, and visual regression tests. |

---

## 7. Architecture Overview (High‑Level)

```
+-------------------+       +-------------------+       +-------------------+
|  Front‑end (React | <---> |  API Gateway (NGINX) | <---> |  Generation Service|
|  + Canvas)        |       |  Auth, Rate‑limit |       |  (vLLM + fine‑tuned|
+-------------------+       +-------------------+       |   diffusion model) |
        |                               |               +-------------------+
        |                               |                        |
        v                               v                        v
+-------------------+       +-------------------+       +-------------------+
|  Collaboration   | <---> |  Feedback Store   | <---> |  Similarity Engine|
|  Service (OT)    |       |  (PostgreSQL +   |       |  (FAISS index)    |
+-------------------+       |   pgvector)      |       +-------------------+
```

- **Front‑end** built with React + Fabric.js for canvas manipulation.  
- **Generation Service** leverages **vLLM** for fast diffusion inference (see C. Frameworks).  
- **Feedback Store** persists vectors for each session; used to condition the model.  
- **Similarity Engine** runs a cosine‑similarity check against the “safe‑concept” corpus (≈ 2 M embeddings).  

---

## 8. Milestones & Timeline

| Milestone | Deliverable | Duration | Owner |
|-----------|-------------|----------|-------|
| **M1 – Foundations** | Repo scaffolding, CI/CD, basic canvas UI | 4 weeks | Front‑end Lead |
| **M2 – Generation Core** | Fine‑tuned diffusion model, vLLM integration, latency < 5 s | 6 weeks | ML Engineer |
| **M3 – Feedback Loop** | Capture thumbs, style sliders, conditioning pipeline | 3 weeks | Product Engineer |
| **M4 – Versioning & Export** | Version history, PNG/PSD/SVG export with manifest | 3 weeks | Backend Lead |
| **M5 – Safety Guardrails** | Similarity check, auto‑regeneration, unit tests | 2 weeks | Security Engineer |
| **M6 – Beta Release** | Closed beta with 3 partner studios, collect NPS | 4 weeks | PM |
| **M7 – Collaboration & Plugins** | Multi‑user OT, Photoshop plug‑in | 5 weeks | Collaboration Team |
| **M8 – Public Launch** | Full product, analytics dashboard, documentation | 2 weeks | Release Manager |

**Total Time to Launch:** ~30 weeks (≈ 7 months)

---

## 9. Risks & Mitigations

| Risk | Impact | Likelihood | Mitigation |
|------|--------|------------|------------|
| Model generates copyrighted‑like output | Legal / IP | Medium | Similarity engine + curated training set; legal review of edge cases. |
| Latency exceeds 5 s under load | User churn | High | Horizontal scaling of vLLM nodes; cache recent feedback vectors. |
| Artists reject “human‑in‑the‑loop” feel | Adoption | Low | Early UX testing; ensure feedback UI is unobtrusive and fast. |
| Data privacy breach | Compliance | Low | End‑to‑end encryption, minimal data retention policy. |
| Integration complexity with external apps | Delayed launch | Medium | Build plug‑in adapters as thin wrappers; use standard file formats. |

---

## 10. Open Questions

1. **Dataset Curation:** What proportion of the existing 7M pairs will be earmarked for “concept‑only” fine‑tuning?  
2. **Pricing Model:** Subscription tier vs. per‑seat licensing – need finance input.  
3. **Beta Partner Selection:** Which studios have expressed interest and can provide rapid feedback?  

---

## 11. Appendices

- **A. Glossary** – Definitions for terms such as “feedback vector”, “similarity threshold”, etc.  
- **B. Reference Architecture** – Detailed component diagram (to be added in Confluence).  
- **C. Compliance Checklist** – GDPR/CCPA data handling matrix.  

--- 

*End of Document*
