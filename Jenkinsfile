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
                  stage('Build Image') {
            steps {
                script {
		    bat "docker build -t \"$BUILD_NUMBER\" ./producer"
                    bat 'echo success build Docker image'
                }
            }
        } 
                  stage('docker push') {
            steps {
                script { photop/micro_focus
                    bat 'docker tag 23:latest photop/23:latest'
                    bat 'docker push  photop/micro_focus:23'
		    bat 'echo docker push'
		     bat "echo seccsses push"
		     }
		}
	    } 
   }
}
