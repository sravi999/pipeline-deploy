pipeline {
  agent any
  environment {
  docker_crds = credentials("DockerCreds")
  docker_image = "$docker_crds_USR/flask"
  dockerImage=""
  }
  stages{
    stage("Build") {
      steps {
        script {
          dockerImage = docker.build docker_image
        }
      }
    }
    stage("Push") {
     steps {
       script {
         dockerImage.push("$BUILD_NUMBER")
       }
     }
    }
    stage("Run") {
     steps {
       script {
         dockerImage.run("-p 0.0.0.0:5000:80")
       }
     }
    }
}
}
