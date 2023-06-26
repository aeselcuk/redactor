

pipeline {
    agent none 
    stages {
        stage('Build') { 
            agent {
                docker {
                    image 'python:2-alpine' 
                }
            }
            steps {
                sh 'python -m eel app_v2/app.py web --onefile --noconsole' 
            }
        }
    }
}

