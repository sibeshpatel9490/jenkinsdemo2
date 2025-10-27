pipeline {
    agent any

    environment {
        PYTHON = 'C:\\Users\\HP\\AppData\\Local\\Programs\\Python\\Python313\\python.exe'
        MY_SECRET_TOKEN = credentials('MY_SECRET_TOKEN')
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Run Secure Reader') {
            steps {
                bat """
                set MY_SECRET_TOKEN=%MY_SECRET_TOKEN%
                %PYTHON% secure_reader.py
                """
            }
        }
    }
}
