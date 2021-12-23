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
        dockerImage = docker.build docker_image
      }
    }
    stage("Push") {
     steps {
       dockerImage.push("$BUILD_NUMBER")
     }
  }
}
}
