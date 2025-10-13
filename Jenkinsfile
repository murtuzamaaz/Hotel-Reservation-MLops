pipeline {
    agent any

    environment {
        VENV_DIR = 'venv'
        GCP_PROJECT = "manifest-campus-474314-i0"
        GCLOUD_PATH = "/var/jenkins_home/google-cloud-sdk/bin"
        DOCKER_IMAGE = "gcr.io/${GCP_PROJECT}/ml-project:latest"
    }

    stages {
        stage('Cloning Github repo to Jenkins') {
            steps {
                script {
                    echo 'Cloning Github repo to Jenkins............'
                    checkout scmGit(
                        branches: [[name: '*/main']], 
                        extensions: [], 
                        userRemoteConfigs: [[
                            credentialsId: 'github-token', 
                            url: 'https://github.com/murtuzamaaz/Hotel-Reservation-MLops.git'
                        ]]
                    )
                }
            }
        }

        stage('Setting up Virtual Environment and Installing dependencies') {
            steps {
                script {
                    echo 'Setting up Virtual Environment and Installing dependencies............'
                    sh '''
                        python -m venv ${VENV_DIR}
                        . ${VENV_DIR}/bin/activate
                        pip install --upgrade pip
                        pip install -e .
                    '''
                }
            }
        }

        stage('Training ML Model') {
            steps {
                withCredentials([file(credentialsId: 'gcp-key', variable: 'GOOGLE_APPLICATION_CREDENTIALS')]) {
                    script {
                        echo 'Training ML model with GCP credentials............'
                        sh '''
                            . ${VENV_DIR}/bin/activate
                            export GOOGLE_APPLICATION_CREDENTIALS=${GOOGLE_APPLICATION_CREDENTIALS}
                            echo "Running training pipeline..."
                            python pipeline/training_pipeline.py
                        '''
                    }
                }
            }
        }

        stage('Building and Pushing Docker Image to GCR') {
            steps {
                withCredentials([file(credentialsId: 'gcp-key', variable: 'GOOGLE_APPLICATION_CREDENTIALS')]) {
                    script {
                        echo 'Building and Pushing Docker Image to GCR.............'
                        sh '''
                            export PATH=$PATH:${GCLOUD_PATH}
                            
                            gcloud auth activate-service-account --key-file=${GOOGLE_APPLICATION_CREDENTIALS}
                            
                            gcloud config set project ${GCP_PROJECT}
                            
                            gcloud auth configure-docker --quiet
                            
                            docker build -t ${DOCKER_IMAGE} .
                            
                            docker push ${DOCKER_IMAGE}
                            
                            echo "Docker image pushed successfully to ${DOCKER_IMAGE}"
                        '''
                    }
                }
            }
        }
    }

    post {
        always {
            echo 'Pipeline execution completed.'
        }
        failure {
            echo 'Pipeline failed! Check logs above for details.'
        }
        success {
            echo 'Pipeline succeeded! Docker image is ready for deployment.'
        }
    }
}