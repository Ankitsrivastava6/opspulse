# OpsPulse

> Mobile-first DevOps Command Center for a one-person engineering workflow.

OpsPulse is a portfolio-grade Android + DevOps platform designed to demonstrate:

- Android development
- Git/GitHub
- GitHub Actions
- CI/CD
- Docker
- Terraform
- Cloud infrastructure
- Monitoring
- Logging
- Security
- SRE practices
- Automated release management
- Rollback strategies

## Project Status

🚧 Phase 0 — Environment & Repository Foundation

## Architecture

```text
Android App
     |
     v
OpsPulse API
     |
     +---- GitHub
     |
     +---- CI/CD
     |
     +---- Monitoring
     |
     +---- Logging
     |
     v
Production Infrastructure


Repository Structure

android/          Android application
backend/          Backend API
infrastructure/   Terraform infrastructure
docker/            Container configuration
monitoring/       Metrics, logs and dashboards
scripts/           Automation scripts
docs/              Documentation
tests/             Cross-component tests
.github/           GitHub workflows and configuration
