pipeline { 
    agent any
    stages {
        stage('properties') {
            steps {
                script {
                    properties([pipelineTriggers([pollSCM('*/30 * * * *')])])
                    properties([buildDiscarder(logRotator(daysToKeepStr: '5', numToKeepStr: '20')),])
                }
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
	            bat 'helm install rabbitmq --set auth.username=user,auth.password=Lior12345,auth.erlangCookie=secretcookie,metrics.enabled=true bitnami/rabbitmq' 
	            bat 'ping -n 45 127.0.0.1 > nul'
		    bat 'kubectl get pods'
		    bat 'echo rabbitmq'	
		    bat 'start python ./expose-RabbitMQ.py'	
                 }
            }
        }  
	stage('Build Docker image - locally') {
            steps {
                script{
                    bat "docker build -t devops:%BUILD_NUMBER% ./producer"
                }
            }
         }
	stage('docker push') {
            steps {
                script {
                    bat 'docker tag devops:%BUILD_NUMBER% photop/devops:%BUILD_NUMBER%'
                    bat 'docker push photop/devops:%BUILD_NUMBER%'
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
		    bat 'start python ./consumer/consumer.py -p 5672 -s localhost'
		    bat 'kubectl get pods'	
                 }
            }
        } 	
	stage('Helm Create monitoring') {
            steps {
                script {
	            bat 'helm install grafana grafana/grafana'
	            bat 'helm install prometheus bitnami/kube-prometheus '
		    bat 'start min/ python expose-RabbitMQ.py '
                }
            }
        }
	stage('Clean env') {
            steps {
                script {
                    bat 'helm delete rabbitmq consumer producer grafana prometheus '
		    bat 'echo delete helm'
                }
            }
        }
    }
}
