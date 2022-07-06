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
                 }
            }
        }
	stage('rabbitmq') {
            steps {
                script {
	            bat 'helm install rabbitmq --set auth.username=admin,auth.password=secretpassword,auth.erlangCookie=secretcookie bitnami/rabbitmq' 
	            bat 'ping -n 30 127.0.0.1 > nul'
// 		    bat 'kubectl port-forward svc/release-rabbitmq 15672:15672'
		    bat 'echo docker push'	
                 }
            }
        }  
	stage('Build Docker image - locally') {
            steps {
                script{
                    bat "docker build -t %BUILD_NUMBER% ./producer"
                    bat "start/min docker run -p -p 127.0.0.1:8777:8777 $BUILD_NUMBER "
                }
            }
         }
	stage('docker push') {
            steps {
                script {
                    bat 'docker tag %BUILD_NUMBER%:latest photop/%BUILD_NUMBER%:latest'
                    bat 'docker push photop/%BUILD_NUMBER%:latest'
		    bat 'echo docker push'	
                 }
            }
        } 

    }	
}
