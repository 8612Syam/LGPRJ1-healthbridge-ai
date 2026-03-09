# 🏥 HealthBridge AI
**AI-powered Healthcare Data Platform**

> Built by [Syamkumar Satheesan](https://www.linkedin.com/in/syamkumar-satheesan) | PMI-CPMAI | Azure Certified | GCP Certified

---

## 🔍 What Is This?

HealthBridge AI is a three-module portfolio project demonstrating AI-powered 
healthcare data engineering — built on real problems from the payer/provider 
ecosystem.

Every API is fully documented with **interactive Swagger UI** — live demo 
available.

---

## 📦 Three Modules

### Module 1 — HL7 v2 → FHIR Transformation Engine
Ingests legacy HL7 v2 messages (ORU^R01), maps OBX segments to FHIR R4 
Observation resources, and exposes a FHIR-compliant REST API — with RBAC 
controlling which role sees which data.

**Why this matters:** CMS mandates FHIR APIs by 2026. Every payer 
(Elevance, BCBSA, HealthEdge) is running this migration right now.

### Module 2 — RBAC Vectorless RAG
BM25 statistical retrieval (no vector database) with a four-layer RBAC model 
built on NetworkX. Role-filtered knowledge retrieval — PHI never returned to 
unauthorized roles.

**Why vectorless:** Explainable, audit-friendly, HIPAA-aligned. No GPU, 
no embedding costs.

### Module 3 — AI Evaluation Pipeline
Promptfoo test suite for functional evaluation, RBAC boundary testing, and 
red teaming protocol — applied to the outputs from Modules 1 and 2.

---

## 🌐 Live Demo & Swagger UI
> 🔗 Live URL: *(coming Week 6 — Replit deployment)*
> 
> Once live:
> - `/docs` → Interactive Swagger UI
> - `/redoc` → ReDoc API documentation  
> - `/openapi.json` → OpenAPI specification

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| Language | Python 3.11 |
| API Framework | FastAPI + Uvicorn |
| API Docs | Swagger UI (OpenAPI 3.0) |
| HL7 Parsing | hl7apy |
| FHIR Resources | fhir.resources (R4) |
| Retrieval | BM25 via rank-bm25 |
| Database | SQLite |
| Graph / RBAC | NetworkX |
| AI Assist | Claude API |
| Evaluation | Promptfoo |
| Visualization | Power BI Desktop |
| Deployment | Replit (free tier) |
| Version Control | GitHub + GitHub Desktop |

---

## 📁 Repository Structure
```
LGPRJ1-healthbridge-ai/
├── module1-fhir-pipeline/     # HL7 v2 → FHIR transformation
├── module2-rbac-rag/          # Vectorless RAG with RBAC
├── module3-ai-eval/           # AI evaluation pipeline
├── docs/                      # Architecture diagrams
└── README.md
```

---

## 🗓️ Build Status

| Module | Status | Target |
|--------|--------|--------|
| Module 1 — FHIR Pipeline | 🔄 In Progress | Week 4 |
| Module 2 — RBAC RAG | ⏳ Planned | Week 6 |
| Module 3 — AI Eval | ⏳ Planned | Week 7 |
| Power BI Dashboard | ⏳ Planned | Week 8 |

---

## 📋 Domain Context

Built on 17+ years of healthcare IT experience across:
- **Payer platforms** — large-scale data warehouse migrations, 
  member enrollment, claims processing, provider data management
- **Regulatory compliance** — HIPAA, CMS mandates, prior 
  authorization workflows, audit and governance frameworks
- **Standards:** HL7 v2, FHIR R4, X12 EDI, CMS-0057-F

---

## 📜 License
MIT License — © 2026 Syamkumar Satheesan  
See [LICENSE](LICENSE) for details.
