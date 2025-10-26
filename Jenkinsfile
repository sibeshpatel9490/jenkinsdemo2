node {
    try {
        stage('Checkout Code') {
            checkout scm
        }
        stage('Extract Data') {
            bat "C:\\Users\\HP\\AppData\\Local\\Programs\\Python\\Python313\\python.exe extract_data.py"
        }
    }
    catch(err) {
        echo "Pipeline Error : ${err}"
    }
    finally {
        echo "pipeline completed"
    }
}