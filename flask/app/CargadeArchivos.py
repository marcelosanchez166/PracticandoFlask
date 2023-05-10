# Carga de archivos
# Ah, sí, el viejo problema de la subida de archivos. La idea básica de la subida de archivos es en realidad bastante simple. Básicamente funciona así:

# Una etiqueta <form> se marca con enctype=multipart/form-data y se coloca un <input type=file> en ese formulario.

# La aplicación accede al archivo desde el diccionario files del objeto de la petición.

# utiliza el método save() del archivo para guardar el archivo de forma permanente en algún lugar del sistema de archivos.

# Una gentil introducción

# Comencemos con una aplicación muy básica que sube un archivo a una carpeta de subida específica y muestra un archivo al usuario. Veamos el código de arranque de nuestra aplicación:
import os
from flask import Flask, flash, request, redirect, url_for
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = '/path/to/the/uploads'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Así que primero necesitamos un par de importaciones. La mayoría deberían ser sencillas, la werkzeug.secure_filename() se explica un poco más tarde.
# El UPLOAD_FOLDER es donde almacenaremos los archivos subidos y el ALLOWED_EXTENSIONS es el conjunto de extensiones de archivo permitidas.

# ¿Por qué limitamos las extensiones permitidas? Probablemente no quiera que sus usuarios puedan subir todo allí si el servidor está enviando directamente los datos al cliente. 
# De este modo, puede asegurarse de que los usuarios no puedan subir archivos HTML que puedan causar problemas de XSS (véase Secuencia de comandos en sitios cruzados (XSS)). 
# También asegúrese de no permitir archivos .php si el servidor los ejecuta, pero ¿quién tiene PHP instalado en su servidor, verdad? :)

# A continuación las funciones que comprueban si una extensión es válida y que suben el archivo y redirigen al usuario a la URL del archivo subido:
def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('download_file', name=filename))
    # return '''
    # <!doctype html>
    # <title>Upload new File</title>
    # <h1>Upload new File</h1>
    # <form method=post enctype=multipart/form-data>
    #   <input type=file name=file>
    #   <input type=submit value=Upload>
    # </form>