def imageName = "alokkavilkar/unit-test"
node('worker'){
 	stage('Checkout'){
	 checkout scm
	}

	stage("Unit test"){
		def image = docker.build("${imageName}", "-f Dockerfile.test .")
		image.inside(
			sh "python test_loader.py"
		)
	}

	stage("Security Test"){
		// sh "docker build -t ${imageName}-lint -f Dockerfile.lint ."

		// sh "docker run --rm ${imageName}-lint"

		image.inside(
			sh "pylint loader.py"
		)
	}

}
