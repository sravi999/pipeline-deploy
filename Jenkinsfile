pipeline {
  agent any
  environment {
  docker_crds = credentials("DockerCreds")
  docker_image = "$docker_crds_USR/flask"
  dockerImage=""
  }
  stages{
    stage("Build") {
     dockerImage = docker.build docker_image
    }
    stage("Push") {
     dockerImage.push("$BUILD_NUMBER")
  }
}
}
