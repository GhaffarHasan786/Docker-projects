# 🎙️ Python Voice Assistant — Dockerized

A simple **Python-based Voice Assistant** containerized with Docker as a hands-on DevOps practice project.

The assistant can listen to voice commands, convert speech to text, respond using text-to-speech, open websites, perform Google searches, and provide the current date and time.

This project focuses on learning how to **Dockerize a Python application**, manage dependencies, build Docker images, and run applications inside containers.

---

## 🚀 Features

* 🎤 Speech recognition using microphone input
* 🔊 Text-to-speech responses
* 🌐 Open YouTube, Google, Facebook and Instagram
* 🔎 Perform Google searches using voice commands
* 🕐 Get the current time
* 📅 Get the current date
* 🛑 Stop the assistant using voice commands
* 🐳 Dockerized Python application
* 📦 Dependency management with `requirements.txt`

---

## 🛠️ Technologies Used

* **Python 3**
* **SpeechRecognition**
* **PyAudio**
* **pyttsx3**
* **Docker**
* **Linux-based Docker container**

---

## 📁 Project Structure

```text
voice-assistant/
│
├── app.py
├── requirements.txt
├── Dockerfile
├── .dockerignore
└── README.md
```

### File Description

| File               | Description                                              |
| ------------------ | -------------------------------------------------------- |
| `app.py`           | Main Python voice assistant application                  |
| `requirements.txt` | Python dependencies required by the application          |
| `Dockerfile`       | Instructions for building the Docker image               |
| `.dockerignore`    | Files and folders excluded from the Docker build context |
| `README.md`        | Project documentation                                    |

---

## 📦 Python Dependencies

The project uses the following external Python packages:

```text
SpeechRecognition==3.14.3
pyttsx3==2.99
PyAudio==0.2.14
```

Python standard-library modules such as `os`, `datetime`, and `webbrowser` do not need to be added to `requirements.txt`.

---

## 🐳 Dockerfile

The Dockerfile uses a lightweight Python image and installs the required system dependencies for audio processing and text-to-speech.

```dockerfile
FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN apt-get update && apt-get install -y \
    portaudio19-dev \
    libasound2-dev \
    espeak \
    espeak-ng \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .

CMD ["python", "app.py"]
```

---

## ⚙️ Run the Project Locally

First, clone the repository:

```bash
git clone <your-repository-url>
cd voice-assistant
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python app.py
```

---

# 🐳 Docker Setup

## 1. Build the Docker Image

Run the following command from the project directory:

```bash
docker build -t voice-assistant .
```

Check the created image:

```bash
docker images
```

---

## 2. Run the Container

```bash
docker run --rm -it voice-assistant
```

### Command Explanation

```text
docker run
```

Creates and starts a container.

```text
--rm
```

Automatically removes the container after it stops.

```text
-it
```

Runs the container interactively with a terminal.

```text
voice-assistant
```

The name of the Docker image.

---

## 🧪 Useful Docker Commands

### List running containers

```bash
docker ps
```

### List all containers

```bash
docker ps -a
```

### List Docker images

```bash
docker images
```

### Stop a container

```bash
docker stop <container-id>
```

### Remove a container

```bash
docker rm <container-id>
```

### Remove an image

```bash
docker rmi voice-assistant
```

### View container logs

```bash
docker logs <container-id>
```

---

# 🎤 Audio & Microphone Considerations

This application uses:

```python
sr.Microphone()
```

for microphone input.

Because Docker containers are isolated from the host operating system, microphone and audio devices are **not automatically available inside the container**.

Additional audio-device configuration may therefore be required depending on the host operating system and Docker environment.

The application also uses:

```python
pyttsx3
```

for text-to-speech, which requires an appropriate speech engine inside the container.

---

# ⚠️ Windows-Specific Commands

The original application contains Windows-specific commands such as:

```python
os.system('notepad.exe')
os.system('calc.exe')
```

These commands work on Windows but are not available inside a standard Linux-based Docker container.

For Docker execution, these commands should either be removed or replaced with Linux-compatible alternatives.

For example:

```python
elif 'notepad' in command:
    speak("Notepad is not available inside the Docker container.")
```

---

# 🏗️ Docker Architecture

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
              Docker Build Process
                      │
                      ▼
               Docker Image
              voice-assistant
                      │
                      ▼
                Docker Run
                      │
                      ▼
                 Container
                      │
                      ▼
             Python Voice Assistant
```

---

# 🎯 DevOps Concepts Practiced

This project was created as a practical introduction to containerization and covers several important DevOps concepts:

* Dockerfile creation
* Docker image building
* Container execution
* Python dependency management
* `requirements.txt`
* Docker build context
* `.dockerignore`
* Container isolation
* Environment configuration
* Linux system dependencies
* Docker troubleshooting
* Application containerization

---

# 🔄 Development Workflow

```text
Write Python Application
        ↓
Create requirements.txt
        ↓
Create Dockerfile
        ↓
Create .dockerignore
        ↓
Build Docker Image
        ↓
Run Container
        ↓
Test Application
        ↓
Debug / Improve
        ↓
Rebuild Image
```

---

# 🧠 What I Learned

Through this project, I practiced how to take an existing Python application and convert it into a Dockerized application.

Key learning areas include:

* How Docker packages applications
* How dependencies are installed inside containers
* How Docker images are created
* How containers are started and stopped
* Why system-level dependencies matter
* How host resources such as audio devices interact with containers
* The difference between an application environment and the host environment

---

# 🔮 Future Improvements

Possible future improvements include:

* Add Docker Compose
* Improve microphone/audio support
* Add environment variables
* Add logging
* Add better error handling
* Add a web interface
* Add AI/LLM integration
* Add API-based commands
* Add CI/CD with GitHub Actions
* Deploy the application to a cloud environment

---

## 👨‍💻 Project Purpose

This project is part of my **DevOps learning and hands-on practice**, where I am learning how to containerize real-world applications using Docker and understand the workflow from application development to container deployment.

---

## 📄 License

This project is created for educational and learning purposes.
