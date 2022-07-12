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
//                     sh 'helm delete rabbitmq '
		    sh 'echo delete helm'	
//                  }
//             }
//         }
	stage('rabbitmq') {
            steps {
                script {
	            sh 'helm install rabbitmq --set auth.username=admin,auth.password=secretpassword,auth.erlangCookie=secretcookie bitnami/rabbitmq' 
// 	            bat 'ping -n 30 127.0.0.1 > nul'
// 		    bat 'kubectl port-forward svc/release-rabbitmq 15672:15672'
		    sh 'echo docker push'	
                 }
            }
        }  
	stage('Build Docker image - locally') {
            steps {
                script{
                    sh "docker build -t devops:%BUILD_NUMBER% ./producer"
                    sh "start/min docker run -p -p 127.0.0.1:8777:8777 $BUILD_NUMBER "
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
