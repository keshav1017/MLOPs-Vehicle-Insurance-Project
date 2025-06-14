# 🚗 Vehicle Insurance ML MLOps Project

Welcome to the **Vehicle Insurance ML MLOps Project**!  
This repository showcases a robust, production-ready machine learning pipeline for vehicle insurance prediction, featuring the latest in MLOps best practices, cloud integration, and automated deployment.  
Impress recruiters, collaborators, and visitors with a modern, scalable, and cloud-native ML system!

---

## 🌟 Key Features

- **End-to-End Machine Learning Pipeline**: From data ingestion to model deployment, every stage is automated and modular.
- **Cloud-Native Architecture**: Integrated with MongoDB Atlas for data storage and AWS (S3, ECR, EC2) for scalable model management and deployment.
- **CI/CD Automation**: Seamless build, test, and deployment using GitHub Actions and Docker, ensuring rapid and reliable releases.
- **Self-Hosted Runner on EC2**: Production-grade deployment using a secure, scalable AWS EC2 instance.
- **Interactive Web App**: User-friendly FastAPI web interface for predictions and model retraining.
- **Best Practices**: Modular code, logging, exception handling, configuration management, and secure secret handling.

---

## 🛠️ Tools, Technologies & Services

| Category            | Stack / Service                                 |
|---------------------|-------------------------------------------------|
| **Language**        | Python 3.12 / 3.13                              |
| **Frameworks**      | FastAPI, Jinja2                                 |
| **Data Storage**    | MongoDB Atlas                                   |
| **Cloud**           | AWS S3, ECR, EC2, IAM                           |
| **MLOps**           | Docker, GitHub Actions, Self-hosted Runner      |
| **CI/CD**           | GitHub Actions, AWS ECR, EC2                    |
| **Visualization**   | Jupyter Notebook, EDA, Feature Engineering      |
| **Logging**         | Custom logger module                            |
| **Exception Handling** | Custom exception module                      |

---

## 🚀 Project Architecture

```mermaid
graph TD
    A[User] -->|Web UI| B(FastAPI App)
    B --> C[Prediction Pipeline]
    C --> D[Model Registry (S3)]
    C --> E[MongoDB Atlas]
    D --> F[EC2 Deployment]
    B -->|/train| C
    G[GitHub Actions] -->|CI/CD| F
    H[Docker] --> G
```

---

## 📦 Project Structure

```
├── src/
│   ├── constants/
│   ├── configuration/
│   ├── pipline/
│   ├── aws_storage/
│   ├── entity/
│   ├── templates/
│   ├── static/
│   └── app.py
├── notebook/
├── .github/workflows/
│   └── aws.yaml
├── Dockerfile
├── requirements.txt
├── setup.py
├── pyproject.toml
└── README.md
```

---

## 🧑‍💻 How It Works

### 1. **Project Setup**
- Generate project template with `template.py`.
- Manage local packages with `setup.py` and `pyproject.toml`.
- Create a virtual environment and install all dependencies.

### 2. **Data Management**
- Use **MongoDB Atlas** for secure, scalable cloud data storage.
- Ingest, validate, and transform data using modular pipeline components.
- Push and pull data using custom utility scripts and configuration files.

### 3. **Model Lifecycle**
- Train models locally or via the web interface.
- Store and manage models in AWS S3.
- Evaluate and push new models automatically when performance improves.

### 4. **Web Application**
- FastAPI serves a modern, interactive UI for predictions and retraining.
- Jinja2 templates and static assets for a polished user experience.

### 5. **CI/CD Pipeline**
- **GitHub Actions** automates build, test, and deployment:
  - Build Docker images and push to AWS ECR.
  - Deploy containers to an EC2 instance via a self-hosted runner.
  - Securely manage secrets and environment variables.
- **Live deployment**: App is always up-to-date with the latest code and model.

### 6. **Cloud Integration**
- **AWS IAM** for secure access management.
- **AWS S3** for model registry.
- **AWS ECR** for container image storage.
- **AWS EC2** for scalable, production-grade hosting.

---

## 📝 Notebooks & Experimentation

- Interactive Jupyter notebooks for EDA, feature engineering, and data exploration.
- Demonstrations of data ingestion, validation, and transformation.
- Push datasets directly to MongoDB from notebooks.

---

## 🔒 Security & Best Practices

- All secrets managed via GitHub Secrets.
- `.gitignore` includes sensitive directories.
- Logging and exception handling modules for robust monitoring.

---

## 🏁 Quickstart

1. **Clone the repository**
2. **Set up your environment**
   ```bash
   conda create -n vehicle python=3.12 -y
   conda activate vehicle
   pip install -r requirements.txt
   ```
3. **Configure MongoDB and AWS**
   - Set `MONGODB_URL`, `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`, and `AWS_DEFAULT_REGION` as environment variables.
4. **Run the app**
   ```bash
   python src/app.py
   ```
5. **Access the web UI**
   - Go to `http://localhost:5000` (or your EC2 public IP and port).

---

## 🌍 Deployment Workflow

1. **Push code to GitHub → CI/CD pipeline triggers**
2. **Docker image built and pushed to AWS ECR**
3. **EC2 self-hosted runner pulls and runs the latest image**
4. **App live at your EC2 public IP and port**

---

## 📈 Model Training & Retraining

- Trigger model retraining via the `/train` route in the web UI.
- Automatic model evaluation and registry update in AWS S3.

---

## 💡 Why This Project Stands Out

- **Truly production-ready**: Not just a notebook—this is a full-stack MLOps pipeline.
- **Cloud-first**: Uses industry-standard cloud services for scalability and reliability.
- **Automated everything**: From data to deployment, all steps are automated.
- **Modern stack**: FastAPI, Docker, AWS, MongoDB, and CI/CD.
- **Impressive for recruiters**: Demonstrates real-world, end-to-end ML engineering.

---

## 🤝 Connect

**Impress recruiters and collaborators by showcasing your expertise in MLOps, cloud, and modern ML engineering!**

---

> _“This project is a one-stop solution for deploying, managing, and scaling machine learning models in production using modern DevOps and MLOps practices.”_

---

**Ready to take your ML projects to the next level? Star ⭐ this repo and get started!**

[1] https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/74911406/1e5ebb94-6bc7-4e69-9206-e8eefb72f596/paste.txt