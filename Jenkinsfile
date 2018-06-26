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
                sh 'Running Integration Tests'
                sh 'python ./integration-test-scripts/test01.py'
            }
        }
    }
}