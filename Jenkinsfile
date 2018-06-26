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
            post {
                always {
                    echo "Build Completed ${currentBuild.fullDisplayName} Status:  ${currentBuild.result}"
                }
                success {
                    // notify users when the Pipeline fails
                    mail to: 'AVashisth@semprautilities.com',
                        from: 'Jenkins <AVashisth@semprautilities.com>'
                        subject: "Success Pipeline: ${currentBuild.fullDisplayName}"
                        body: "${env.BUILD_URL}. The latest version of  applicaiton deployed in Dev now is NEW_VERSION_TAG"
                }
                failure {
                    // notify users when the Pipeline fails
                    mail to: 'AVashisth@semprautilities.com',
                        from: 'Jenkins <AVashisth@semprautilities.com>'
                        subject: "Failed Pipeline: ${currentBuild.fullDisplayName}"
                        body: "Build Failed ${env.BUILD_URL}."
                    echo "Rollback to previous version"
                    echo "Undeploy Current Version"
                    sleep 5
                    echo "Deploy previous version"
                    sleep 5
                    mail to: 'AVashisth@semprautilities.com',
                        from: 'Jenkins <AVashisth@semprautilities.com>'
                        subject: "Applicaiton Rolled Back success ${currentBuild.fullDisplayName}"
                        body: "Build Failed ${env.BUILD_URL}"
                    
                }
            }
            
        }        
    }
    post {
        always {
        echo "I ALWAYS run first"
        }
        unstable {
        echo "UNSTABLE runs after ALWAYS"
        }
  }
}