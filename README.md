# HTML_Program_Libreria

![Portada](./screenshots/Fondo-removebg-preview.png)

Creación de aplicación dinámica en python flask donde se trabajara con una [plantilla](https://plantillashtmlgratis.com/categoria-plantillas/plantillas-html/page/115/) de html5 gratuita.

A partir de esta plantilla se creará una plantilla base.html.


1. Primero se ha creado un entorno virtual desde el que se va a trabajar en el programa de esta página.

![Entorno virtual](./screenshots/envt.png) 

2. Para poder crear la aplicación he utilizado una [plantilla de HTML gratuita](https://plantillashtmlgratis.com/todas-las-plantillas/plantilla/plantilla-web-gratuita-dark-theme/) haciendo uso únicamente del index.html y del css que tenía prederteminado, ambos serán modificados.

3. Con esta plantilla [index.html](https://github.com/belennazareth/HTML_Program_Libreria/blob/main/templates/index.html) se ha creado la [base](https://github.com/belennazareth/HTML_Program_Libreria/blob/main/templates/base.html) que usaremos para la creación del resto de partes de la aplicación.

4. Dentro del entorno virtual se ejecuta la [app.py](https://github.com/belennazareth/HTML_Program_Libreria/blob/main/app.py) usando la última versión de flask.

![Flask](./screenshots/codeflask.png)

5. Lo siguiente es crear un fichero con los paquetes usados en la instalación de flask, para ello se ha usado este comando:

        `pip freeze > requirements.txt`

6. A continuación, podemos ver que el fichero [requirements](https://github.com/belennazareth/HTML_Program_Libreria/blob/main/requirements.txt) se ha creado correctamente:

![Requirements](./screenshots/requirements.png)

7. Una vez preparado lo anterior se ha montado el [app.py](https://github.com/belennazareth/HTML_Program_Libreria/blob/main/app.py) donde se irán definiendo las rutas, además del [base.html](https://github.com/belennazareth/HTML_Program_Libreria/blob/main/templates/base.html), que hará de plantilla para el resto de recursos usando bloques.

        `{%block xxxxxx%}{%endblock%}`

8. Se ha creado un fichero html para el inicio, llamado [biblioteca](https://github.com/belennazareth/HTML_Program_Libreria/blob/main/templates/biblioteca.html), donde se muestran los títulos de los libros como enlace.

![Inicio](./screenshots/inicio.png)

9. Al entrar en uno de los títulos de la página principal se abrirá una página con los datos sobre ese libro, para esto se ha hecho un fichero [libro.html](https://github.com/belennazareth/HTML_Program_Libreria/blob/main/templates/libro.html) donde se ha realizado todo el código necesario.

![Libro](./screenshots/libro.png)

10. En caso de que el ISBN no exista devolverá un error 404, el cual esta añadido en el [app.py](https://github.com/belennazareth/HTML_Program_Libreria/blob/main/app.py) como un except.

![error404](./screenshots/error.png)

11. En caso de que el campo status sea MEAP devolverá un mensaje donde se indique que el libro aún no se ha publicado.

![MEAP](./screenshots/MEAP.png)

12. En los detalles del libro aparecen las categorías como enlaces donde se mostrarán en una página ['categoría'](https://github.com/belennazareth/HTML_Program_Libreria/blob/main/templates/categoria.html) los libros que pertenezcan a la misma con el título de esta.

![Enlace](./screenshots/enlace.png)
![categoría](./screenshots/categoria.png)


## Acceso a la página


Para poder aceder a esta página podemos hacerlo a través de este [enlace](https://html-flask-libreria.herokuapp.com/).
Se ha usado HEROKU, una plataforma de servicios en la nube que nos va a permitir manejar servidores y configurarlos.

Debido al corte por parte de HEROKU hacia el uso directo de repositorios de GITHUB he usado esta [guía](https://www.josedomingo.org/pledin/2022/04/heroku-cli/) de despliegue en Heroku usando su CLI 

![Fav](./screenshots/indexfav.png)
