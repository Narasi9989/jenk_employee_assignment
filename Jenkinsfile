pipeline {
    agent any

    stages {

        stage('Install Dependencies') {
            steps {
                bat '"C:\\Users\\admin\\AppData\\Local\\Programs\\Python\\Python314\\python.exe" -m pip install -r requirements.txt'
            }
        }

        stage('Lint') {
            steps {
                bat '"C:\\Users\\admin\\AppData\\Local\\Programs\\Python\\Python314\\python.exe" -m flake8 .'
            }
        }

        stage('Unit Test') {
            steps {
                bat '"C:\\Users\\admin\\AppData\\Local\\Programs\\Python\\Python314\\python.exe" -m pytest'
            }
        }
    }
}