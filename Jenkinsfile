
pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/shashankchaurasia136/html-form-jenkins.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'python3 -m pip install -r requirements.txt'
            }
        }

        stage('Test HTML Form') {
            steps {
                sh 'python3 -m pytest -v test_form.py'
            }
        }
    }

    post {
        success {
            echo 'SUCCESS: All HTML form tests passed.'
        }
        failure {
            echo 'FAILURE: Check the console output for errors.'
        }
    }
}
