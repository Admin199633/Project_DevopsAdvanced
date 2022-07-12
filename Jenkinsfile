podTemplate(cloud: 'k8s-houston', label: 'api-build', yaml: """
apiVersion: v1
kind: Pod
metadata:
  name: maven
spec:
  containers:
  - name: maven
    image: maven:3-jdk-8-alpine
    volumeMounts:
      - name: volume-0
        mountPath: /mvn/.m2nrepo
    command:
    - cat
    tty: true
    resources:
      requests:
        memory: "512Mi"
        cpu: "500m"
    securityContext:
      runAsUser: 10000
      fsGroup: 10000
""",
  containers: [
    containerTemplate(name: 'jnlp', image: 'jenkins/jnlp-slave:3.23-1-alpine', args: '${computer.jnlpmac} ${computer.name}', resourceRequestCpu: '250m', resourceRequestMemory: '512Mi'),
    containerTemplate(name: 'pmd', image: 'stash.trinet-devops.com:8443/pmd:pmd-bin-5.5.4', alwaysPullImage: false, ttyEnabled: true, command: 'cat'),
    containerTemplate(name: 'owasp-zap', image: 'stash.trinet-devops.com:8443/owasp-zap:2.7.0', ttyEnabled: true, command: 'cat'),
    containerTemplate(name: 'kubectl', image: 'lachlanevenson/k8s-kubectl:v1.8.7', ttyEnabled: true, command: 'cat'),
    containerTemplate(name: 'dind', image: 'docker:18.01.0-ce-dind', privileged: true, resourceRequestCpu: '20m', resourceRequestMemory: '512Mi',),
    containerTemplate(name: 'docker-cmds', image: 'docker:18.01.0-ce', ttyEnabled: true, command: 'cat', envVars: [envVar(key: 'DOCKER_HOST', value: 'tcp://localhost:2375')]),
  ],
  volumes: [
    persistentVolumeClaim(claimName: 'jenkins-pv-claim', mountPath: '/mvn/.m2nrepo'),
    emptyDirVolume(mountPath: '/var/lib/docker', memory: false)
  ]
)
