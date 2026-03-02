pipeline {
	agent any
	
	stages {
		stage('Cleanup') {
			steps {
				sh '''
				pkill -f app.py || true
				'''
			}
		}
		
		stage('Setup Virtual Environment') {
			steps {
				sh '''
				python3 -m venv venv
				source venv/bin/activate
				pip install -r requirements.txt
			}
		}
		
		stage('Start Application') {
			steps {
				sh '''
				source venv/bin/activate
				python app.py &
				sleep 5
				'''
			}
		}

		stage('Health Check') {
			steps {
				sh '''
				curl http://localhost:5000/health
				'''
			}	
		}

	}
}
