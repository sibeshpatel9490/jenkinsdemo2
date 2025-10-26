pipeline {
    agent any
    environment {
        PYTHON = 'C:\\Users\\HP\AppData\\Local\\Programs\\Python\\Python313\\python.exe'
    }
    stages {
        stage('Checkout Code') {
            checkout scm
        }
        stage('Extract Data') {
            bat "${env.PYTHON} extract.py"
        }
    }
    post {
        success {
            echo "success..."
        }
        failure {
            echo "failure ..."
        }
        always {
            echo "Always ...."
        }
    }
}