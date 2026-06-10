# ROADMAP.md – conceptforge

## Vision
Empower concept artists to rapidly explore original visual ideas **without** the unpredictability of black‑box generative AI.  
We combine **human‑in‑the‑loop feedback** with lightweight, domain‑specific machine‑learning models to iteratively refine sketches, palettes, and composition suggestions, delivering high‑quality, unique concepts that remain fully owned by the artist.

---

## MVP (Must‑Have for Launch) – **Release 0.1**

| Feature | Description | Owner | Acceptance Criteria |
|---------|-------------|-------|----------------------|
| **Core UI** | Minimal web app (React + Vite) with canvas, toolbar, and feedback panel. | Front‑end Lead | Artists can upload a sketch, draw on canvas, and submit feedback. |
| **Feedback Loop Engine** | Server‑side service (FastAPI) that ingests artist feedback (e.g., “more contrast”, “tighten silhouette”) and updates a lightweight model (fine‑tuned Stable Diffusion‑lite). | ML Engineer | Model returns a revised image within 5 s; feedback improves a quantitative similarity score. |
| **Model Hosting** | Containerised inference using **vLLM** for low‑latency generation. | DevOps | Scales to 200 concurrent users on a single GPU node (RTX 4090). |
| **Versioned Asset Store** | Simple S3‑backed storage with versioning for each concept iteration. | Backend Lead | Artists can revert to any previous version. |
| **Export & License** | Export final concept as PNG/SVG with embedded usage rights metadata. | Product Lead | Download works, metadata matches schema, and legal disclaimer displayed. |
| **Basic Analytics** | Track number of iterations, time per iteration, and user satisfaction (1‑5 star). | Data Engineer | Dashboard shows daily active users ≥ 10 in beta. |
| **Documentation & Onboarding** | Quick‑start guide, FAQ, and in‑app tutorial. | Technical Writer | New user completes first iteration in < 10 min. |

**MVP Success Metric:** 100 paying beta artists complete ≥ 5 concept cycles each within 30 days of launch.

---

## Phase 1 – **v1.0** (Quarter 2 2026)

**Theme:** *Polish & Collaboration*

| Epic | Target Release | Key Stories |
|------|----------------|-------------|
| **Collaborative Workspaces** | v1.0‑alpha | • Invite teammates, share live canvas.<br>• Real‑time cursor & annotation sync. |
| **Advanced Feedback Types** | v1.0‑beta | • Semantic tags (style, mood, era).<br>• Brush‑stroke‑level constraints. |
| **Model Library** | v1.0‑rc | • Switch between “Sketch‑Boost”, “Palette‑Guide”, “Composition‑Assist”.<br>• Community‑contributed fine‑tuned checkpoints. |
| **Asset Management UI** | v1.0‑GA | • Tagging, search, and collection folders.<br>• Bulk export (PDF, PSD). |
| **Performance Optimisation** | v1.0‑GA | • GPU‑offload to vLLM + SGLang for structured generation.<br>• Latency < 3 s for 1024×1024 output. |
| **Pricing & Billing** | v1.0‑GA | • Tiered subscription (Free, Pro, Studio).<br>• Usage‑based credits for extra GPU minutes. |
| **Compliance & IP Guard** | v1.0‑GA | • Automated plagiarism check against public datasets.<br>• Legal audit of generated assets. |

**Milestones**
- **M1 (4 weeks):** Collaborative canvas prototype + real‑time sync.
- **M2 (8 weeks):** Feedback taxonomy & UI integration.
- **M3 (12 weeks):** Model switcher & community upload pipeline.
- **M4 (16 weeks):** Full billing integration & public beta launch.

---

## Phase 2 – **v2.0** (Quarter 4 2026)

**Theme:** *Intelligence & Ecosystem*

| Epic | Target Release | Key Stories |
|------|----------------|-------------|
| **AI‑Assisted Storyboarding** | v2.0‑alpha | • Generate multi‑panel sequences from a single concept.<br>• Auto‑layout suggestions. |
| **Cross‑Tool Plug‑ins** | v2.0‑beta | • Photoshop & Blender plug‑ins for seamless import/export.<br>• Unity/Unreal asset pipeline hooks. |
| **Personalised Style Models** | v2.0‑rc | • On‑device fine‑tuning using artist’s own portfolio (privacy‑preserving). |
| **Marketplace** | v2.0‑GA | • Artists sell/licence generated concepts.<br>• Revenue‑share smart contracts. |
| **Analytics Dashboard** | v2.0‑GA | • Heatmaps of feedback impact.<br>• ROI estimator for concept‑to‑production pipelines. |
| **Enterprise Admin Console** | v2.0‑GA | • Role‑based access, SSO, audit logs. |
| **Research Loop** | Ongoing | • Continuous data collection → retrain models → push updates without downtime. |

**Milestones**
- **M1 (4 weeks):** Storyboard generation engine (vLLM + SGLang).
- **M2 (8 weeks):** Plugin SDK & first Photoshop plug‑in.
- **M3 (12 weeks):** Personalised model training pipeline (FedAvg style).
- **M4 (16 weeks):** Marketplace MVP + payment gateway.
- **M5 (20 weeks):** Enterprise admin release & full GA.

---

## Long‑Term Outlook (2027+)

| Horizon | Vision |
|---------|--------|
| **AI‑Free Guarantee** | Formal certification that no proprietary generative AI data is used without explicit artist consent. |
| **Multimodal Fusion** | Combine text prompts, audio mood‑boards, and motion references to drive concept generation. |
| **AR/VR Collaboration** | Immersive shared studio where artists manipulate 3D concepts in real time. |
| **Open‑Source Core** | Release the feedback‑loop engine under a permissive license, fostering community extensions while retaining commercial SaaS layers. |

---

## How We Measure Success

| KPI | Target (12 mo) |
|-----|----------------|
| **Paid Users** | 2 000 active subscriptions |
| **Iteration Velocity** | Avg. 4 iterations per concept ≤ 3 min each |
| **Churn Rate** | < 5 % monthly |
| **Revenue** | $250 k ARR |
| **Artist Satisfaction** | ≥ 4.5 / 5 stars |
| **Model Quality** | Human‑rated improvement ≥ 30 % over baseline sketches |

---

*Prepared by the conceptforge product & engineering leadership team – June 2026*
