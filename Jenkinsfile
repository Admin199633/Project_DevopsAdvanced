podTemplate(yaml: '''
apiVersion: v1
kind: Pod
spec:
  containers:
  - name: docker
    image: docker:19.03.1-dind
    securityContext:
      privileged: true
    env:
      - name: DOCKER_TLS_CERTDIR
        value: ""
''') 
pipeline { 
    agent any
    environment { 
        registry = "photop/micro_focus" 
        registryCredential = 'dockerhub_id'
        dockerImage = ""
	buildnm= "%BUILD_NUMBER%"
    } 
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
	stage('delete helm') {
            steps {
                script {
                    bat 'helm delete rabbitmq '
		    bat 'echo delete helm'
		    bat 'echo KAKI Gadol'
                }
            }
        }
	stage('rabbitmq') {
            steps {
                script {
		    bat 'helm repo add bitnami https://charts.bitnami.com/bitnami'	
	            bat 'helm install rabbitmq --set auth.username=admin,auth.password=secretpassword,auth.erlangCookie=secretcookie bitnami/rabbitmq' 
// 	            bat 'ping -n 30 127.0.0.1 > nul'
		    bat 'echo docker push'	
                 }
            }
        }  
	stage('Build Docker image - locally') {
            steps {
                script{
                    bat "docker build -t devops:%BUILD_NUMBER% ./producer"
                    bat "start/min docker run -p -p 127.0.0.1:8777:8777 $BUILD_NUMBER "
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
		    bat 'kubectl get pods'	
                 }
            }
        } 
        stage('Helm create consumer') {
            steps {
                script {
	            bat 'helm create consumer'
                    bat 'helm install consumer --set image.tag=%BUILD_NUMBER% ./consumer-helm '
		    bat 'kubectl get pods'	
                 }
            }
        } 

    }	
}
