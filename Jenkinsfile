node {

   stage('Clone Repository') {
        // Get some code from a GitHub repository
        git 'https://github.com/ajarv/spring-boot-app'
    
   }
   stage('Build Maven Image') {
        docker.build("maven-build")
   }
   
   stage('Run Maven Container') {
       
        //Run maven image
        sh "docker run --rm --name maven-build-container maven-build"
   }
   
   stage('Deploy Spring Boot Application') {
        
        sh "docker run  --rm --name java-deploy-container --volumes-from maven-build-container -d -p 9090:8080 summer-sdge/gs-spring-boot-docker:3.3.2"
   }

}
