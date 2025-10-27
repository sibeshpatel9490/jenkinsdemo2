pipeline {
    agent any

    environment {
        PYTHON_VERSION = 'C:\\Users\\HP\\AppData\\Local\\Programs\\Python\\Python313\\python.exe'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Set up Python') {
            steps {
                sh '''
                python${PYTHON_VERSION} -m venv venv
                source venv/bin/activate
                pip install --upgrade pip
                pip install -r requirements.txt
                '''
            }
        }

        stage('Run API ETL Script') {
            steps {
                sh '''
                source venv/bin/activate
                python extract_data.py
                '''
            }
        }
    }
}
