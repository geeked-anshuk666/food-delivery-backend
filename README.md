# Food Delivery Backend Microservices

This project implements the backend for a food delivery application using a microservices architecture. It consists of three distinct services: User, Restaurant, and Delivery Agent, designed for scalability and maintainability.

## Services and Features

### 1. User Service
-   **Retrieve Restaurants:** Allows users to retrieve a list of all restaurants available online.
-   **Place Order:** Enables users to place orders from available restaurants.
-   **Leave Ratings:** Provides functionality for users to leave ratings for their orders and the delivery agents.

### 2. Restaurant Service
-   **Manage Menu & Availability:** Restaurants can update their menu items, pricing, and availability status (online/offline).
-   **Order Processing:** Restaurants can accept or reject incoming orders. If an order is accepted, it proceeds to processing.
-   **Auto-Assign Delivery Agent:** Automatically assigns an available and free delivery agent to an accepted order.

### 3. Delivery Agent Service
-   **Update Delivery Status:** Delivery agents can update the status of orders (e.g., picked up, in transit, delivered).

## Tech Stack

The following technologies are used in this project:

-   **Backend Framework:** FastAPI (Python)
-   **Database:** PostgreSQL
-   **ORM:** SQLAlchemy
-   **Containerization:** Docker
-   **Deployment:** Render (using Docker images)
-   **Inter-service Communication:** HTTP (using `requests` library)

## Database Schema

Each microservice manages its own set of data, with relationships defined where necessary. The database schemas are defined using SQLAlchemy ORM in the `models.py` files within each service's `app` directory. A single shared PostgreSQL database instance is used on Render to adhere to free tier limitations, with each service's tables residing within it.

## Code Structure and Design Principles

-   **Microservices Architecture:** Clear separation of concerns, with each service handling a specific domain.
-   **Modularity & Extensibility:** Code is organized into routers, CRUD operations, schemas, and database models for maintainability and future expansion.
-   **Shared Module:** A `shared` directory contains common utilities like `ServiceClient` for inter-service communication and `config` for shared environment variables, promoting code reuse and consistency.
-   **API-First Design:** All services expose RESTful APIs, documented with Swagger UI.
-   **Dockerization:** Each service is containerized, ensuring consistent environments from development to production.

## Local Development

### Prerequisites
To run this project locally, you will need:
-   [Docker](https://www.docker.com/get-started) and [Docker Compose](https://docs.docker.com/compose/install/) installed.
-   [Git](https://git-scm.com/downloads)

### Steps to Run Locally
1.  **Clone the repository:**
    ```bash
    git clone <your-github-repo-link>
    cd food-delivery-backend
    ```
2.  **Build and start all services using Docker Compose:**
    This command will build the Docker images for each service and the PostgreSQL database, then start all containers.
    ```bash
    docker-compose build
    docker-compose up
    ```
3.  **Access Local API Documentation (Swagger UI):**
    Once the services are running, you can access their API documentation in your web browser:
    -   User Service: `http://localhost:8001/docs`
    -   Restaurant Service: `http://localhost:8002/docs`
    -   Delivery Service: `http://localhost:8003/docs`

## Deployment Instructions (Free Hosting on Render with Docker)

The application is configured for continuous deployment on Render using a `render.yaml` Blueprint file, which defines all services and a shared PostgreSQL database.

### Steps to Deploy
1.  **Create a free account on [Render](https://render.com/).**
2.  **Push your project to a GitHub repository.** Ensure all necessary files, including `render.yaml` and the Dockerfiles for each service, are pushed to your main branch.
3.  **Clean up any old free tier databases/services on Render:** Before deploying, verify that you do not have any other active free PostgreSQL databases or Blueprint services in your Render account. Render's free tier allows only one free database per account.
4.  **Connect your GitHub repository to Render:**
    -   Navigate to the Render Dashboard.
    -   Click the "New" button and select "Blueprint".
    -   Connect your GitHub account and select this repository.
    -   Render will automatically detect the `render.yaml` file, build the Docker image for each service, and deploy them.

### Live Endpoints
Once successfully deployed, your services will be available at the following URLs:
-   **User Service:** `https://food-delivery-user-service.onrender.com`
-   **Restaurant Service:** `https://food-delivery-restaurant-service.onrender.com`
-   **Delivery Service:** `https://food-delivery-delivery-service.onrender.com`

### Access Deployed API Documentation (Swagger UI):
You can access the interactive API documentation for each deployed service here:
-   User Service: `[https://food-delivery-user-service-nxxt.onrender.com/docs]`
-   Restaurant Service: `[https://food-delivery-restaurant-service-reba.onrender.com/docs]`
-   Delivery Service: `[https://food-delivery-delivery-service-br1b.onrender.com/docs]`

## Postman Collection

A Postman collection is provided to facilitate easy testing and interaction with the API endpoints.

**To use the Postman Collection:**
1.  Open Postman.
2.  Click "Import" and select the provided Postman collection file (e.g., `Food_Delivery_API.postman_collection.json`).
3.  Import the accompanying Postman environment file (e.g., `Food_Delivery_API_Environment.postman_environment.json`).
4.  Select the "Food Delivery API Environment" from the environment dropdown in Postman. You can then switch the `USER_SERVICE_URL`, `RESTAURANT_SERVICE_URL`, and `DELIVERY_SERVICE_URL` variables between local (`http://localhost:XXXX`) and deployed (`https://food-delivery-XXXX.onrender.com`) URLs as needed.
