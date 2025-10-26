pipeline {
    agent any
    environment {
        PYTHON = 'C:\\Users\\HP\\AppData\\Local\\Programs\\Python\\Python313\\python.exe'
    }
    trigger {
        cron("*/2 * * * *")
    }
    stages {
        stage('Checkout Code') {
            steps {
                checkout scm
            }
        }
        stage('Extract Data') {
            steps {
                bat "${env.PYTHON} extract_data.py"
            }
        }
    }
    post {
        success {
            echo "success..."
        }
        failure {
            echo "failure ..."
        }
    }
}