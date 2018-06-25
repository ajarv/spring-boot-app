pipeline {
    agent {
        docker {
            image 'gradle:jdk8-alpine' 
            args '-v /var/jenkins_home/.m2:/root/.m2' 
        }
    }
    stages {
        stage('Build Classes') { 
            steps {
                sh 'gradle classes' 
            }
        }
        stage('Run Tests') { 
            steps {
                sh 'gradle test' 
            }
        }
        stage('Build Package with label') { 
            steps {
                sh 'gradle docker' 
            }
        }

    }
}