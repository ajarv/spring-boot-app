pipeline {
    agent {
        docker {
            image 'gradle:jdk8-alpine' 
            args '-v /c/temp/.m2:/root/.m2' 
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
                sh gradle dockerPrepare
                '''
            }
        }
        stage('Build Image') { 
            steps {
                sh 'gradle docker_image --stacktrace'
            }
        }
    }
}