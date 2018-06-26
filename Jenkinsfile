pipeline {
    agent none
    stages {
        stage('Build - Unit Test') { 
            agent {
                docker {
                    image 'gradle:jdk8-alpine' 
                    args '-v /var/jenkins_home/.m2:/root/.m2' 
                }
            }
            steps {
                sh 'gradle build' 
            }
        }
        stage('Package Docker Image') { 
            agent {
                docker {
                    image 'gradle:jdk8-alpine' 
                    args '-v /var/jenkins_home/.m2:/root/.m2' 
                }
            }
            steps {
                echo 'Building Docker'
                sleep 20
            }
        }
        stage('Deploy in Dev') { 
            steps {
                echo 'Deploying Docker Image'
                sleep 20
            }
        }
        stage('Run Integration Tests'){
             agent {
                docker {
                    image 'qnib/pytest'
                }
            }
            steps {
                sh 'py.test --verbose --junit-xml test-reports/results.xml ./integration-test-scripts/test01.py'
            }
            post {
                always {
                    junit 'test-reports/results.xml'
                }
            }
        }
    }
}