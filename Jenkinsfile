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
                git 'https://github.com/Admin199633/Project_Devops.git'
            }
        }
        stage('Flask.py') {
            steps {
                script {
		    bat  'echo hello word'
                    bat 'cd producer'
                    bat 'docker build . -f Dockerfile --no-cache --pull --force-rm -t photop/micro_focus/producer'
		    bat 'echo secsses'
                }
            }
        }
    }
}
