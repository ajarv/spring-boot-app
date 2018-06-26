pipeline {
    agent {
        docker {
            image 'gradle:jdk8-alpine' 
            args '-v /var/jenkins_home/.m2:/root/.m2' 
        }
    }
    stages {
        
        stage('Build Image') { 
            agent none
            steps {
                sh '''
                pwd
                . ./gradle.properties
                cd build/docker
                which docker            
                // docker build -t summer-sdge/gs-spring-boot-docker:test  .
                '''
            }
        }
    }
}