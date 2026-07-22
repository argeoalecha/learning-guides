# ShopFast

Used by: **[DevOps/SRE guide](../../devops-sre/devops-sre_learning_guide.html)**

**Not a downloadable dataset.** ShopFast is a containerized e-commerce platform the learner provisions, deploys, and operates across the guide — the exercise is standing up and running the infrastructure, not downloading a finished system.

## Stack

- API: Python/Flask
- Database: PostgreSQL
- Cache/queue: Redis

## Progression across the guide

1. **Phase 1 (Foundations, Weeks 1–4):** Linux fundamentals, Git, shell scripting. Capstone: **Bootstrap ShopFast** (get the Flask app running on a VM manually).
2. **Phase 2 (Containers & Orchestration):** Docker, Kubernetes fundamentals and production patterns. Capstone: **Containerize & Deploy**.
3. **Phase 3 (Infrastructure as Code, Weeks 9–13ish):** Terraform, Ansible, cloud fundamentals. Capstone: **Provision ShopFast** (from code, not by hand).
4. **Phase 4 (CI/CD & Delivery, Weeks 14–16):** pipelines, GitOps. Capstone: **Ship It**.
5. **Phase 5 (SRE & Reliability, Weeks 17–20):** observability, SLOs/error budgets, incident response. Capstone: **Run the System**.
6. **Final Capstone:** Operate ShopFast — the full stack, provisioned as code, deployed via CI/CD, observed and held to an SLO.

## Notes

- No pre-seeded database schema is prescribed by the guide beyond "a containerized e-commerce platform" — pick a minimal products/orders schema (e.g., reuse the shape from [`tindahub/`](../tindahub/) or [`shopph/`](../shopph/) if you want a head start) since the point of this guide is the infrastructure around the app, not the app's own business logic.
