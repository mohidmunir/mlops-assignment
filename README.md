
# MLOps Assignment 2 - Full Stack Microservices Application on Minikube

## Project Overview

This project is developed for **MLOps Assignment 2**, showcasing the end-to-end deployment of a full-stack microservices application using:

- **Frontend**: React (Login, Signup, Forgot Password)
- **Backend**: Flask (API & Authentication)
- **Database**: PostgreSQL
- **Authentication**: JWT (JSON Web Tokens)
- **Containerization**: Docker
- **Orchestration**: Kubernetes (Minikube)

## Directory Structure

```
mlops-assignment/
├── frontend/                         # React frontend
│   ├── public/
│   └── src/
│       ├── components/
│       │   ├── Login.js
│       │   ├── Signup.js
│       │   └── ForgotPassword.js
│       ├── App.js
│       └── index.js
│   ├── package.json
│   └── .env                          # Frontend environment variables

├── backend/                          # Flask backend
│   ├── app/
│   │   ├── __init__.py
│   │   ├── routes.py
│   │   ├── auth.py
│   │   ├── models.py
│   │   └── utils.py
│   ├── requirements.txt
│   ├── config.py
│   ├── run.py                        # Entry point
│   └── .env                          # Backend environment variables

├── database/
│   └── init.sql                      # SQL to create tables like "users"

├── docker/
│   ├── Dockerfile.frontend
│   ├── Dockerfile.backend
│   └── Dockerfile.database           # Optional for completeness

├── k8s/
│   ├── frontend-deployment.yaml
│   ├── frontend-service.yaml
│   ├── backend-deployment.yaml
│   ├── backend-service.yaml
│   ├── postgres-deployment.yaml
│   ├── postgres-service.yaml
│   └── secrets.yaml                  # DB password, JWT secret etc.

├── docker-compose.yml                # Local testing with all services
└── README.md                         # Instructions for running the project
```

## Steps to Run the Application

### 1. Clone the Repository

Clone the repository to your local machine:

```bash
git clone https://github.com/mohidmunir/mlops-assignment.git
cd mlops-assignment
```

### 2. Docker Setup

Make sure Docker Desktop is running.

- **Build Docker Images**:
  
  In your terminal, run the following command to build the Docker images for frontend, backend, and database:

  ```bash
  docker-compose build
  ```

- **Run Docker Containers**:

  After building the images, start the containers with:

  ```bash
  docker-compose up
  ```

  This will start the frontend, backend, and database containers. 

- **Access the Application**:

  - **Frontend**: Open [http://localhost:3000](http://localhost:3000) in your browser to access the frontend.
  - **Backend**: The backend API will be running at [http://localhost:5000](http://localhost:5000).

### 3. Kubernetes Deployment on Minikube

Make sure Minikube is running:

```bash
minikube start
```

To deploy the application on Minikube using Kubernetes, follow these steps:

- **Build Docker Images Inside Minikube**:

  Build the Docker images for the frontend and backend inside Minikube’s Docker daemon:

  ```bash
  eval $(minikube docker-env)
  docker-compose build
  ```

- **Deploy to Kubernetes**:

  Apply the Kubernetes configuration files to deploy the application on Minikube:

  ```bash
  kubectl apply -f k8s/
  ```

- **Check Deployment**:

  Verify the deployment and services by running:

  ```bash
  kubectl get pods
  kubectl get svc
  ```

  The services will be available via Minikube’s IP address, which can be found with:

  ```bash
  minikube ip
  ```

  You can access the frontend by visiting `[Minikube_IP]:3000` in your browser.

### 4. Accessing Logs

To check the logs for any service, use the following:

```bash
kubectl logs <pod_name>
```

### 5. Troubleshooting

- **Database Connection Issues**:

  Ensure that the PostgreSQL database is correctly initialized and accessible from both the backend and frontend containers.

- **Service Not Found**:

  Check the `k8s/<service>-service.yaml` files to ensure that the service is correctly exposed.

- **API Issues**:

  Ensure the backend API is running by checking the logs for the backend service using:

  ```bash
  kubectl logs <backend_pod_name>
  ```

## Features Implemented

### Authentication

- **Signup**: Users can create an account by providing an email and password. The password is hashed before being stored in the database using bcrypt.
  
- **Login**: Users can log in by providing their credentials, which are checked against the stored hashed password in the database. If the credentials are correct, a JWT token is generated.

- **Forgot Password**: Placeholder feature for future development.

### Frontend

- **React Components**: The frontend is built with React, containing components for Login, Signup, and Forgot Password.
  
- **Axios for API Calls**: Axios is used to make HTTP requests to the backend API for user authentication.

### Backend

- **Flask API**: The backend is built with Flask, providing routes for user authentication (signup and login).
  
- **PostgreSQL Database**: The application uses a PostgreSQL database to store user credentials.

### Kubernetes and Docker

- **Docker**: Docker is used to containerize the frontend, backend, and database services for easy deployment.
  
- **Kubernetes**: Kubernetes is used to deploy the application on Minikube, with services and pods for managing the backend, frontend, and database containers.

---

## Conclusion

This project demonstrates the use of Docker and Kubernetes for building, containerizing, and deploying a full-stack microservices application. The project uses Flask for the backend, React for the frontend, PostgreSQL for data storage, and JWT for secure authentication. With Kubernetes and Docker, the application is highly scalable and can handle increased traffic effectively.
