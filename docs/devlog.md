# Project Titan - Developer Log

## Sprint 1

### Ticket 1 - Project Initialization

#### Objective
Set up the AuthCore project foundation.

#### Today I Learned
- How to initialize a Git repository.
- How to create and activate a Python virtual environment.
- How to install project dependencies using pip.

#### Problems I Faced
- `pip` was not recognized in PowerShell.

#### How I Solved It
- Activated the virtual environment.
- Used `python -m pip install` instead of `pip install`.

---

### Ticket 2 - FastAPI Setup

#### Objective
Create and run the first FastAPI application.

#### Today I Learned
- How to create a FastAPI application.
- How to create my first API endpoint.
- How to run the server using Uvicorn.
- How to access the automatic API documentation at `/docs`.

#### Problems I Faced
- The browser requested `favicon.ico`, which returned a 404 error.

#### How I Solved It
- Learned that this is normal because we haven't added a favicon yet.