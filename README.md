# docker-compose-project: Python + Node.js + PostgresSQL

**Project Overview**
This project demonstrates how to **containerize a multi-service application** using **Docker and Docker Compose**.

The application consists of:
**.** Python (Flask) backend
**.** Node.js frontend
**.** PostgreSQL database
All services run in isolated containers and communicate with each other using Docker Compose networking.

**Project Structure**

docker-compose-project/

├── docker-compose.yml

├── python-app/

│   ├── Dockerfile

│   ├── app.py

│   └── requirements.txt

└── node-app/

    ├── Dockerfile
    
    ├── index.js
    
    └── package.json

**Technologies Used**
- Docker
- Docker Compose (v2)
- Python (Flask)
- Node.js (Express)
- PostgreSQL
- AWS EC2 (for deployment)
- MobaXterm (SSH access)

**Key DevOps Concepts Learned**
- Containerizing applications using Docker
- Multi-container orchestration using Docker Compose
- Docker networking (service-name-based communication)
- Environment variables for configuration
- Port mapping and container isolation
- Deploying containers on an EC2 instance

**Docker Compose Configuration**
The application is orchestrated using Docker Compose with three services:
**.** db – PostgreSQL database (official image)
**.** python – Flask backend (custom Dockerfile)
**.** node – Node.js frontend (custom Dockerfile)

**Docker Compose automatically:**
**.** Creates a private network
**.** Assigns DNS names to services
**.** Manages startup order using **depends_on**

**How to Run the Project**

**Step 1:**
**Prerequisites**
Make sure the following are installed:
**.** Docker
**.** Docker compose plugin
On AWS EC2:
**.** Open ports 3000 and 5000 in Security Group inbound rules

**Step 2:**
**Clone the repository**
**.** git clone https://github.com/<your-username>/<repo-name>.git
cd docker-compose-project

**Step 3:**
**Build and Start the container**
**.** docker compose up --build -d

**Step 4:**
**Verify running containers**
**.** docker compose ps

**Step 5:**
**Access the Application**
If running locally:
- Node frontend: http://localhost:3000
- Python backend: http://localhost:5000

If running on EC2:
- Node frontend: http://<EC2_PUBLIC_IP>:3000
- Python backend: http://<EC2_PUBLIC_IP>:5000







