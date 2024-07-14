def imageName = "alokkavilkar/unit-test"
def buildName = "alokkavilkar/loader"
node('worker'){

	withCredentials([string(credentialsId: 'aws-access-key', variable: 'AWS_ACCESS_KEY_ID'),string(credentialsId: 'aws-secret-key', variable: 'AWS_SECRET_ACCESS_KEY')]) {

		env.alok = 'Alok'

		stage('Check All Environment Variables') {
			// Use a shell command to print all environment variables
			sh 'printenv | grep alok'
    	}

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
			sh "docker build -t ${buildName} -f Dockerfile ."
			sh """
                docker run --rm \
                -e AWS_ACCESS_KEY_ID=${AWS_ACCESS_KEY_ID} \
                -e AWS_SECRET_ACCESS_KEY=${AWS_SECRET_ACCESS_KEY} \
                -e AWS_REGION=${env.AWS_REGION} \
                ${buildName}
            """
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
}
