def imageName = "alokkavilkar/unit-test"
def buildName = "alokkavilkar/loader"
// def registry = "public.ecr.aws/l9r7x6m1"
def private_registry = "058264318784.dkr.ecr.us-east-1.amazonaws.com"

def commitID() {
	sh 'git rev-parse HEAD > .git/commitID'
	def commitID = readFile('.git/commitID').trim()
	sh 'rm .git/commitID'
	commitID
}

node('worker'){

	withCredentials([string(credentialsId: 'aws-access-key', variable: 'AWS_ACCESS_KEY_ID'),string(credentialsId: 'aws-secret-key', variable: 'AWS_SECRET_ACCESS_KEY'), string(credentialsId: 'aws-ecr-key', variable: 'AWS_ECR_KEY'), string(credentialsId: 'aws-ecr-pass-private', variable: 'AWS_ECR_PRIVATE')]) {

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

		stage("Push")
		{
			sh "echo ${AWS_ECR_PRIVATE} | docker login --username AWS --password-stdin ${private_registry}"
			sh "echo Login success."
			docker.image(imageName).push(commitID)


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
