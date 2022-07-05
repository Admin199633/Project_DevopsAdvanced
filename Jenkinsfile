pipeline { 
    agent any
    environment { 
        registry = "photop/micro_focus" 
        registryCredential = 'dockerhub_id'
        dockerImage = ""
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
                script {
			bat "docker build . -f Dockerfile --no-cache --pull --force-rm -t photop/producer"
// 		      dockerImage = docker.build registry + ":$BUILD_NUMBER" "./producer"
// 		      bat 'echo success Build'
//                      docker.withRegistry('', registryCredential) {	
//                      dockerImage.push() 	 
		     bat "echo seccsses push"
		     }
		}
	    } 
       }
   }
}
