# 🌐 Dockerized Web Page

A simple and modern web page containerized using Docker. This project demonstrates how to package a web application into a Docker container and run it consistently across different environments.

---

## 🚀 Features

* Responsive web page
* HTML, CSS, and JavaScript in a single file
* Docker containerization
* Easy deployment
* Lightweight setup
* Beginner-friendly Docker project

---

## 📂 Project Structure

```text
project-folder/
│
├── index.html       # Main web page with HTML, CSS & JavaScript
├── Dockerfile       # Docker configuration
└── README.md
```

---

## 🐳 Dockerfile

The Dockerfile is used to create a lightweight container for serving the web page.

```dockerfile
FROM nginx:alpine

COPY index.html /usr/share/nginx/html/index.html

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
```

---

## ⚙️ Build Docker Image

Build the Docker image from the project directory:

```bash
docker build -t web-page-app .
```

---

## ▶️ Run Docker Container

Run the container and map port `8080` on the host to port `80` inside the container:

```bash
docker run -d -p 8080:80 --name web-container web-page-app
```

---

## 🌍 Access Application

Open your browser and visit:

```text
http://localhost:8080
```

Your web page should now be running inside a Docker container.

---

## 🛠 Technologies Used

* HTML5
* CSS3
* JavaScript
* Docker
* Nginx

---

## 📚 Learning Objectives

This project was created to practice:

* Docker fundamentals
* Containerization concepts
* Dockerfile creation
* Docker image building
* Container management
* Port mapping
* Running a web application inside a container
* Serving static web content using Nginx

---

## 👨‍💻 Author

**Ghaffar Hasan**

AI Automation | Python | n8n | Docker | Future DevOps Engineer
