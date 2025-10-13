pipeline{
    agent any

    environment{
        VENV_DIR = 'venv'
        GCP_PROJECT = "manifest-campus-474314-i0"
        GCLOUD_PATH = "/var/jenkins_home/google-cloud-sdk/bin"
    }


    stages{
        stage('Cloning github repo to Jenkins'){
            steps{
                script{
                    echo'Cloning github repo to Jenkins'
                    checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[credentialsId: 'github-token', url: 'https://github.com/murtuzamaaz/Hotel-Reservation-MLops.git']])

                }
            }
        }

        stage('Setting up our Virtual Environment and Installing depedencies'){
            steps{
                script{
                    echo'Setting up our Virtual Environment and Installing depedencies'
                    sh ''' 

                    python -m venv ${VENV_DIR}
                    . ${VENV_DIR}/bin/activate

                    pip install --upgrade pip
                    pip install -e .


                    '''

                }
            }
        }



        stage('Building and Pushing Docker image to GCR'){
            steps{
                withCredentials([file(credentialsId:'gcp-key', variable : 'GOOGLE_APPLICATION_CREDENTIALS')]){
                    script{
                        echo 'Building and Pushing Docker image to GCR'
                        sh '''

                        export PATH=$PATH:${GCLOUD_PATH}
                        
                        gcloud auth activate-service-account --key-file=${GOOGLE_APPLICATION_CREDENTIALS}

                        gcloud config set project ${GCP_PROJECT}

                        gcloud auth configure-docker --quiet

                        docker build -t gcr.io/${GCP_PROJECT}/mlops-project-first:latest .

                        docker push gcr.io/${GCP_PROJECT}/mlops-project-first:latest

                        ''' 
                    }
                }
            }
        }


    }
}