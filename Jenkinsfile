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
        stage('Prepare Folder') { 
            steps {
                sh '''
                echo "Preparing Docker Build Folder"
                gradle dockerPrepare
                '''
            }
        }
        stage('Build Docker Image') { 
            steps {
                echo 'Building Docker'
                sleep 20
            }
        }
        stage('Deploy Image') { 
            steps {
                echo 'Deploying Docker Image'
                sleep 20
            }
        }
        stage('Run Integration Tests'){
            steps {
                echo 'Running Integration Tests'
                sleep 20
            }
        }
    }
}