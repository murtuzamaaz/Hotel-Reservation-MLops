# 🏨 Hotel Reservation Cancellation Prediction — End-to-End MLOps Project

## 🚀 Overview
This project focuses on predicting whether a hotel reservation will be canceled — a classic **binary classification problem** — but with a full-fledged **MLOps workflow** behind it.  
The main goal wasn’t just to build a machine learning model, but to implement a **production-grade, automated CI/CD pipeline** for reproducible, scalable, and reliable ML delivery.

---

## 🎯 Objectives
- Build an **end-to-end ML system** from data ingestion to deployment.  
- Automate the entire ML workflow using **Jenkins CI/CD**.  
- Ensure **reproducibility** and **traceability** using MLflow.  
- Containerize and deploy the model on **Google Cloud Run**.  
- Achieve strong performance metrics on hotel reservation data.

---

## ⚙️ MLOps Stack

| Component | Tool/Service | Purpose |
|------------|--------------|----------|
| **Version Control** | Git + GitHub | Source code management |
| **Automation** | Jenkins | Orchestrates CI/CD pipeline |
| **Containerization** | Docker | Packages application and dependencies |
| **Experiment Tracking** | MLflow | Logs parameters, metrics, and artifacts |
| **Cloud Platform** | Google Cloud Platform (GCP) | Storage, container registry, and deployment |
| **Deployment** | Google Cloud Run | Scalable, serverless model hosting |

---

## 🧠 ML Workflow

### 1️⃣ Data Ingestion
- Source: Google Cloud Storage  
- Loads raw hotel reservation data  
- Performs sanity checks and data validation  

### 2️⃣ Feature Engineering & Preprocessing
- Custom transformations and encoding (Label Encoding, One-Hot Encoding)  
- Handling of missing and categorical values  
- Feature scaling for numerical columns  

### 3️⃣ Model Training
- Automated hyperparameter tuning  
- Training and validation split  
- Model selection and evaluation (Accuracy, F1-Score)  

### 4️⃣ Experiment Tracking (MLflow)
- Logs all model metrics, parameters, and artifacts  
- Enables complete experiment reproducibility  

### 5️⃣ Containerization (Docker)
- Application and model encapsulated into a Docker image  
- Image pushed to **Google Container Registry (GCR)**  

### 6️⃣ CI/CD Automation (Jenkins)
- Jenkins pipeline automates:  
  - Code checkout  
  - Data preprocessing  
  - Model training & evaluation  
  - MLflow logging  
  - Docker image build & push  
  - Deployment to Google Cloud Run  

### 7️⃣ Deployment (GCP Cloud Run)
- Final model exposed as a **REST API endpoint**  
- Serverless, auto-scalable environment  

###Project Structure
---

┣ 📂 data/ # Raw and processed datasets
┣ 📂 src/
┃ ┣ 📂 data_ingestion/ # Scripts for reading and validating data
┃ ┣ 📂 preprocessing/ # Feature engineering scripts
┃ ┣ 📂 model/ # Model training, tuning, evaluation
┃ ┣ 📂 utils/ # Helper functions and configs
┣ 📂 notebooks/ # EDA and experimentation
┣ 📂 jenkins/ # Jenkinsfile and pipeline definitions
┣ 📂 docker/ # Dockerfile and related configs
┣ 📂 mlruns/ # MLflow tracking logs
┣ 📜 requirements.txt # Dependencies
┣ 📜 app.py # Flask/FastAPI app for inference
┣ 📜 Dockerfile
┣ 📜 Jenkinsfile
┣ 📜 README.md

---

### 📊 Model Performance
| Metric       | Score |
| ------------ | ----- |
| **Accuracy** | 0.89  |
| **F1-Score** | 0.87  |

---
### 🧪 Run Locally
1️⃣ Clone the Repository
```
git clone https://github.com/murtuzamaaz/Hotel-Reservation-MLops/
cd hotel-Reservation-mlops
```
###2️⃣ Create a Virtual Environment
```
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```
###
3️⃣ Install Dependencies
```
pip install -r requirements.txt
```
###4️⃣ Run the Application
```
python pipeline/training_pipeline.py
```

### Deployment Steps
🐳 Docker Setup
```
docker build -t jenkins-dind . 
docker images
```
```
docker run -d --name jenkins-dind ^
--privileged ^
-p 8080:8080 -p 50000:50000 ^
-v //var/run/docker.sock:/var/run/docker.sock ^
-v jenkins_home:/var/jenkins_home ^
jenkins-dind
```

Creating Venv in container and installing python and dependencies
```
docker exec -u root -it jenkins-dind bash
apt update -y
apt install -y python3
python3 --version
ln -s /usr/bin/python3 /usr/bin/python
python --version
apt install -y python3-pip
apt install -y python3-venv
exit

docker restart jenkins-dind
```
### Updating packages in linux
```
docker exec -u root -it jenkins-dind bash
apt-get update
apt-get install -y curl apt-transport-https ca-certificates gnupg
curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key add -
echo "deb https://packages.cloud.google.com/apt cloud-sdk main" | tee -a /etc/apt/sources.list.d/google-cloud-sdk.list

apt-get update && apt-get install -y google-cloud-sdk
gcloud --version
exit

```













