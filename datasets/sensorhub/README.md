# SensorHub

Used by: **[Web App Product Dev guide](../../webapp-product-dev/webapp-product-dev_learning_guide.html)**

**Not a downloadable dataset.** SensorHub is a multi-tenant IoT equipment-monitoring SaaS webapp the learner specs, designs, and builds across all 5 phases of the guide — starting from a PRD, not from code or data.

## What it is

A SaaS product where users upload sensor CSVs, receive AI-generated anomaly reports, and manage equipment assets — multi-tenant (each customer's data is isolated).

## Progression across the guide

1. **Phase 1 (Product):** write the SensorHub PRD (user stories, acceptance criteria, MoSCoW prioritization — "Must Haves" only until proven otherwise).
2. **Phase 2:** (design/architecture modules)
3. **Phase 3 (Weeks 11–13):** testing & CI/CD — Vitest, Playwright, Vercel.
4. **Phase 4:** (further build-out modules)
5. **Final Capstone (Ongoing):** full SensorHub launch.

## Notes

- Since the guide's own Module 1.1 has the learner *write the PRD from scratch as the first exercise*, this README deliberately doesn't prescribe a tech stack or schema — inventing that spec (equipment assets, sensor readings, anomaly reports, tenant/org model) is the point of Phase 1. Treat any schema decision as something you own once you've done that exercise, not something this file should pre-decide for you.
- If you need a sensor-data CSV shape to prototype against once you reach the upload/anomaly-report modules, a minimal starting shape is: `equipment_id, sensor_type, timestamp, reading_value, unit` — refine it against your own PRD's acceptance criteria.
