node('worker'){
 	stage('Checkout'){
	 checkout scm
	}

	stage("Unit test"){
		sh "docker build -t ${imageName}-test -f Dockerfile.test ."

		sh "docker run --rm ${imageName}-test"
	}

}
