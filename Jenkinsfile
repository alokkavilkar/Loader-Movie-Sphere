def imageName = "alokkavilkar/unit-test"
node('worker'){
 	stage('Checkout'){
	 checkout scm
	}

	def image = docker.build("${imageName}", "-f Dockerfile.test .")
	stage("pre-integration tests")
	{
		parallel(
			'Quality Tests': {
				image.inside{
					sh 'pylint loader.py'
				}
			},

			'Unit Test' : {
				image.inside{
					sh 'python test_loader.py '
				}
			},

			'Security Test' :{
				sh "docker build -t ${imageName}-security -f Dockerfile.security ."

				sh "docker run --rm ${imageName}-security"
			}
		)
	}

	stage("Build"){
		sh "docker build -t alokkavilkar/loader-micro -f Dockerfile ."
		
	}
	// stage("Unit test"){
	// 	image.inside{
	// 		sh 'python test_loader.py'
	// 	}
	// }

	// stage("Quality Test"){
	// 	// sh "docker build -t ${imageName}-lint -f Dockerfile.lint ."

	// 	// sh "docker run --rm ${imageName}-lint"

	// 	image.inside{
	// 		sh 'pylint loader.py'
	// 	}
	// }

	// stage("Security Test"){
	// 	sh "docker build -t ${imageName}-security -f Dockerfile.security ."
	// 	sh "docker run --rm ${imageName}-security"
	// }

}
