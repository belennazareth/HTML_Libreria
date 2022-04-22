# HTML_Program_Libreria

Creación de aplicación dinámica en python flask donde se trabajara con una [plantilla](https://plantillashtmlgratis.com/categoria-plantillas/plantillas-html/page/115/) de html5 gratuita.

A partir de esta plantilla se creará una plantilla base.html.


1. Primero se ha creado un entorno virtual desde el que se va a trabajar en el programa de esta página.

2. Para poder crear la aplicación he utilizado una [plantilla de HTML gratuita](https://plantillashtmlgratis.com/todas-las-plantillas/plantilla/plantilla-web-gratuita-dark-theme/) haciendo uso únicamente del index.html y del css que tenía prederteminado, ambos serán modificados.

3. Con esta plantilla [index.html](https://github.com/belennazareth/HTML_Program_Libreria/blob/main/templates/index.html) se ha creado la [base](https://github.com/belennazareth/HTML_Program_Libreria/blob/main/templates/base.html) que usaremos para la creación del resto de partes de la aplicación.

4. Dentro del entorno virtual se ejecuta la [app.py](https://github.com/belennazareth/HTML_Program_Libreria/blob/main/app.py) usando la última versión de flask.

5. Lo siguiente es crear un fichero con los paquetes usados en la instalación de flask, para ello se ha usado este comando:

        `pip freeze > requirements.txt`

6. A continuación, podemos ver que el fichero se ha creado correctamente:

7. Una vez preparado lo anterior se ha montado el [app.py](https://github.com/belennazareth/HTML_Program_Libreria/blob/main/app.py) donde se irán definiendo las rutas, además del [base.html](https://github.com/belennazareth/HTML_Program_Libreria/blob/main/templates/base.html), que hará de plantilla para el resto de recursos usando bloques.

        `{%block xxxxxx%}{%endblock%}`

8. Se ha creado un fichero html para el inicio, llamado [biblioteca](https://github.com/belennazareth/HTML_Program_Libreria/blob/main/templates/biblioteca.html), donde se muestran los títulos de los libros como enlace: