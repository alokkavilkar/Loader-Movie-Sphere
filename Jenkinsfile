def imageName = "alokkavilkar/unit-test"
node('worker'){
 	stage('Checkout'){
	 checkout scm
	}

	def image = docker.build("${imageName}", "-f Dockerfile.test .")
	stage("Unit test"){
		image.inside{
			sh 'python test_loader.py'
		}
	}

	stage("Quality Test"){
		// sh "docker build -t ${imageName}-lint -f Dockerfile.lint ."

		// sh "docker run --rm ${imageName}-lint"

		image.inside{
			sh 'pylint loader.py'
		}
	}

}
