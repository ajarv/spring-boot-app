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
                echo 'Stop the previous container version if running'
                sleep 20
                echo 'Start new container version'
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
                success {
                 // notify users when the Pipeline fails
                    mail to: 'AVashisth@semprautilities.com',
                        subject: "Success Pipeline: ${currentBuild.fullDisplayName}",
                        body: "${env.BUILD_URL}"
                }
                failure {
                 // notify users when the Pipeline fails
                    mail to: 'AVashisth@semprautilities.com',
                        subject: "Failed Pipeline: ${currentBuild.fullDisplayName}",
                        body: "Something is wrong with ${env.BUILD_URL}"
                    echo "Rollback to previous version"
                    echo "Undeploy Current Version"
                    sleep 5
                    echo "Deploy previous version"
                    sleep 5
                }
            }
        }        
    }
}