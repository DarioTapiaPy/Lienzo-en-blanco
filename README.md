## Lienzo-en-blanco
Repositorio para aprender y practicar git / github

# Primero que todo
Antes que nada debemos verificar si tenemos git instalado, para eso vamos a utilizar el siguiente comando:

*git --version*

Este debería decirnos que versión de git tenemos instalado en nuestro computador.

# Segundo paso
iniciar sesión con nuestra cuenta de GitHub en nuestro Git de escritorio, para eso, vamos a tener que hacer una serie de comandos para añadir un nombre de usuario y un correo

*git config --global user.name "nombredeejemplo777"*
*git config --global user.email correo.deejemplo@gmail.com*

Estos comandos debieron haber agregado un nombre de usuario y un correo que sirven para identificar a qué usuario hizo tal commit o rama. Para verificar que esté todo correcto podemos ejecutar el siguiente comando que muestra todas las configuraciones:

*git config --list*

# Dos formas de seguir
Podemos crear nuestra carpeta local e inicializar nuestro repositorio de manera manual, creando nosotros el readme y el .gitignore pero en nuestro caso no es necesario. Nosotros haremos uso de la página web de GitHub para crear un repositorio desde ahí, inicializarlo con un readme, con el .gitignore que sea correspondiente e incluso añadir colaboradores en caso de hacer un trabajo en grupo, para eso vamos a entrar en nuestro repositorio creado y clickear donde dice **<> CODE**, luego vamos a copiar el link abajo de donde dice Local, Clone y HTTPS, teniendo este link podemos pasar al siguiente paso

# Hacer un clone
Para trabajar de manera local en nuestro repositorio debemos clonar el que está subido al GitHub, para ello vamos a ejecutar el siguiente comando donde queramos que se clone nuestro repositorio, por ejemplo si quisiera que fuera en el escritorio habría que irse al escritorio, hacer click derecho, tocar el que dice **Open Git Bash Here** y ahí ejecutar la siguiente línea de comando con el link que sacamos el paso anterior

*git clone https://github.com/usuario/repositorio*

Con esto ya podriamos entrar a la carpeta y seguir en Visual Studio Code, podemos hacer un cd nombre_de_repositorio/ y luego un code . para abrir el VSC

# Empezar a trabajar en Git & GitHub

Cada cambio que hagamos dentro de esta carpeta, como por ejemplo: Crear un archivo .py, debe venir acompañado de un commit, los commits son formas de versionar nuestro repositorio. Imagina que tenemos una calculadora, pensemos que queremos ir de a poco agregando funciones a mi calculadora, entonces creo un archivo de python que sea main.py (que sería mi calculadora final) y otro archivo de python que se llame utils.py (donde irán mis funciones), empezaremos creando la función de una suma y llamaremos la librería utils con nuestra función suma(), en el main tenemos dos variables de tipo entero que son inputs que hará el usuario y hasta ahí tenemos todo esto que hemos hecho en un solo commit. No sé si me entiendo pero pensemos que esta es nuestra calculadora versión 1.0 y nuestro primer commit (sin contar el inicial).
Lo que sigue es ejecutar un comando que te mostrará el estado de tu carpeta, revisa si hay archivos que no están commiteados, onda, que son temporales

*git status*

Luego de ver todos los archivos creados y que esté todo correcto vamos a crear un commit, para ello vamos a ejecutar el siguiente comando:

*git add "Nombre del archivo"*

o
*git add .*

La diferencia entre estos dos es que cuando escribes el nombre del archivo solo subirás ese archivo y si pones el punto es para que se suba todo lo que está en la carpeta, ambos son muy útiles pero si tu carpeta es limpia y sabes que solo tienes archivos importantes para tu repositorio recomiendo usar el *git add .*

Luego de que estén añadidos debemos hacer un Commit que evidencie nuestros cambios, vamos a ejecutar el siguiente comando:

*git commit -m "Explicar brevemente los cambios hechos"*

la "-m" especifica que lo que vamos a escribir siguiente es un mensaje, sin la "-m" nos abriría un editor de texto, no recuerdo si vim o nano pero es algo muy molesto. Luego vamos a entre comillas escribir el cambio que hicimos a nuestro repositorio, por ejemplo yo pondre: "Creación del main y la función de suma"

Cuando hayamos hecho el commit vamos a ejecutar nuevamente *git status* si dice nothing to commit, o sea, que no hay nada que agregar (ya agregamos todo) podemos continuar

# Pero mis cambios no se ven reflejados en GitHub
Para subir los cambios al repositorio que está en línea y verlo debemos simplemente hacer un push, esto se hace desde la rama que queremos hacer el push, en nuestro caso no hemos creado ninguna así que subiremos main que debería ser la que tiene todo, el readme, el .gitignore, el utils que creamos y el main que es nuestra calculadora

*git push*

o si queremos subir una rama

*git push origin nombre_rama*
