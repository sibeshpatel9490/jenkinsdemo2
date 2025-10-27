pipeline {
    agent any

    environment {
        PYTHON = 'C:\\Users\\HP\\AppData\\Local\\Programs\\Python\\Python313\\python.exe'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                bat '''
                %PYTHON% -m pip install -r requirements.txt
                '''
            }
        }

        stage('Run API ETL Script') {
            steps {
                bat '%PYTHON% extract_data.py'
            }
        }
    }
}
