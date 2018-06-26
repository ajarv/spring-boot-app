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
                Preparing Docker Build Folder'
                sh 'mkdir -p /var/jenkins_home/jobs/springboot-java-app/workspace'
                sh 'gradle dockerPrepare
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