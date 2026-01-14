# TradeSight AI Agent
## Multi-Agent System for Trade Surveillance Alert Triage

A production-grade portfolio project demonstrating end-to-end product management in AI systems—from user research and technical architecture through working prototype and governance frameworks.

---

## Problem Context

Financial institutions face a persistent challenge in trade surveillance operations. Compliance teams must investigate thousands of system-generated alerts monthly to detect potential market abuse—spoofing, layering, front-running, and manipulation. Industry research indicates that traditional rule-based surveillance systems generate substantial false positive rates, requiring manual investigation of each alert.

**Observed Pain Points:**
- Analysts manually gather context from disparate systems per alert
- Investigation requires cross-referencing trade data, communications, market conditions, and patterns
- High cognitive load from volume contributes to fatigue and delays  
- Regulatory bodies mandate timely investigation, directly impacting risk, cost, and retention

---

## Solution Overview

A multi-agent AI system that automates the investigative workflow, synthesizing data from disparate sources and providing analysts with context-rich recommendations alongside transparent reasoning.

**Core Capabilities:**
1. **Automated Data Aggregation**: Retrieve relevant trade history, client profiles, market conditions without manual lookup
2. **Pattern Recognition**: Identify statistical anomalies and compare against historical surveillance cases
3. **Context Enrichment**: Surface relevant communications and external market events
4. **Structured Decision Support**: Generate preliminary assessment with evidence and recommended next steps

**Design Principles:**
- **Human-in-the-loop**: System provides recommendations; humans make final decisions (regulatory requirement)
- **Explainability**: Complete reasoning chain for every recommendation
- **Audit Trail**: Immutable logs of all agent actions and data sources consulted
- **Fail-Safe**: Conservative bias toward escalation when uncertain

---

## Getting Started

### Prerequisites
- Python 3.11+
- Docker & Docker Compose (optional, for containerized deployment)
- API keys: OpenAI, Anthropic, Pinecone, LangSmith

### Quick Start

1. **Clone and setup:**
   ```bash
   git clone <repo-url>
   cd tradesight-ai-agent
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

2. **Configure environment:**
   ```bash
   cp .env.example .env
   # Fill in API keys and database credentials
   ```

3. **Run Streamlit dashboard:**
   ```bash
   streamlit run src/streamlit_app.py
   ```

4. **Or deploy with Docker:**
   ```bash
   docker-compose up
   ```

---

## Technical Stack

**Backend:**
- Python 3.11, LangGraph, FastAPI, PostgreSQL, Redis

**AI/ML:**
- OpenAI GPT-4o, Claude Sonnet, text-embedding-3-large, Pinecone, pandas, scipy

**Frontend:**
- Streamlit (prototype), Plotly

```
tradesight-ai-agent/
├── README.md
├── docs/
│   ├── PRD.md
│   ├── TECHNICAL_DESIGN.md
│   ├── SPRINT_PLAN.md
│   └── user-stories.csv
├── src/
│   ├── agents/
│   │   ├── data_retrieval.py
│   │   ├── pattern_analysis.py
│   │   ├── context_enrichment.py
│   │   └── decision_synthesis.py
│   ├── orchestrator.py
│   ├── api.py
│   └── streamlit_app.py
├── tests/
│   ├── test_agents.py
│   └── fixtures/
├── docker-compose.yml
└── requirements.txt
```

---

## Demonstration Scope

This repository demonstrates **end-to-end product thinking** through design-phase artifacts and prototype validation of architectural approach.

**What's Demonstrated:**

*Product & Process:*
- User research methodology applied to problem validation
- RICE-based feature prioritization and MVP scoping
- Agile sprint planning with clear deliverables
- Risk mitigation and governance frameworks for regulated environments
- Metrics-driven decision-making approach

*Technical Architecture:*
- Multi-agent system design pattern with LangGraph orchestration
- REST API contract specification for production integration
- Decision logic framework (Escalate | Monitor | Dismiss)
- Scalability patterns: parallel agent execution, caching, smart routing
- Governance controls: audit trails, explainability requirements, human-in-the-loop design

*Prototype Implementation:*
- Mock implementation of 4-agent architecture demonstrating orchestration pattern
- Streamlit dashboard showing UI flow and analyst decision points
- API specification with request/response contracts
- Sample alert analysis flow showing evidence mapping and recommendations

**What's Not Included in Prototype:**
- Live database connections (PostgreSQL, Pinecone) - architecture specified, not integrated
- Real LLM integrations (GPT-4o, Claude) - pattern designed, using mock responses
- Production infrastructure (Kubernetes, monitoring, logging) - infrastructure designed in technical docs
- Historical case library - vector store design specified, not populated

**Validation Approach:**
The prototype validates the architectural approach through mock implementation: user flows, API contracts, agent interaction patterns, and decision logic are testable without external service dependencies.

---

## Repository Purpose

This repository demonstrates product management and technical execution in AI systems:

**Product & Strategy:**
- User research methodology (interviews, shadowing, personas)
- RICE-based prioritization and MVP scoping
- Regulatory and compliance-driven requirements
- Stakeholder alignment across technical/business/legal

**Execution:**
- Agile delivery with clear sprint goals and demos
- Technical specifications (API contracts, data models, architecture)
- Risk mitigation and governance frameworks
- Metrics-driven approach to decision-making

**Technical Depth:**
- Multi-agent AI system design and orchestration
- LLM integration and cost optimization
- Production-grade observability and failover strategies
- Hands-on implementation across agents, API, and UI

**Communication:**
- PRDs, technical design docs, and user stories
- Executive and technical audience customization
- Clear problem framing and decision transparency

---

## Documentation

- [Portfolio Specs](ai_pm_portfolio_specs.md) — Full product and technical vision
- [PRD](docs/PRD.md) — Product requirements and user research
- [Technical Design](docs/TECHNICAL_DESIGN.md) — Architecture specifications and governance
- [Sprint Plan](docs/SPRINT_PLAN.md) — 6-week MVP delivery roadmap
- [User Stories](docs/user-stories.csv) — Detailed requirements

