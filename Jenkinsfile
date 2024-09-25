pipeline {
    agent any

    environment {
        DOCKERHUB_USERNAME = 'dunkzilla10'
        DOCKERHUB_PASSWORD = 'hammer@15'
    }

    stages {
        stage('Checkout Code') {
            steps {
                git branch: 'main', url: 'https://github.com/Mujster/MLOps-Task5.git'
            }
        }
        stage('Login to Docker Hub') {
            steps {
                script {
                    sh "echo \"$DOCKERHUB_PASSWORD\" | docker login -u \"$DOCKERHUB_USERNAME\" --password-stdin"
                }
            }
        }
        stage('Build Docker Image') {
            steps {
                script {
                    sh 'ls -la'
                    sh "docker build -t $DOCKERHUB_USERNAME/mlops-task ."
                }
            }
        }
        stage('Push Docker Image') {
            steps {
                script {
                    sh "docker push $DOCKERHUB_USERNAME/mlops-task:latest"
                }
            }
        }
    }

    post {
        always {
            cleanWs()
        }
    }
}