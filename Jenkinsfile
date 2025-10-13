pipeline{
    agent any

    stages{
        stage("CLoning Github repo to jenkins"){
            steps{
                script{
                    echo 'Cloning Github repo to Jenkins'
                    checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[credentialsId: 'github-token', url: 'https://github.com/murtuzamaaz/Hotel-Reservation-MLops.git']])
                }
            }
        }
    }
}