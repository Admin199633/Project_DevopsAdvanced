podTemplate(containers: [
    containerTemplate(
        name: 'test', 
        image: 'jenkinsci/jnlp-slave:alpine'
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
