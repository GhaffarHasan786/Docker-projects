# Docker Volume Practice

A simple practice project to understand and demonstrate **Docker Volumes** using a Python application.

## 📌 Project Overview

This project demonstrates how Docker Volumes can be used to **persist data** even when a Docker container is stopped or removed.

A simple Python program is used to save and read user data from a file. The file is connected to a Docker Volume so that the data remains available outside the container lifecycle.

## 🛠️ Technologies Used

* Python
* Docker
* Docker Volumes

## 📂 Project Structure

```text
Docker-volume/
│
├── main.py
├── user_name.txt
└── README.md
```

## 🐳 Docker Volume

Create a Docker volume:

```bash
docker volume create my_volume
```

Check available volumes:

```bash
docker volume ls
```

Inspect the volume:

```bash
docker volume inspect my_volume
```

## ▶️ Run the Project

Build the Docker image:

```bash
docker build -t python-volume-app .
```

Run the container with the Docker volume:

```bash
docker run -it -v my_volume:/app python-volume-app
```

The `-v` option mounts the Docker volume to the `/app` directory inside the container.

## 🎯 What I Practiced

* Creating Docker Volumes
* Listing Docker Volumes
* Inspecting Docker Volumes
* Mounting a Volume to a Container
* Persistent data storage
* Running a Python application with Docker Volumes

## 📚 Learning Objective

The main goal of this project is to understand how **Docker Volumes provide persistent storage** and how data can survive even after a container is removed.

---

**Practice Project — Docker & DevOps Learning**
