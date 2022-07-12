podTemplate(containers: [
    containerTemplate(
        name: 'TEST', 
        image: 'docker:19.03.1-dind'
        )
  ]) {

    node(POD_LABEL) {
        stage('Get a Maven project') {
            container('jnlp') {
                stage('Shell Execution') {
                    sh '''
                    echo "Hello! I am executing shell"
                    '''
                }
            }
        }

    }
}
