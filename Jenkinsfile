pipeline {
    agent none
    stages {
        stage('Build - Unit Test') { 
            agent {
                docker {
                    image 'gradle:jdk8-alpine' 
                    args '-u root -v /var/jenkins_home/.m2:/root/.m2' 
                }
            }
            steps {
                sh 'gradle build' 
            }
        }
        stage('Package Docker Image') { 
            agent {
                docker {
                    image 'jenkinsci/blueocean' 
                    args '-v /var/run/docker.sock:/var/run/docker.sock' 
                }
            }
            steps {
                echo 'Building Docker'
                sh 'pwd'
                sh 'ls -al'
                sh 'docker'
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
        }        
    }
    post {
        always {
            echo "Build Completed ${currentBuild.fullDisplayName} Status:  ${currentBuild.result}"
        }
        success {
            // notify users when the Pipeline succeeds
            echo "Success"
            mail bcc: '', body: "<b>Example</b><br>\n\<br>Project: ${env.JOB_NAME} <br>Build Number: ${env.BUILD_NUMBER} <br> URL build: ${env.BUILD_URL}", cc: '', charset: 'UTF-8', from: '', mimeType: 'text/html', replyTo: '', subject: "ERROR CI: Project name -> ${env.JOB_NAME}", to: "avashisth@semprautilities.com";

        }
        failure {
            // notify users when the Pipeline fails
            echo "Rollback to previous version"
            mail bcc: '', body: "<b>Example</b><br>\n\<br>Project: ${env.JOB_NAME} <br>Build Number: ${env.BUILD_NUMBER} <br> URL build: ${env.BUILD_URL}", cc: '', charset: 'UTF-8', from: '', mimeType: 'text/html', replyTo: '', subject: "SUCCESS CI: Project name -> ${env.JOB_NAME}", to: "avashisth@semprautilities.com";
        }
    }
}