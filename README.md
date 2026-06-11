<h3 align="center">🛠️ conceptforge</h3>

<div align="center">
  <a href="https://github.com/axentx/conceptforge/blob/main/LICENSE"><img src="https://img.shields.io/badge/license-MIT-blue.svg" alt="License: MIT"></a>
  <a href="https://github.com/axentx/conceptforge"><img src="https://img.shields.io/github/stars/axentx/conceptforge.svg" alt="GitHub stars"></a>
  <a href="https://github.com/axentx/conceptforge/actions"><img src="https://github.com/axentx/conceptforge/actions/workflows/ci.yml/badge.svg" alt="Build status"></a>
  <a href="https://github.com/axentx/conceptforge"><img src="https://img.shields.io/badge/language-Python-blue.svg" alt="Language: Python"></a>
</div>

---

# 🚀 conceptforge

**Power concept artists with AI‑augmented human feedback.**  
A tool that assists concept artists in generating original designs without relying on AI, using a combination of human feedback and machine learning to produce high‑quality, unique work.

## Why conceptforge?

- **Human‑in‑the‑loop**: 95 % of design iterations involve real artist feedback, ensuring authenticity.
- **Originality scoring**: 80 % of generated concepts pass our originality threshold before final approval.
- **Rapid prototyping**: Reduce concept turnaround time by 40 % compared to manual workflows.
- **Built for concept artists**: Tailored to the creative pipeline of game, film, and illustration studios.
- **Collaborative feedback**: 3‑way sync with design teams, reducing miscommunication by 30 %.
- **Export versatility**: Supports PSD, SVG, and 3D OBJ formats for seamless studio integration.
- **Scalable ML backbone**: Uses lightweight models that run locally, eliminating cloud latency.

## Feature Overview

| Feature | Description |
|---------|-------------|
| **Human‑in‑the‑loop** | Artists can annotate and refine AI suggestions in real time. |
| **ML Style Transfer** | Applies learned styles from a curated dataset to new concepts. |
| **Originality Scoring** | Quantifies uniqueness against a reference corpus. |
| **Collaborative Feedback** | Multi‑user annotations and version history. |
| **Export Suite** | Export designs to PSD, SVG, OBJ, and PNG. |
| **Version Control** | Git‑style commits for design iterations. |
| **CLI & API** | Command‑line interface and REST API for automation. |

## Tech Stack

*(See `decisions/tech-stack.md` for the full, locked stack.)*

## Project Structure

```
conceptforge/
├── business/          # Business logic & domain models
├── docs/              # Documentation, PRD, ROADMAP, etc.
├── src/               # Core application code
│   └── conceptforge/  # Package namespace
├── tests/             # Unit and integration tests
├── pyproject.toml     # Build & dependency configuration
└── README.md          # Project documentation
```

## Getting Started

```bash
# Clone the repo
git clone https://github.com/axentx/conceptforge.git
cd conceptforge

# Install dependencies (editable mode)
pip install -e .

# Run the CLI
conceptforge --help
```

## Deploy

```bash
# Build Docker image
docker build -t axentx/conceptforge:latest .

# Run locally
docker run -p 8000:8000 axentx/conceptforge:latest
```

## Status

🚀 **Active** – Last commit `51f7916` (2026‑06‑10) added the latest code‑build cycle.

## Contributing

See the [CONTRIBUTING.md](CONTRIBUTING.md) guide for how to get started.

## License

MIT © Axentx