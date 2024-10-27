pipeline {
    agent any 

    stages {
        stage('Build') {
            steps {
                // Aquí va el comando para construir tu proyecto
                echo 'Construyendo el proyecto...'
                // Por ejemplo: sh 'python calculator_test.py'
            }
        }
        stage('Publish') {
            steps {
                // Agregar pasos para empujar cambios a Git
                script {
                    def remote = 'https://github.com/tu_usuario/nombre_repositorio.git'
                    def branch = 'main' // o la rama que desees
                    def credentialsId = 'tu-credencial-id' // ID de las credenciales en Jenkins

                    // Comandos para hacer push a Git
                    sh """
                    git config user.name 'tu_nombre'
                    git config user.email 'tu_email@example.com'
                    git add .
                    git commit -m 'Actualizaciones automáticas de Jenkins'
                    git push ${remote} ${branch}
                    """
                }
            }
        }
    }

    // Opcional: Agregar el bloque de post para manejar notificaciones o limpieza
    post {
        success {
            echo 'Construcción exitosa.'
        }
        failure {
            echo 'La construcción falló.'
        }
    }
}
