pipeline {
    agent {
        docker {
            image 'gradle:jdk8-alpine' 
            args '-v /var/jenkins_home/.m2:/root/.m2' 
        }
    }
    stages {
        stage('Prepare Folder') { 
            steps {
                sh '''
                echo "Preparing Docker Build Folder"
                gradle dockerPrepare
                '''
            }
        }
        stage('Build Image') { 
            agent none
            steps {
                sh '''
                gradle docker
                '''
            }
        }
    }
}