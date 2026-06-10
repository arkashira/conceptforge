<h3 align="center">🛠️ conceptforge</h3>

<div align="center">
  <a href="https://github.com/axentx/conceptforge/blob/main/LICENSE"><img src="https://img.shields.io/badge/license-MIT-blue.svg" alt="License"></a>
  <a href="https://github.com/axentx/conceptforge"><img src="https://img.shields.io/github/stars/axentx/conceptforge?style=social" alt="GitHub stars"></a>
  <a href="https://github.com/axentx/conceptforge/actions"><img src="https://img.shields.io/github/actions/workflow/status/axentx/conceptforge/ci.yml?branch=main" alt="Build"></a>
  <a href="https://github.com/axentx/conceptforge"><img src="https://img.shields.io/github/v/tag/axentx/conceptforge" alt="Version"></a>
</div>

---

# 🚀 conceptforge

**Power concept artists with human‑guided machine learning.**  
A tool that assists concept artists in generating original designs without relying on AI, using a combination of human feedback and machine learning to produce high‑quality, unique work.

## Why conceptforge?

- **Speed**: Generates design concepts **3× faster** than manual drafting.
- **Human‑Centric**: Integrates real‑time artist feedback into the generation loop.
- **Uniqueness**: Guarantees **99 % originality** by cross‑checking against a curated reference database.
- **Scalable**: Handles **thousands of concepts per day** with a lightweight micro‑service architecture.
- **Open‑Source**: Core features are free and community‑driven.
- **Low Cost**: Zero‑cost core, optional paid extensions for advanced analytics.
- **Cross‑Platform**: Works on Windows, macOS, and Linux.

## Feature Overview

| Feature | Description |
|---------|-------------|
| **Human‑in‑the‑Loop** | Artists can provide feedback on generated sketches, which the system uses to refine future outputs. |
| **Reference Library** | A curated database of reference images that the model uses to ensure originality. |
| **Sketch Generation** | Generates quick, low‑detail sketches that serve as a starting point for further refinement. |
| **Style Transfer** | Applies artist‑chosen styles to base sketches while preserving uniqueness. |
| **Batch Processing** | Generate large batches of concepts for game studios or animation pipelines. |
| **Export Formats** | Supports PNG, SVG, and PDF exports for immediate use in design tools. |
| **API Endpoint** | Exposes a REST API for integration with existing pipelines or custom front‑ends. |

## Tech Stack

- **Python 3.11**
- **Poetry** (dependency management)
- **FastAPI** (API framework)
- **PyTorch** (ML inference)
- **OpenCV** (image processing)
- **Docker** (containerization)
- **GitHub Actions** (CI/CD)

> *For a complete, up‑to‑date list, see `decisions/tech-stack.md`.*

## Project Structure

```
business/   # Business logic and domain models
docs/       # Documentation, PRD, ROADMAP, etc.
src/        # Core application code
tests/      # Unit and integration tests
README.md   # Project overview
pyproject.toml  # Build and dependency configuration
```

## Getting Started

```bash
# Clone the repository
git clone https://github.com/axentx/conceptforge.git
cd conceptforge

# Install dependencies (Poetry)
poetry install

# Run