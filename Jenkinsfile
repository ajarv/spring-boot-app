pipeline {
    agent {
        docker {
            image 'gradle:jdk8-alpine' 
            args '-v /var/jenkins_home/.m2:/root/.m2' 
        }
    }
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