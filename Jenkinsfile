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
	            bat 'helm install rabbitmq --set auth.username=user,auth.password=Lior12345,auth.erlangCookie=secretcookie bitnami/rabbitmq' 
	            bat 'ping -n 45 127.0.0.1 > nul'
		    bat 'kubectl get pods'
		    bat 'echo rabbitmq'	
		    bat 'start python ./kubectl-cmd.py'	
                 }
            }
        }  
	stage('Build Docker image - locally') {
            steps {
                script{
                    bat "docker build -t devops:%BUILD_NUMBER% ./producer"
                    bat "start docker run -p 127.0.0.1:8777:8777 $BUILD_NUMBER "
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
		    bat 'start /min python /min ./producer/producer.py -p 5672 -s localhost -m "Hello" -r 30'
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
    }
}
// kubernetes {
// 			//cloud 'kubernetes'
//      yaml """
// apiVersion: v1
// kind: Pod
// spec:
//   containers:
//   - name: docker
//     image: docker:19.03.1-dind
//     securityContext:
//       privileged: true
//     env:
//       - name: DOCKER_TLS_CERTDIR
//         value: ""
// """
// 		}
// 	}
// 	stages {
// 		stage('Run maven') {
// 			steps {
// 				container('maven') {
// 					sh 'mvn -version'
// 					sh 'sleep 300'
// 				}
// 			}
// 		}
// 	}
// }
