# NutriSigno Skeleton

This repository provides a skeleton implementation for the **NutriSigno**
project.  It is not a full implementation; instead, it is intended
to illustrate the file structure and basic components required to
develop the application described in the specification.

## Structure

* **backend/** — FastAPI application with routers, models,
  repositories, and services.  Models are defined using SQLAlchemy,
  while Pydantic schemas describe request and response payloads.  The
  services layer includes stubs for interacting with an AI service
  (Agnos), building PDFs and images, caching, and filtering banned
  language.  A minimal Alembic environment is provided for
  migrations.
* **frontend/** — Streamlit application demonstrating login,
  questionnaire submission, and report display.  It uses a stubbed
  API client to communicate with the backend.
* **data/** — Sample data files including astrology profiles, plan
  templates, and substitution rules.  These serve as examples of
  the static resources referenced by the backend.
* **docs/** — This documentation and any future design notes or
  diagrams.

## Running the skeleton

1. Install dependencies:

   ```bash
   pip install fastapi uvicorn pydantic[dotenv] sqlalchemy streamlit reportlab pillow
   ```

2. Start the backend server:

   ```bash
   uvicorn backend.app:app --reload --host 0.0.0.0 --port 8000
   ```

3. In a separate terminal, start the frontend:

   ```bash
   streamlit run frontend/main.py
   ```

You can then visit `http://localhost:8501` to interact with the
Streamlit application.  Most endpoints return stubbed data and do
not persist state between sessions.  Use this skeleton as a starting
point to implement the full functionality described in your project
specification.