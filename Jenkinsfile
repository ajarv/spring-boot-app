properties = null


def loadProperties() {
    node {
        checkout scm
        properties = readProperties file: 'gradle.properties'
        echo "appReleaseVersion - ${properties.appReleaseVersion}"
    }
}

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
        stage('Prepare Docker Files') { 
            agent {
                docker {
                    image 'gradle:jdk8-alpine' 
                    args '-u root -v /var/jenkins_home/.m2:/root/.m2' 
                }
            }
            steps {
                sh 'gradle dockerPrepare' 
            }
        }
        stage('Build Docker Image') { 
            agent {
                docker {
                    image 'jenkinsci/blueocean' 
                    args '-v /var/run/docker.sock:/var/run/docker.sock' 
                }
            }
            steps {
                echo 'Building Docker Image'
                script {
                    loadProperties()
                    echo "appReleaseVersion ${properties.appReleaseVersion}"
                }
                echo 'App Release Version ${env.appReleaseVersion}' 
                sh 'docker build -t summer-sdge/gs-spring-boot-docker:1.0.1 ./build/docker' 
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
                script {
                    def props = readProperties file:'gradle.properties';
                    env['appReleaseVersion'] = props['appReleaseVersion'];
                }
                sh 'pwd'
                sh 'ls -al'
                sh 'docker'
                sleep 4
            }
        }
        stage('Deploy in Dev') { 
            steps {
                echo 'Stop the previous container version if running'
                sleep 4
                echo 'Start new container version'
                sleep 4
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
            echo "Change Integrated Successfully"
            mail bcc: '', body: "<b>Example</b><br><br>Project: ${env.JOB_NAME} <br>Build Number: ${env.BUILD_NUMBER} <br> URL build: ${env.BUILD_URL}", cc: '', charset: 'UTF-8', from: '', mimeType: 'text/html', replyTo: '', subject: "SUCCESS CI: Project name -> ${env.JOB_NAME}", to: "avashisth@semprautilities.com";

        }
        failure {
            // notify users when the Pipeline fails
            echo "Change failed tests"
            mail bcc: '', body: "<b>Example</b><br><br>Project: ${env.JOB_NAME} <br>Build Number: ${env.BUILD_NUMBER} <br> URL build: ${env.BUILD_URL}", cc: '', charset: 'UTF-8', from: '', mimeType: 'text/html', replyTo: '', subject: "FAILURE CI: Project name -> ${env.JOB_NAME}", to: "avashisth@semprautilities.com";
            echo "Rolling back to previous version"
            mail bcc: '', body: "<b>Example</b><br><br>Project: ${env.JOB_NAME} <br>Build Number: ${env.BUILD_NUMBER} <br> URL build: ${env.BUILD_URL}", cc: '', charset: 'UTF-8', from: '', mimeType: 'text/html', replyTo: '', subject: "ROLLED BACK CI: Project name -> ${env.JOB_NAME}", to: "avashisth@semprautilities.com";
        }
    }
}