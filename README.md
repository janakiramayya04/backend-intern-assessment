# Backend Developer Assessment

A Scalable REST API built with **FastAPI**, **PostgreSQL**, and **Docker**, featuring JWT Authentication and Role-Based Access Control (RBAC).

## Features
* **Authentication:** User registration & login (JWT).
* **RBAC:** Admin vs. User roles. Users manage their own items; Admins manage all.
* **CRUD Operations:** Create, Read, Update, and Delete items.
* **Async Database:** High-performance database access using `asyncpg` + `SQLAlchemy`.
* **Frontend:** A lightweight UI using Vanilla JS & Bootstrap.

## Tech Stack
* **Backend:** Python 3.10, FastAPI
* **Database:** PostgreSQL 15
* **Infrastructure:** Docker & Docker Compose

## Getting Started

### Prerequisites
* Docker & Docker Compose installed on your machine.

### Installation & Running
1.  **Clone the repository:**
    ```bash
    git clone <your-repo-url>
    cd <your-repo-folder>
    ```

2.  **Start the Application:**
    ```bash
    docker-compose up --build
    ```

3.  **Access the App:**
    * **Frontend UI:** Open `frontend/src/index.html` in your browser.
    * **API Docs (Swagger):** Visit [http://localhost:8000/docs](http://localhost:8000/docs).

## Testing the API
You can register a new user via the UI or Swagger.
* **Admin Role:** To create an admin, register with `role: "admin"` in the JSON body (or modify the UI dropdown).

