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
                  stage('Flask.py') {
            steps {
                script {
                    bat 'cd producer'
		    bat 'pwd'
		    bat 'docker build ./producer -f Dockerfile --no-cache --pull --force-rm -t /producer' 
                    bat 'echo success Flask.py'
                }
            }
        } 
    }
  }
