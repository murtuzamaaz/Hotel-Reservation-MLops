# 🏨 Hotel Reservation Cancellation Prediction — End-to-End MLOps Project

## 🚀 Overview

This project focuses on predicting whether a hotel reservation will be canceled—a classic **binary classification problem**—but with a full-fledged **MLOps workflow** behind it.
The main goal wasn’t just to build a machine learning model, but to implement a **production-grade, automated CI/CD pipeline** for reproducible, scalable, and reliable ML delivery.

---

## 🎯 Objectives

* Build an **end-to-end ML system** from data ingestion to deployment.
* Automate the entire ML workflow using **Jenkins CI/CD**.
* Ensure **reproducibility** and **traceability** using MLflow.
* Containerize and deploy the model on **Google Cloud Run**.
* Achieve strong performance metrics on hotel reservation data.

---

## ⚙️ MLOps Stack

| Component | Tool/Service | Purpose |
| :--- | :--- | :--- |
| **Version Control** | Git + GitHub | Source code management |
| **Automation** | Jenkins | Orchestrates CI/CD pipeline |
| **Containerization** | Docker | Packages application and dependencies |
| **Experiment Tracking** | MLflow | Logs parameters, metrics, and artifacts |
| **Cloud Platform** | Google Cloud Platform (GCP) | Storage, container registry, and deployment |
| **Deployment** | Google Cloud Run | Scalable, serverless model hosting |

---

## 🧠 ML Workflow

### 1. Data Ingestion

* **Source:** Google Cloud Storage
* Loads raw hotel reservation data
* Performs sanity checks and data validation

### 2. Feature Engineering & Preprocessing

* Custom transformations and encoding (Label Encoding, One-Hot Encoding)
* Handling of missing and categorical values
* Feature scaling for numerical columns

### 3. Model Training

* Automated hyperparameter tuning
* Training and validation split
* Model selection and evaluation (Accuracy, F1-Score)

### 4. Experiment Tracking (MLflow)

* Logs all model metrics, parameters, and artifacts
* Enables complete experiment reproducibility

### 5. Containerization (Docker)

* Application and model encapsulated into a Docker image
* Image pushed to **Google Container Registry (GCR)**

### 6. CI/CD Automation (Jenkins)

* Jenkins pipeline automates:
    * Code checkout
    * Data preprocessing
    * Model training & evaluation
    * MLflow logging
    * Docker image build & push
    * Deployment to Google Cloud Run

### 7. Deployment (GCP Cloud Run)

* Final model exposed as a **REST API endpoint**
* Serverless, auto-scalable environment

---


---

## 📊 Model Performance

| Metric | Score |
| :--- | :--- |
| **Accuracy** | 0.89 |
| **F1-Score** | 0.87 |

---

## 🧪 Run Locally

1.  **Clone the Repository**
    ```bash
    git clone [https://github.com/murtuzamaaz/Hotel-Reservation-MLops/](https://github.com/murtuzamaaz/Hotel-Reservation-MLops/)
    cd hotel-Reservation-mlops
    ```

2.  **Create a Virtual Environment**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3.  **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Run the Training Pipeline**
    ```bash
    python pipeline/training_pipeline.py
    ```

---

## 🐳 Jenkins & Deployment Setup

These steps guide you through setting up the Jenkins container and configuring it to run the CI/CD pipeline.

### 1. Build and Run the Jenkins (dind) Container

First, build the custom Jenkins image defined in your `Dockerfile`.

```bash
docker build -t jenkins-dind .
docker images
```


## 📂 Project Structure
. ├── 📂 data/ # Raw and processed datasets ├── 📂 src/ │ ├── 📂 data_ingestion/ # Scripts for reading and validating data │ ├── 📂 preprocessing/ # Feature engineering scripts │ ├── 📂 model/ # Model training, tuning, evaluation │ └── 📂 utils/ # Helper functions and configs ├── 📂 notebooks/ # EDA and experimentation ├── 📂 jenkins/ # Jenkinsfile and pipeline definitions ├── 📂 docker/ # Dockerfile and related configs ├── 📂 mlruns/ # MLflow tracking logs ├── 📜 requirements.txt # Dependencies ├── 📜 app.py # Flask/FastAPI app for inference ├── 📜 Dockerfile ├── 📜 Jenkinsfile └── 📜 README.md

