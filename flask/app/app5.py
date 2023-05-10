# Carga de archivos
# Puedes manejar los archivos subidos con Flask fácilmente. Sólo asegúrese de no olvidar establecer el atributo enctype="multipart/form-data" en su formulario HTML, 
# de lo contrario el navegador no transmitirá sus archivos en absoluto.

# Los archivos subidos se almacenan en la memoria o en una ubicación temporal en el sistema de archivos. Puede acceder a esos archivos mirando el atributo files del objeto request. 
# Cada archivo subido se almacena en ese diccionario. Se comporta como un objeto file estándar de Python, pero también tiene un método save() que permite almacenar ese fichero 
# en el sistema de ficheros del servidor. Aquí hay un ejemplo sencillo que muestra cómo funciona:


from flask import request, Flask

app=Flask(__name__)

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['the_file']
        f.save('/var/www/uploads/uploaded_file.txt')
        print(f)
    return "subir archivo"


# Si quieres saber cómo se nombró el archivo en el cliente antes de subirlo a tu aplicación, puedes acceder al atributo filename. Sin embargo, 
# ten en cuenta que este valor puede ser falsificado, así que nunca confíes en él. Si quieres utilizar el nombre de archivo del cliente para almacenar el archivo en el servidor, 
# pásalo a través de la función secure_filename() que te proporciona Werkzeug:

from werkzeug.utils import secure_filename

@app.route('/uploads', methods=['GET', 'POST'])
def upload_files():
    if request.method == 'POST':
        file = request.files['the_file']
        file.save(f"/var/www/uploads/{secure_filename(file.filename)}")
        print(file)
    return "Carga de archivo"
    ...