# TradeSight AI Agent
## Multi-Agent System for Trade Surveillance Alert Triage

A production-grade portfolio project demonstrating end-to-end product management in AI systems—from user research and technical architecture through working prototype and governance frameworks.

---

## Problem Context

Financial institutions face a persistent challenge in trade surveillance operations. Compliance teams must investigate thousands of system-generated alerts monthly to detect potential market abuse—spoofing, layering, front-running, and manipulation. Industry research indicates that traditional rule-based surveillance systems generate substantial false positive rates, requiring manual investigation of each alert.

**Observed Pain Points:**
- Analysts manually gather context from 5+ disparate systems per alert
- Investigation requires cross-referencing trade data, communications, market conditions, and patterns
- High cognitive load from volume contributes to fatigue and delays  
- Regulatory (FINRA, FCA, MAS) mandate timely investigation, directly impacting risk, cost, and retention

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

### Working Prototype

**What's Included:**
- Functional multi-agent system with 4 specialized agents.
- 50 synthetic test alerts covering spoofing, layering, and front-running scenarios.
- Streamlit interface showing an alert queue, detailed analysis, and agent reasoning traces.
- LangSmith integration for observability.
- Docker Compose setup for local deployment.

**What's Simulated:**
- Market data API (using JSON fixtures).
- Communication search (using pre-indexed sample emails).
- Historical case library (10 labeled examples).

### Demo Flow
1. Analyst opens a dashboard and sees a queue of alerts.
2. Selects a high-priority alert.
3. The system displays a summary, agent analysis, a recommendation (e.g., "ESCALATE"), and supporting evidence.
4. The analyst reviews the reasoning and approves the escalation, routing it to a senior analyst.
5. The system logs the decision with a full audit trail.

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
- [Technical Design](docs/TECHNICAL_DESIGN.md) — Architecture and API specifications
- [Sprint Plan](docs/SPRINT_PLAN.md) — 6-week MVP delivery roadmap
- [User Stories](docs/user-stories.csv) — Detailed requirements

---

## Demonstration Scope

**Working Prototype Includes:**
- Functional multi-agent system (4 specialized agents)
- 50 synthetic test alerts (spoofing, layering, front-running)
- Streamlit dashboard with alert queue and analysis views
- LangSmith integration for observability
- Docker Compose setup for local deployment

**MVP Features:**
- Data retrieval agent (trade data, client profiles, market data)
- Pattern analysis agent (statistical anomalies, historical matching)
- Decision synthesis with structured recommendations
- Web interface for analyst review queue

See [ai_pm_portfolio_specs.md](ai_pm_portfolio_specs.md) for complete feature breakdown and roadmap.