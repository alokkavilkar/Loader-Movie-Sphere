def imageName = "alokkavilkar/unit-test"
node('worker'){
 	stage('Checkout'){
	 checkout scm
	}

	stage("Unit test"){
		docker.build("${imageName}", "-f Dockerfile.test .")
		sh "docker run --rm ${imageName}"
	}

	stage("Security Test"){
		sh "docker build -t ${imageName}-lint -f Dockerfile.lint ."

		sh "docker run --rm ${imageName}-lint"
	}

}