Next, run the container. This command uses Docker-in-Docker (dind) and maps the Docker socket, allowing Jenkins to run Docker commands.

Note: The \ character is for Linux/macOS. On Windows (CMD/PowerShell), replace \ with ^.

```
docker run -d --name jenkins-dind \
  --privileged \
  -p 8080:8080 -p 50000:50000 \
  -v /var/run/docker.sock:/var/run/docker.sock \
  -v jenkins_home:/var/jenkins_home \
  jenkins-dind
```

2. Install Python in the Container
You must exec into the running container to install Python, pip, and venv.


```
# Get a root shell inside the running container
docker exec -u root -it jenkins-dind bash
```

# Install Python, pip, and venv
```
apt update -y
apt install -y python3
python3 --version
ln -s /usr/bin/python3 /usr/bin/python
python --version
apt install -y python3-pip
apt install -y python3-venv
exit
```

# Restart the container to apply changes
```
docker restart jenkins-dind
3. Install Google Cloud SDK in the Container
Repeat the process to install the gcloud CLI for GCP interactions.
```


# Get a root shell again
```
docker exec -u root -it jenkins-dind bash
```

# Update package lists
```
apt-get update
apt-get install -y curl apt-transport-https ca-certificates gnupg
```

# Add the gcloud SDK repository
curl [https://packages.cloud.google.com/apt/doc/apt-key.gpg](https://packages.cloud.google.com/apt/doc/apt-key.gpg) | apt-key add -
echo "deb [https://packages.cloud.google.com/apt](https://packages.cloud.google.com/apt) cloud-sdk main" | tee -a /etc/apt/sources.list.d/google-cloud-sdk.list

# Install the SDK
```
apt-get update && apt-get install -y google-cloud-sdk
gcloud --version
exit
```
🚀 Running the CI/CD Pipeline
Once your Jenkins container is running, follow these steps to run the build.

1. Access Jenkins & Initial Setup
Navigate to http://localhost:8080 in your browser.

Get the initial admin password from the container's logs to unlock Jenkins:

Bash

docker exec jenkins-dind cat /var/jenkins_home/secrets/initialAdminPassword
Copy the password, paste it into the Jenkins UI, and follow the setup instructions (installing suggested plugins is recommended).

2. Configure Credentials
The pipeline needs credentials to access GitHub and GCP.

GitHub Token:

Create a GitHub Personal Access Token with repo scopes.

In Jenkins, go to Manage Jenkins > Credentials > System > Global credentials.

Add a new "Secret text" credential.

Set the ID to github-token (or match the ID used in your Jenkinsfile).

Paste your token into the Secret field.

GCP Service Account Key:

In your Google Cloud project, create a Service Account.

Grant it the following roles: Cloud Run Admin, Storage Admin (or Storage Object Admin), and Artifact Registry Admin.

Create a JSON key for this service account and download it.

In Jenkins, go to Manage Jenkins > Credentials > System > Global credentials.

Add a new "Secret file" credential.

Set the ID to gcp-key (or match the ID used in your Jenkinsfile).

Upload your GCP JSON key file.

3. Run the Build
From the Jenkins dashboard, create a new "Pipeline" job.

In the job configuration, scroll down to the "Pipeline" section.

Select "Pipeline script from SCM".

Choose "Git" as the SCM.

Enter your repository's URL (e.g., https://github.com/murtuzamaaz/Hotel-Reservation-MLops.git).

Specify the branch to build (e.g., main).

Ensure the "Script Path" is Jenkinsfile.

Save the job.

Click on Build Now to trigger the pipeline. Jenkins will now execute all stages: check out, preprocess, train, log, build, and deploy.
