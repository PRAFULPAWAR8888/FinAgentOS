# FinAgentOS Architecture

## 1. System Overview

FinAgentOS is a governed, multi-agent AI platform for intelligent financial services.

The platform is designed with security, authorization, observability, auditability, and human oversight as core principles.

## 2. High-Level Architecture

```text
User
  ↓
Streamlit Web UI
  ↓
FastAPI Backend
  ↓
Application Services
  ↓
Agentic Workflows
  ↓
┌──────────────────────────────────────┐
│ Supervisor Agent                     │
│   ↓                                  │
│ Financial Analysis Agent             │
│   ↓                                  │
│ Credit Risk Agent                    │
│   ↓                                  │
│ Compliance Agent                     │
│   ↓                                  │
│ Decision Agent                       │
└──────────────────────────────────────┘
  ↓
Security & Governance
  ↓
┌──────────────┬──────────────┬──────────────┐
│ PostgreSQL   │ ML Models    │ MCP Servers  │
│ + pgvector   │              │              │
└──────────────┴──────────────┴──────────────┘

## 3. Core Principles

- Security-first architecture
- Least-privilege authorization
- Know Your Agent (KYA)
- Granular user consent
- Human-in-the-loop for high-risk actions
- Deterministic financial calculations
- Governed machine-learning models
- Controlled RAG
- MCP security and validation
- Structured logging and observability
- Complete auditability
- Safe failure and controlled side effects