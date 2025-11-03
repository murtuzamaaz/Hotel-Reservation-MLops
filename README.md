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
## ScreenShots
<img width="1894" height="863" alt="Screenshot 2025-11-03 195615" src="https://github.com/user-attachments/assets/1bc49eff-ab9f-48dc-8ab2-61299d7fcdf3" />


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
    git clone https://github.com/murtuzamaaz/Hotel-Reservation-MLops/
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
hotel-Reservation-mlops/
```
hotel-reservation-mlops/
│
├── data/
│ ├── raw/ # Raw hotel booking data
│ └── processed/ # Cleaned & preprocessed data
│
├── notebooks/
│ └── EDA.ipynb # Exploratory Data Analysis notebook
│
├── src/
│ ├── data_ingestion.py # Loads data from GCP Storage / local path
│ ├── feature_engineering.py # Encodes categorical vars, feature scaling, etc.
│ ├── model/
│ │ ├── train.py # Model training, evaluation, and MLflow logging
│ │ ├── predict.py # Handles inference API logic
│ │ └── init.py
│ ├── pipeline/
│ │ ├── train_pipeline.py # Combined data → model training workflow
│ │ ├── predict_pipeline.py # Combined data → inference workflow
│ │ └── init.py
│ ├── utils/
│ │ ├── logger.py # Centralized logging utility
│ │ ├── helpers.py # Reusable helper functions
│ │ └── init.py
│ └── init.py
│
├── app.py # Flask app for serving predictions
│
├── Dockerfile # Docker build configuration
├── Jenkinsfile # Jenkins CI/CD pipeline definition
├── requirements.txt # Python dependencies
├── config.yaml # Configuration for paths, parameters, etc.
├── README.md # Documentation
├── .dockerignore # Ignored files for Docker context
├── .gitignore # Ignored files for Git
│
└── mlruns/ # MLflow experiment tracking directory
└── ... # Stored model artifacts and logs
```
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
```
curl [https://packages.cloud.google.com/apt/doc/apt-key.gpg](https://packages.cloud.google.com/apt/doc/apt-key.gpg) | apt-key add -
echo "deb [https://packages.cloud.google.com/apt](https://packages.cloud.google.com/apt) cloud-sdk main" | tee -a /etc/apt/sources.list.d/google-cloud-sdk.list
```
# Install the SDK
```
apt-get update && apt-get install -y google-cloud-sdk
gcloud --version
exit
```

---

## 🚀 Running the CI/CD Pipeline

Once your Jenkins container is up and running, follow these steps to set up and execute your automated build and deployment pipeline.

---

### 🧭 Step 1: Access Jenkins & Initial Setup

1. Open Jenkins in your browser:
```
http://localhost:8080
```



2. Retrieve the initial admin password from your Jenkins container logs:

```
docker exec jenkins-dind cat /var/jenkins_home/secrets/initialAdminPassword
Copy the password, paste it into the Jenkins setup screen, and complete the setup wizard.
✅ Tip: Installing the suggested plugins during setup is recommended.
```

🔐 Step 2: Configure Credentials
Your Jenkins pipeline requires credentials to interact with GitHub and Google Cloud Platform (GCP).

🪣 GitHub Token Setup
Create a GitHub Personal Access Token with repo permissions.
```
(GitHub → Settings → Developer Settings → Personal Access Tokens → Tokens (classic))
```

In Jenkins, navigate to:
```
Manage Jenkins → Credentials → System → Global credentials
Click Add Credentials → choose "Secret text".

Set:

ID: github-token
(Ensure this matches the ID used in your Jenkinsfile.)

Secret: Paste your GitHub token here.
```

☁️ GCP Service Account Key Setup
In your Google Cloud Console, create a Service Account.

Assign the following roles:

Cloud Run Admin

Storage Admin (or Storage Object Admin)

Artifact Registry Admin

Generate and download a JSON key for this service account.

In Jenkins, go to:

```
Manage Jenkins → Credentials → System → Global credentials
Click Add Credentials → choose "Secret file".
```

Set:

ID: gcp-key
(Ensure this matches the ID used in your Jenkinsfile.)

Upload File: Select your downloaded JSON key.

⚙️ Step 3: Run the Build
From the Jenkins dashboard, click New Item → select Pipeline → click OK.

In the job configuration:

Scroll down to the Pipeline section.

Under Definition, select Pipeline script from SCM.

Set SCM to Git.

Enter your repository URL, e.g.:

```
https://github.com/murtuzamaaz/Hotel-Reservation-MLops.git
Specify the branch (e.g., main).
```

Set Script Path to:

nginx
Copy code
Jenkinsfile
Click Save.

On the left sidebar, click Build Now.

🧩 What Happens Next
Once triggered, Jenkins will automatically execute all pipeline stages:

Checkout – Pulls the latest code from GitHub.

Install Dependencies – Sets up the environment.

Train Model – Runs model training and MLflow logging.

Build Docker Image – Containerizes the trained model and app.

Push to GCR – Pushes the image to Google Container Registry.

Deploy to Cloud Run – Deploys the image to a live, serverless endpoint.

You can monitor each stage from the Jenkins dashboard — successful stages appear with a ✅ green status.
