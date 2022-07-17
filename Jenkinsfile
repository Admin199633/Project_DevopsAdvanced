pipeline { 
    agent any
    stages {
        stage('properties') {
            steps {
                git branch: 'main', url: 'https://github.com/Admin199633/Project_Devops.git'
            }
        }
	stage('Creata DND(docker in docker)') {
            steps {
                script {
		    bat 'kubectl apply -f docker.yml'
		    bat 'echo docker in docker'
                }
            }
        }
	stage('rabbitmq') {
            steps {
                script {
	            bat 'helm install rabbitmq --set auth.username=user,auth.password=Lior12345,auth.erlangCookie=secretcookie,metrics.enabled=true,persistence.enabled=true bitnami/rabbitmq' 
	            bat 'ping -n 45 127.0.0.1 > nul'
		    bat 'kubectl get pods'
		    bat 'echo rabbitmq'	
		    bat 'start /min python ./expose-RabbitMQ.py'	
                 }
            }
        }  
	stage('Build Docker image - locally') {
            steps {
                script{
                    bat "docker build -t devops_producer:%BUILD_NUMBER% ./producer"
                    bat "docker build -t devops_consumer:%BUILD_NUMBER% ./consumer"
		    bat "start/min docker run -p -p 127.0.0.1:8777:8777 $BUILD_NUMBER"
                }
            }
         }
	stage('docker push') {
            steps {
                script {
                    bat 'docker tag devops:%BUILD_NUMBER% photop/devops_producer:%BUILD_NUMBER%'
                    bat 'docker push photop/devops_producer:%BUILD_NUMBER%'
                    bat 'docker tag devops:%BUILD_NUMBER% photop/devops_consumer:%BUILD_NUMBER%'
                    bat 'docker push photop/devops_consumer:%BUILD_NUMBER%'
		    bat 'echo docker push'	
                 }
            }
        } 
        stage('Helm create producer') {
            steps {
                script {
	            bat 'helm create poducer'
                    bat 'helm install producer --set image.tag=%BUILD_NUMBER% ./producer-helm '
		    bat 'start /min python ./producer/producer.py -p 5672 -s localhost -m "Hello Nuni" -r 30'
		    bat 'kubectl get pods'	
                 }
            }
        } 
        stage('Helm create consumer') {
            steps {
                script {
	            bat 'helm create consumer'
                    bat 'helm install consumer --set image.tag=%BUILD_NUMBER% ./consumer-helm '
		    bat 'start /min python ./consumer/consumer.py -p 5672 -s localhost'
		    bat 'kubectl get pods'	
                 }
            }
        } 	
	stage('monitoring') {
            steps {
                script {
		    bat 'helm repo update'
		    bat 'kubectl apply -f ./monitoring/namespace.yml '
		    bat 'helm install prometheus --namespace monitoring   prometheus-community/prometheus'	
	            bat 'kubectl apply -f monitoring/config.yml'
		    bat 'helm install -f monitoring/values.yml  --namespace monitoring  grafana grafana/grafana'
		    bat 'kubectl get pods -n monitoring'	
		    bat 'ping -n 25 127.0.0.1 > nul'	
		    bat 'start python expose-grafana.py'
		    bat 'ping -n 1000 127.0.0.1 > nul'	
                }
            }
        }
// 	stage('Clean env') {
//             steps {
//                 script {
//                     bat 'helm delete rabbitmq consumer producer grafana prometheus '
//	               bat 'helm delete -n monitoring prometheus grafana'
// 		       bat 'echo delete helm'
//                 }
//             }
//         }
	    
    }
}
