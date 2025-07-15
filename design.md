# Design Document

## Overview
This document describes the architecture and design decisions for the Lead Intelligence Panel, focusing on a modular, OOP-friendly Python (FastAPI) backend and a React frontend.

---

## Backend (Python, FastAPI)

### Structure
- **Framework**: FastAPI (async, type-safe, auto-docs)
- **OOP Principles**: Service classes, repository pattern, dependency injection
- **Modules**: Each feature (scraping, enrichment, scoring, etc.) is a Python package under `backend/app/services/`
- **API Layer**: All endpoints under `backend/app/api/`, grouped by resource
- **Models**: SQLAlchemy ORM models in `backend/app/models/`
- **Schemas**: Pydantic models for request/response validation in `backend/app/schemas/`
- **Repositories**: Data access logic in `backend/app/repositories/`
- **Core**: App config, settings, and startup logic in `backend/app/core/`
- **Utils**: Shared utilities in `backend/app/utils/`
- **Caching**: Redis integration via `redis-py` for API, session, and task caching

### Rationale
- **FastAPI**: Modern, async, type-checked, and auto-generates OpenAPI docs
- **OOP**: Service/repository pattern makes code testable and extensible
- **Modularity**: Each business domain is a package, making it easy to add/replace features
- **Redis**: Central for caching, session, and background task queue (Celery-ready)
- **Extensibility**: New modules (e.g., new enrichment provider) can be added as new packages

---

## Frontend (React)

### Structure
- **Framework**: React (with TypeScript)
- **Component Structure**: Feature-based folders under `frontend/src/components/`
- **Pages**: Route-based pages under `frontend/src/pages/`
- **State Management**: Context API or Zustand (future Redux possible)
- **API Layer**: All API calls in `frontend/src/services/`
- **UI Library**: Material-UI or Chakra UI (to be decided)

### Rationale
- **React**: Modern, component-based, widely adopted
- **Feature Folders**: Easy to scale, each feature (dashboard, lead cards) is a folder
- **TypeScript**: Type safety and better developer experience
- **Extensibility**: New UI features are new components/pages

---

## Shared Principles
- **Documentation**: Each module has its own README, developer.md, design.md, checkpoints.md
- **Testing**: Pytest for backend, React Testing Library for frontend
- **CI/CD**: GitHub Actions (planned)
- **Docker**: For local dev and deployment

---

## Extensibility
- **Backend**: Add new modules by creating new packages in `services/` and registering routers
- **Frontend**: Add new features as new components/pages
- **Caching**: Use Redis for any new caching needs

---

## Design Choices
- **Why FastAPI?** Async, type-safe, auto-docs, great for microservices
- **Why React?** Modern, modular, easy to hire for
- **Why Redis?** Fast, simple, works for cache, session, and queue
- **Why OOP?** Testable, maintainable, extensible

---

## To Do
- Finalize UI library for React
- Set up Celery for background jobs
- Add more module templates for backend

---

**Last updated:** 2024-12-19 

---

## Enrichment Workflow (2024-12-20)

### Overview
- After scraping and normalization, company data is passed to the `EnrichmentService`.
- The service attempts to enrich the data using third-party APIs (Clearbit, Apollo, etc.).
- Fallback logic: If the primary API fails or is missing data, a secondary API is tried.
- The enriched data is then cached and stored.

### Integration Point
- Enrichment is called in each scraper after normalization, before caching/storage.
- This ensures all downstream consumers (cache, DB, API) receive enriched data.

### Impact
- Adds funding, tech stack, employee count, and other fields to company data.
- Centralizes enrichment logic for maintainability and extensibility.
- Easy to add new enrichment providers or change fallback order.
- EnrichmentService is OOP, modular, and independently testable.

### Extensibility
- New enrichment APIs can be added to the service with minimal changes to scrapers.
- Real API integration can replace stubbed logic as needed.

--- 

## AI-Powered Company Summarization (2025-07-15)

### Overview
- After enrichment, company data is passed to the `SummarizerService`.
- The service uses GPT-4 to generate a concise, business-focused summary from the company description.
- The summary is added as a `summary` field in the output.

### Integration Point
- Summarization is called in each enrichment pipeline after enrichment, before caching/storage.
- This ensures all downstream consumers (cache, DB, API, frontend) receive a summary if available.

### Value
- Provides a quick, digestible overview of each company for business users.
- Improves dashboards, lead cards, and analytics by surfacing key information at a glance.
- Modular and extensible for future enhancements (e.g., custom prompts, multi-language support).

### Error Handling
- API errors and rate limits are logged and handled gracefully.
- If summarization fails, the pipeline continues and the `summary` field is omitted.

### Extensibility
- Prompt and model can be customized in `SummarizerService`.
- Additional summarization providers or fallback logic can be added as needed.

--- 