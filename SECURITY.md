# FinAgentOS Security

## 1. Security Principles

FinAgentOS follows a security-first design.

The system treats the following as untrusted:

- User input
- LLM output
- Retrieved documents
- Tool descriptions
- MCP metadata
- MCP tool results
- External API responses

No untrusted input is allowed to directly execute sensitive actions.

## 2. Core Security Controls

FinAgentOS will implement:

- Authentication
- Authorization
- Role-based access control (RBAC)
- Know Your Agent (KYA)
- Least-privilege permissions
- Granular user consent
- Tool permission checks
- Transaction and action limits
- Input and output validation
- Prompt-injection defenses
- MCP security controls
- Human approval for high-risk actions
- Audit logging
- Secret management
- Rate limiting where appropriate
- Secure error handling

## 3. Sensitive Actions

Sensitive financial actions must never be executed solely because an LLM requested them.

Examples include:

- Payments
- Loan applications
- Account modifications
- Consent changes
- Financial data access

These actions require appropriate authorization, consent, risk evaluation, limits, and auditability.

## 4. Security Rule

LLMs may reason and recommend, but they cannot bypass deterministic security, authorization, consent, risk, or policy controls.