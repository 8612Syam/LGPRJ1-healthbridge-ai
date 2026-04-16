# 🏥 HealthBridge AI
**AI-powered Healthcare Data Platform**

> Built by [Syamkumar Satheesan](https://www.linkedin.com/in/syamkumar-satheesan) | PMI-CPMAI | Azure Certified | GCP Certified

---

## 🔍 What Is This?
HealthBridge AI is a three-module portfolio project demonstrating AI-powered healthcare data engineering — built on real problems from the payer/provider ecosystem.

---

## 📦 Three Modules

### Module 1 — HL7 v2 → FHIR Transformation Engine
Ingests legacy HL7 v2 messages (ORU^R01), maps OBX segments to FHIR R4 Observation resources, and exposes a FHIR-compliant REST API.
* **Status:** ✅ **Core Logic Complete.** HL7 parsing and FHIR mapping (Patient/Observation) verified.

### Module 2 — RBAC Vectorless RAG
BM25 statistical retrieval (no vector database) with a four-layer RBAC model built on NetworkX. 
* **Why vectorless:** Explainable, audit-friendly, HIPAA-aligned. No GPU, no embedding costs.
* **Status:** 🔄 **In Planning.** ### Module 3 — AI Evaluation Pipeline
Promptfoo test suite for functional evaluation, RBAC boundary testing, and red teaming protocol.

---

## 🗓️ Build Status

| Module | Status | Target |
|--------|--------|--------|
| **Module 1 — FHIR Pipeline** | ✅ **Logic Complete** | Week 4 |
| **Module 2 — RBAC RAG** | 🔄 In Progress | Week 6 |
| **Module 3 — AI Eval** | ⏳ Planned | Week 7 |
| **Power BI Dashboard** | ⏳ Planned | Week 8 |

---

## 🛠️ Tech Stack (Updated)

| Layer | Technology |
|-------|-----------|
| **Language** | Python 3.12.10 (Windows 11) |
| **Environment** | venv (Managed via `python -m pip`) |
| **API Framework** | FastAPI + Uvicorn |
| **HL7 / FHIR** | hl7apy, fhir.resources (R4) |
| **Retrieval** | BM25 via rank-bm25 |
| **Graph / RBAC** | NetworkX |
| **Version Control** | GitHub + GitHub Desktop |

---

## 📋 Domain Context
Built on 17+ years of healthcare IT experience across:
- **Payer platforms** — large-scale data warehouse migrations, member enrollment, claims processing.
- **Regulatory compliance** — HIPAA, CMS mandates, prior authorization workflows.
- **Standards:** HL7 v2, FHIR R4, X12 EDI, CMS-0057-F.

---

## 📜 License
MIT License — © 2026 Syamkumar Satheesan