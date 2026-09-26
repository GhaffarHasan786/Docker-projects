# DevOps Dashboard

A modern **Flask-based DevOps Dashboard** designed for practicing Docker, Docker Compose, Nginx reverse proxy, container networking, and system monitoring.

The application provides a landing page, DevOps services section, and a dynamic server status page showing CPU, memory, disk usage, uptime, and system information.

## Features

* Flask web application
* Bootstrap-based modern UI
* Dynamic CPU, RAM, and Disk monitoring
* Server uptime monitoring
* Docker containerization
* Docker Compose setup
* Nginx reverse proxy
* Custom Docker bridge network
* Multi-container architecture

## Project Structure

```text
devops-dashboard/
│
├── app.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── nginx.conf
│
└── templates/
    ├── index.html
    └── status.html
```

## Architecture

```text
                    Browser
                       │
                       │ HTTP :80
                       ▼
              ┌─────────────────┐
              │     Nginx       │
              │ Reverse Proxy   │
              └────────┬────────┘
                       │
                       │ web-app:5000
                       ▼
              ┌─────────────────┐
              │  Flask Web App  │
              │    Container    │
              └────────┬────────┘
                       │
                       ▼
                    psutil
                       │
              ┌────────┼────────┐
              ▼        ▼        ▼
             CPU      RAM      Disk
```

## Docker Compose Network

```text
              devops-network
                    │
          ┌─────────┴─────────┐
          │                   │
          ▼                   ▼
   reverse-proxy          web-app
      Nginx                Flask
      :80                  :5000
```

Both containers communicate through the custom `devops-network`.

## Technologies

* Python
* Flask
* Bootstrap
* Docker
* Docker Compose
* Nginx
* psutil

## Run with Docker Compose

Build and start the containers:

```bash
docker compose up --build
```

Open the application:

```text
http://localhost
```

Stop the containers:

```bash
docker compose down
```

## Dashboard Pages

### Home

```text
/
```

Landing page with DevOps dashboard overview and services.

### Services

```text
/services
```

Displays DevOps-related services.

### Server Status

```text
/status
```

Displays dynamic system metrics including:

* CPU usage
* Memory usage
* Disk usage
* Application uptime
* Hostname
* Operating system
* Python version
* Storage information

## Monitoring API

The dashboard uses:

```text
/api/metrics
```

The frontend requests this endpoint every few seconds to update the server metrics dynamically.

## Purpose

This project was created as a **DevOps practice project** to understand:

* Dockerfile
* Docker containers
* Docker Compose
* Container networking
* Nginx reverse proxy
* Volume mounting
* Service dependencies
* Flask application deployment
* Basic server monitoring
