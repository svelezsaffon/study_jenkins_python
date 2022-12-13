pipeline {
    agent {
        kubernetes {
            label "build-pod"
            cloud "kubernetes"
            yaml '''
                apiVersion: v1
                kind: Pod
                metadata:
                  namespace: devops-tools
                  labels:
                    job: bootvar-build-pod
                spec:
                  containers:
                  - name: svs-python
                    image: python:3.10.7-alpine
                    tty: true
                    command: ['cat']
                '''
        }
    }
    stages {
        stage("add dependencies"){
            steps{
                container("svs-python"){
                    sh "apk add scons pkgconf gcc g++ libx11-dev libxcursor-dev libxinerama-dev libxi-dev libxrandr-dev mesa-dev libexecinfo-dev eudev-dev alsa-lib-dev pulseaudio-dev"
                }
            }
        } 
        stage("First") {
            steps {
                container("svs-python") {
                    sh "python3 test/test_all.py"
                }
            }
        }
    }
}
