pipeline {
    agent {
        docker {
            image 'gradle:jdk8-alpine' 
            args '-v /var/jenkins_home/.m2:/root/.m2' 
        }
    }
    stages {
        stage('Build Image') { 
            agent {
                docker {
                    image 'jenkinsci/blueocean' 
                    args '-u root -v /var/run/docker.sock:/var/run/docker.sock' 
                }
            }
            steps {
                sh '''
                pwd
                cd build/docker
                docker
                '''
            }
        }
    }
}