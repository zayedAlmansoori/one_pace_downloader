pipeline {
  agent any
  stages {
    stage('Checkout Code') {
      steps {
        git(url: 'https://github.com/zayedAlmansoori/one_pace_downloader.git', branch: 'master')
      }
    }

    stage('Log') {
      steps {
        sh 'ls -la'
      }
    }

  }
}