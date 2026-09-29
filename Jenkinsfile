pipeline {
    agent any

    stages {

        stage('Install Dependencies') {
            steps {
                dir('SauceDemo') {
                    bat 'python -m pip install -r requirements.txt'
                }
            }
        }

        stage('Run Tests') {
            steps {
                dir('SauceDemo') {
                    bat 'python -m pytest -v -n 2 --html=reports/report.html --self-contained-html --alluredir=allure-results'
                }
            }
        }
    }

    post {
        always {

            publishHTML([
                allowMissing: true,
                alwaysLinkToLastBuild: true,
                keepAll: true,
                reportDir: 'SauceDemo/reports',
                reportFiles: 'report.html',
                reportName: 'Pytest HTML Report'
            ])

            allure([
                results: [[path: 'SauceDemo/allure-results']]
            ])

            echo 'Automation execution completed'
        }

        success {
            echo 'All tests passed'
        }

        failure {
            echo 'Automation tests failed'
        }
    }
}