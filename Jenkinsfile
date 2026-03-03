pipeline {
	agent any
		stages {
			stage('Checkout code') {
				steps {
					checkout scm
				}
			}
			stage('Build docker image') {
				steps {
					sh "docker build -t flask-app:${BUILD_NUMBER} ."
				}
			}	
			stage('Run Container') {
				steps {
					sh """
					docker rm -f flask-container || true
					docker run -d -p 5000:5000 --name flask-container flask-app:${BUILD_NUMBER}
				    """
				}
			}
			stage('Health Check') {
				steps {
					sh 'sleep 5'
					sh 'curl -f http://localhost:5000/health'
				}
			}		
		}

		post {
			always {
				sh 'docker rm -f flask-container || true'
			}
		}
} 	