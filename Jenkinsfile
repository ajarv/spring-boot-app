pipeline {
    agent none
    stages {
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