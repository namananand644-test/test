pipeline {
    agent {
    docker {
        image 'docker:cli'
        args '-u root:root -v /var/run/docker.sock:/var/run/docker.sock'
    }
}

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t task-manager:latest .'
            }
        }

        stage('Test Docker Image') {
            steps {
                sh 'docker run --rm task-manager:latest python -m pytest -v'
            }
        }

        stage('Deploy Application') {
            steps {
                sh '''
                    docker rm -f task-manager || true
                    docker run -d \
                        --name task-manager \
                        --restart unless-stopped \
                        -p 8000:8000 \
                        task-manager:latest
                '''
            }
        }
    }
}
