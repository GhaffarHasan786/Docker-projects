# Docker Networking Practice

A simple Flask-based practice project created to understand and practice **Docker Networking** concepts and commands.

## 📌 Project Overview

This project uses a simple Python Flask application to demonstrate the basic Docker network types:

* Bridge Network
* Host Network
* None Network

The main purpose of this project is to practice Docker networking commands and understand how containers handle network connectivity.

## 🛠️ Technologies Used

* Python
* Flask
* Docker
* Docker Networking

## 📂 Project Structure

```text
Docker-networking/
│
├── app.py
├── Dockerfile
├── requirements.txt
└── README.md
```

## 🐳 Docker Network Commands

### Create a Network

```bash
docker network create my_network
```

### List Networks

```bash
docker network ls
```

### Inspect a Network

```bash
docker network inspect my_network
```

### Run Container with Bridge Network

```bash
docker run -d --name flask-app --network my_network -p 5000:5000 flask-network
```

### Host Network

```bash
docker run -d --network host flask-network
```

### None Network

```bash
docker run -d --network none flask-network
```

### Remove a Network

```bash
docker network rm my_network
```

## 🎯 What I Practiced

* Creating Docker networks
* Listing Docker networks
* Inspecting networks
* Connecting containers to networks
* Bridge networking
* Host networking
* None networking
* Running a Flask application inside a Docker container

## 📚 Learning Objective

The main goal of this project is to understand the basics of **Docker Networking** and how Docker containers communicate through different network modes.

---

**Practice Project — Docker & DevOps Learning**
