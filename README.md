# 🚀 Flask DevOps Pipeline Demo

This project showcases a complete DevOps pipeline using a simple Flask application. It demonstrates how to automate build, test, and deployment workflows using Docker, GitHub Actions, and Kubernetes — all built entirely with free and open-source tools.

This project was created as part of the Team Better DevOps role assessment.

---

## 🔧 Tech Stack Used

- **Flask** – A lightweight Python web framework
- **Docker** – Containerizes the application
- **GitHub Actions** – Automates testing, image builds, and security scans
- **Trivy** – Scans Docker images for vulnerabilities
- **Kubernetes** – Deploys the application to a cluster
- **pytest** – Tests the Flask routes

---

## 📁 Project Structure

.
├── app.py # Flask application source code
├── test_app.py # Unit test for the root route
├── Dockerfile # Docker image definition
├── requirements.txt # Python package dependencies
├── .github/workflows/
│ └── ci-cd.yml # GitHub Actions CI/CD workflow
└── k8s/
├── deployment.yaml # Kubernetes deployment configuration
└── service.yaml # Kubernetes service definition

yaml
Copy
Edit

---

## ✅ CI/CD Pipeline Overview

Every time a commit is pushed to the `main` branch, GitHub Actions automatically runs the following steps:

1. **Run Tests**  
   Uses `pytest` to ensure the Flask app is functioning correctly.

2. **Build & Push Docker Image**  
   Builds a Docker image of the app and pushes it to DockerHub.

3. **Security Scan**  
   Uses Trivy to scan the Docker image for known vulnerabilities before deployment.

---

## 🐳 Docker Image

You can pull and run the Docker image directly from DockerHub:

- **Image**: [`vipul04/flask-devops-app`](https://hub.docker.com/r/vipul04/flask-devops-app)
- **Tag**: `latest`

### ▶️ Run it locally:

```bash
docker run -p 5000:5000 \
  -e ENVIRONMENT=production \
  -e APP_VERSION=1.0.0 \
  vipul04/flask-devops-app:latest
