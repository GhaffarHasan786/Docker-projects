# 🐳 Docker Projects

A professional collection of **Docker and containerization practice projects** covering the core concepts required for modern DevOps workflows.

This repository contains hands-on implementations of Docker fundamentals, container management, persistent storage, networking, Docker Compose, Nginx reverse proxy, and multi-container application architecture.

The purpose of this repository is to build practical experience with Docker by implementing each concept through separate projects and exercises.

---

## 🚀 Repository Overview

This repository focuses on practical Docker concepts including:

* Docker fundamentals
* Dockerfile
* Docker images
* Docker containers
* Container lifecycle
* Port mapping
* Docker volumes
* Bind mounts
* Docker networking
* Docker Compose
* Multi-container applications
* Nginx reverse proxy
* Flask applications
* Containerized Python applications
* Application monitoring
* DevOps-oriented container architecture

---

# 📂 Repository Structure

```text
Docker-projects/
│
├── 01-dockerfile/
│   ├── Dockerfile
│   ├── index.html
│   └── README.md
│
├── 02-docker-volume/
│   ├── main.py
│   ├── user_name.txt
│   └── README.md
│
├── 03-bind-mount/
│   ├── application files
│   └── README.md
│
├── 04-docker-network/
│   ├── app.py
│   ├── Dockerfile
│   └── README.md
│
├── 05-docker-compose/
│   ├── app.py
│   ├── Dockerfile
│   ├── docker-compose.yml
│   └── README.md
│
├── 06-nginx-reverse-proxy/
│   ├── app.py
│   ├── Dockerfile
│   ├── nginx.conf
│   ├── docker-compose.yml
│   └── README.md
│
├── 07-python-app/
│   ├── Dockerfile
│   ├── requirements.txt
│   └── application files
│
└── README.md
```

> Folder names can be adjusted according to the actual projects added to the repository.

---

# 🧩 Docker Topics Practiced

## 1. Docker Fundamentals

Practice with the basic Docker workflow:

* Docker installation and setup
* Docker CLI
* Docker images
* Docker containers
* Container lifecycle
* Starting and stopping containers
* Removing containers
* Inspecting containers
* Viewing container logs
* Executing commands inside containers

Example commands:

```bash
docker images
docker ps
docker ps -a
docker run
docker stop
docker start
docker rm
docker logs
docker exec
docker inspect
```

---

## 2. Dockerfile

Dockerfiles are used to create custom application images.

Practice includes:

* Base images
* Working directories
* Copying application files
* Installing dependencies
* Exposing ports
* Container startup commands
* Building custom images

Example:

```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["python", "app.py"]
```

---

## 3. Docker Images

Image-related practice includes:

* Building images
* Naming images
* Tagging images
* Listing images
* Removing images
* Understanding image layers

Example:

```bash
docker build -t my-app .
```

```bash
docker images
```

---

# 💾 4. Docker Volumes

Docker volumes are used for persistent container data.

Practice includes:

* Creating Docker volumes
* Attaching volumes to containers
* Storing application data
* Persisting data after container removal
* Inspecting volumes

Example:

```bash
docker volume create app-data
```

```bash
docker run -v app-data:/app/data my-app
```

### Concept

```text
Container
    │
    ▼
Docker Volume
    │
    ▼
Persistent Data
```

---

# 📁 5. Bind Mounts

Bind mounts allow a directory or file from the host machine to be mounted inside a container.

Practice includes:

* Host-to-container file sharing
* Development workflows
* Live application changes
* Mounting configuration files

Example:

```bash
docker run -v ./app:/app my-app
```

### Concept

```text
Host Machine
     │
     │ Bind Mount
     ▼
Container
     │
     ▼
Application
```

---

# 🌐 6. Docker Networking

Docker networking practice focuses on communication between containers.

Topics include:

* Docker bridge network
* Creating custom networks
* Connecting containers
* Container-to-container communication
* Service name based communication

Example:

```bash
docker network create devops-network
```

Containers can communicate using their service/container names.

### Architecture

```text
              devops-network
                    │
          ┌─────────┴─────────┐
          │                   │
       Flask App           Database
          │                   │
          └─────── Network ───┘
```

---

# ⚙️ 7. Docker Compose

Docker Compose is used to define and manage multi-container applications.

Practice includes:

* `docker-compose.yml`
* Services
* Builds
* Container names
* Ports
* Volumes
* Networks
* Environment variables
* `depends_on`
* Multi-container applications

Example structure:

