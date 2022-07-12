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
''') {
    node(POD_LABEL) {
        stage ('Docker-Login')
        container('docker')
        {
            			withCredentials([usernamePassword(credentialsId: 'jenkins-dockerhub', passwordVariable: 'password', usernameVariable: 'username')]) {
                         sh '''
                         echo ${password} | docker login -u ${username} --password-stdin
                         '''
                    }
        }
        stage ('Docker-Build'){
        git branch: 'main', url: 'https://github.com/Admin199633/Project_Devops.git'
        container('docker') {
            
            sh 'docker version && cd docker/consumer/ && docker build -t consumer .'
            sh 'docker version && cd docker/producer/ && docker build -t producer .'
            sh 'docker images'
			sh 'docker image tag producer yahel567/producer:latest'
			sh 'docker image tag consumer yahel567/consumer:latest'
			sh 'docker images'
			sh 'docker image push yahel567/producer:latest'
			sh 'docker image push yahel567/consumer:latest'
			
        }
        }
    }
}
