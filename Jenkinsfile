pipeline{
    agent any

    environment{
        VENV_DIR='venv'
    }

    stages{
        stage("CLoning Github repo to jenkins"){
            steps{
                script{
                    echo 'Cloning Github repo to Jenkins'
                    checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[credentialsId: 'github-token', url: 'https://github.com/murtuzamaaz/Hotel-Reservation-MLops.git']])
                }
            }
        }

        stage("Setting up Virtual ENvironment and Installing Dependecies"){
            steps{
                script{
                    echo 'Setting up Virtual ENvironment and Installing Dependecies'
                    sh ''' 
                    python -m venv ${VENV_DIR}
                    . ${VENV_DIR}/bin/activate
                    pip install --upgrade pip
                    pip install -e .
                     '''
                }
            }
        }
    }
}