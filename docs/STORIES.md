# STORIES.md

## Overview
**Product:** **conceptforge** – a hybrid design assistant for concept artists that blends human‑in‑the‑loop feedback with lightweight machine‑learning models to generate original, high‑quality artwork without relying on black‑box generative AI.  

The backlog below is organized into **Epics** that map to the core product pillars: **Feedback Loop**, **Model Engine**, **Artist Workspace**, **Collaboration & Export**, and **Production‑Ready Ops**. Stories are ordered to deliver a Minimum Viable Product (MVP) first, then iterate toward a polished, market‑ready release.

---

## EPIC 1 – Human‑in‑the‑Loop Feedback Loop
*Enable artists to steer the generation process through intuitive, iterative feedback.*

| # | User Story | Acceptance Criteria |
|---|------------|----------------------|
| 1.1 | **As a concept artist, I want to submit a rough sketch as a reference, so that the system can base its suggestions on my style.** | - UI provides a drag‑and‑drop area for image upload.<br>- Uploaded image is stored and displayed as a thumbnail.<br>- System extracts visual features within 2 seconds and makes them available to the generation engine. |
| 1.2 | **As a concept artist, I want to rate each generated suggestion (thumbs‑up / thumbs‑down), so that the model learns my preferences.** | - Each suggestion shows clear rating buttons.<br>- Rating is persisted to the user’s feedback store.<br>- After 5 ratings, the next generation batch reflects the updated preference vector (observable change in style). |
| 1.3 | **As a concept artist, I want to add textual “prompt hints” to a suggestion, so that I can guide specific elements (e.g., “add cyberpunk neon”).** | - A text field is attached to every suggestion.<br>- Hints are sent to the model as weighted tokens.<br>- New suggestions incorporate the hint within 1 generation cycle. |
| 1.4 | **As a product manager, I need a visual “feedback heatmap” that shows which parts of the sketch influenced the model most, so that we can validate the learning loop.** | - Heatmap overlay appears on the reference image after generation.<br>- Colors map to feature importance scores (0‑100%).<br>- Exportable as PNG for internal review. |

---

## EPIC 2 – Lightweight Generation Engine
*Provide a deterministic, controllable ML engine that produces variations without “black‑box” AI.*

| # | User Story | Acceptance Criteria |
|---|------------|----------------------|
| 2.1 | **As a developer, I want a plug‑and‑play model wrapper around the open‑source `vLLM` inference engine, so that we can run generation locally.** | - Wrapper exposes `generate(reference_features, prompt, seed)` API.<br>- Supports CPU‑only and GPU‑accelerated modes.<br>- Latency ≤ 3 seconds for 256×256 output on a single RTX‑4090. |
| 2.2 | **As a concept artist, I want to set a deterministic seed, so that I can reproduce a specific output later.** | - UI includes a “Seed” field with numeric input.<br>- Same seed + same inputs always yields identical output (pixel‑perfect). |
| 2.3 | **As a concept artist, I want to request a batch of N variations (N = 1‑9), so that I can explore multiple directions quickly.** | - Batch size selector present (max 9).<br>- All N images are generated in parallel and displayed in a grid. |
| 2.4 | **As a QA engineer, I need automated regression tests that compare generated hashes against a golden set, so that model updates do not break visual consistency.** | - Test suite runs on every CI build.<br>- Fails if > 2 % of hashes differ from baseline. |

---

## EPIC 3 – Artist Workspace & UI
*Deliver a clean, responsive interface tailored to concept artists’ workflow.*