```yaml
version: "3.8"

services:

  web-app:
    build: .
    container_name: web-app
    networks:
      - app-network

  database:
    image: postgres:16
    container_name: database
    networks:
      - app-network

networks:
  app-network:
    driver: bridge
```

Run the application:

```bash
docker compose up --build
```

Stop:

```bash
docker compose down
```

---

# 🔀 8. Nginx Reverse Proxy

Nginx is used as a reverse proxy in multi-container application architecture.

Practice includes:

* Nginx container
* Reverse proxy configuration
* Flask application behind Nginx
* Container networking
* Port forwarding
* Service-to-service communication

### Architecture

```text
                    Browser
                       │
                       │ HTTP :80
                       ▼
              ┌─────────────────┐
              │      Nginx      │
              │ Reverse Proxy   │
              └────────┬────────┘
                       │
                       │ :5000
                       ▼
              ┌─────────────────┐
              │   Flask App     │
              │    Container    │
              └─────────────────┘
```

This project demonstrates how an application can be placed behind a reverse proxy instead of exposing the application container directly.

---

# 🐍 9. Python Application Containerization

Python applications are also containerized as part of the practice.

Topics include:

* Python base images
* `requirements.txt`
* Dependency installation
* Flask applications
* CLI applications
* Application startup commands
* Containerized Python environments

Example:

```text
Python Application
        │
        ▼
   requirements.txt
        │
        ▼
     Dockerfile
        │
        ▼
   Docker Image
        │
        ▼
   Docker Container
```

---

# 🏗️ Multi-Container Architecture

The projects gradually move from single-container applications toward multi-container DevOps architectures.

Example:

```text
                         Internet
                            │
                            ▼
                    ┌───────────────┐
                    │     Nginx     │
                    │ Reverse Proxy │
                    └───────┬───────┘
                            │
                    Docker Network
                            │
              ┌─────────────┴─────────────┐
              │                           │
              ▼                           ▼
       ┌─────────────┐             ┌─────────────┐
       │ Flask App   │             │  Database   │
       │  Container  │             │  Container  │
       └──────┬──────┘             └──────┬──────┘
              │                           │
              └─────────────┬─────────────┘
                            │
                       Docker Storage
                            │
                            ▼
                         Volume
```

---

# 🛠️ Technologies

| Technology     | Purpose                       |
| -------------- | ----------------------------- |
| Docker         | Containerization              |
| Dockerfile     | Image creation                |
| Docker Compose | Multi-container orchestration |
| Nginx          | Reverse proxy                 |
| Python         | Application development       |
| Flask          | Web applications              |
| Bootstrap      | Frontend UI                   |
| Docker Network | Container communication       |
| Docker Volume  | Persistent storage            |
| Bind Mount     | Host-container file sharing   |
| Linux          | Container/server environment  |

---

# 📚 Learning Progression

The repository follows a practical learning progression:

```text
Docker Basics
      │
      ▼
Docker Images
      │
      ▼
Dockerfile
      │
      ▼
Containers
      │
      ▼
Volumes
      │
      ▼
Bind Mounts
      │
      ▼
Docker Networking
      │
      ▼
Docker Compose
      │
      ▼
Nginx Reverse Proxy
      │
      ▼
Multi-Container Applications
      │
      ▼
DevOps Container Architecture
```

---

# 🎯 Repository Goals

The main goals of this repository are to gain practical experience with:

* Containerization
* Application deployment
* Docker CLI
* Image management
* Persistent storage
* Container networking
* Multi-container architecture
* Reverse proxy configuration
* Infrastructure-oriented application deployment
* Docker-based DevOps workflows

---

# ▶️ General Docker Workflow

Most projects follow this workflow:

```bash
# Build image
docker build -t my-app .

# Run container
docker run -p 5000:5000 my-app

# Check running containers
docker ps

# View logs
docker logs <container>

# Execute command inside container
docker exec -it <container> bash

# Stop container
docker stop <container>

# Remove container
docker rm <container>
```

For Compose-based projects:

```bash
docker compose up --build
```

```bash
docker compose down
```

---

# 📈 DevOps Focus

This repository is part of my practical **DevOps learning journey**, with a focus on understanding how applications are packaged, deployed, connected, and managed using container technologies.

The projects are intentionally organized as separate hands-on exercises so that each Docker concept can be understood and practiced independently.

---

## 👨‍💻 Author

**Ghaffar Hasan**

DevOps Engineering | Docker | Python | Flask | Automation

---

## 📌 Note

This repository is continuously evolving as new Docker and DevOps concepts are learned and implemented through practical projects.
