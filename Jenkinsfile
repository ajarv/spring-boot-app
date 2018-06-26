pipeline {
    agent none
    stages {
        stage('Run Integration Tests'){
             agent {
                docker {
                    image 'python:2-alpine'
                }
            }
            steps {
                sh 'pwd '
                sh 'ls -al'
            }
        }
    }
}