| # | User Story | Acceptance Criteria |
|---|------------|----------------------|
| 3.1 | **As a concept artist, I want a canvas where I can draw or annotate over generated suggestions, so that I can refine ideas directly.** | - Canvas supports pen, brush, eraser with adjustable size.<br>- Layers: “Reference”, “Generated”, “Annotations”.<br>- Export includes all layers as PSD. |
| 3.2 | **As a concept artist, I want a “history timeline” of my sessions, so that I can revisit earlier versions.** | - Timeline shows thumbnails of each generation step.<br>- Clicking a thumbnail restores that state (reference, prompts, seed). |
| 3.3 | **As a concept artist, I want dark‑mode UI, so that I can work comfortably in low‑light environments.** | - Theme toggle persists per user.<br>- All UI components meet WCAG AA contrast in both modes. |
| 3.4 | **As a product owner, I need the workspace to be responsive on tablets (iPad) and desktops, so that artists can work on their preferred device.** | - Layout adapts to ≥ 1024 px and ≤ 768 px widths.<br>- Touch gestures (pinch‑zoom, drag) work on tablets. |

---

## EPIC 4 – Collaboration & Export
*Allow teams to share, review, and export assets efficiently.*

| # | User Story | Acceptance Criteria |
|---|------------|----------------------|
| 4.1 | **As a lead artist, I want to invite teammates to a project with view‑only or edit permissions, so that we can collaborate securely.** | - Invite via email link.<br>- Permissions: “Viewer”, “Editor”.<br>- Access revocation works instantly. |
| 4.2 | **As a concept artist, I want to export final assets in PNG, JPEG, and layered PSD formats, so that they can be used in downstream pipelines.** | - Export dialog lists all three formats.<br>- PSD includes separate layers for reference, generated, annotations.<br>- Export completes within 2 seconds for 4K resolution. |
| 4.3 | **As a marketing manager, I need a shareable public URL that renders a read‑only gallery of selected suggestions, so that we can showcase work to clients.** | - URL is short, token‑based, expires after configurable period.<br>- Gallery is responsive and includes download buttons (PNG). |
| 4.4 | **As a product analyst, I want usage analytics (time spent, number of generations, rating distribution) per project, so that we can measure engagement.** | - Dashboard shows aggregated metrics per project.<br>- Data updates in near‑real‑time (≤ 5 min). |

---

## EPIC 5 – Production‑Ready Operations
*Ensure reliability, security, and scalability for internal and external users.*

| # | User Story | Acceptance Criteria |
|---|------------|----------------------|
| 5.1 | **As a DevOps engineer, I need Docker images for the backend (model server) and frontend, so that we can deploy consistently across environments.** | - Images built from `Dockerfile` with tags `latest` and `sha‑<commit>`.<br>- Images pass vulnerability scan (CVEs < 7 days old). |
| 5.2 | **As a security officer, I want all user data (reference images, feedback) encrypted at rest, so that we meet GDPR compliance.** | - Data stored in encrypted S3 bucket (AES‑256).<br>- Access controlled via IAM policies. |
| 5.3 | **As a site reliability engineer, I need health‑check endpoints for the model server and UI, so that monitoring can auto‑restart unhealthy pods.** | - `/healthz` returns 200 when model loaded.<br>- Alerts fire on > 2 minute downtime. |
| 5.4 | **As a product owner, I want a feature‑flag system to toggle the “AI‑assisted hints” module, so that we can A/B test with early adopters.** | - Flags stored in a central config service.<br>- UI reacts to flag change without redeploy. |

---

## MVP Scope (Stories to be delivered in Sprint 1‑3)

| Sprint | Stories |
|--------|---------|
| **Sprint 1** (2 weeks) | 1.1, 1.2, 2.1, 2.2, 3.1, 5.1 |
| **Sprint 2** (2 weeks) | 1.3, 2.3, 3.2, 4.1, 5.2 |
| **Sprint 3** (2 weeks) | 1.4, 3.3, 4.2, 5.3, 5.4 |

*All MVP stories are shippable, testable, and provide a complete end‑to‑end workflow: upload reference → generate variations → give feedback → iterate → export.*

--- 

*Prepared by the senior product/engineering lead, conceptforge backlog, 2026‑06‑10.*
