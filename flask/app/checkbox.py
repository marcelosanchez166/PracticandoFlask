from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

@app.route("/")
def index():
    return redirect(url_for('submit'))

@app.route('/submit', methods=['POST', 'GET'])
def submit():
    if request.method == "POST":
        opciones = request.form.getlist('opciones')  # Obtiene una lista con todos los valores seleccionados
        print(type(opciones),opciones, "Tipo de dato que se obtiene con el getlist")
        return render_template("checkboxesmismonombre.html", opciones=opciones)
    return render_template("checkboxesmismonombre.html")


# @app.route('/prueba', methods=['POST', 'GET'])
# def prueba():
#     if request.method == 'POST':
#         # Diccionario donde se almacenará el resultado
#         diccionario_horarios = {}
#         #obtener la lista del dia lunes 
#         lunes = request.form.getlist('lunes')
#         # Asignar los valores de la lista al diccionario
#         dia, hora_inicio, hora_fin = lunes
#         print(dia)
#         print(hora_inicio)
#         print(hora_fin)
#         diccionario_horarios[dia] = {"hora_inicio": hora_inicio, "hora_fin": hora_fin}
#         print(diccionario_horarios)
#         martes = request.form.getlist('martes')
#         dia, hora_inicio, hora_fin = martes
#         print(martes[0], "Martes de la posicion cero ")
#         diccionario_horarios[dia] = {"hora_inicio": hora_inicio, "hora_fin": hora_fin}
#         print(diccionario_horarios, "Diccionarios con dos dias ")
#         miercoles = request.form.getlist('miercoles')
#         jueves = request.form.getlist('jueves')
#         viernes = request.form.getlist('viernes')
#         return render_template('pruebas.html', data=diccionario_horarios)
#     return render_template('pruebas.html')

@app.route('/prueba', methods=['POST', 'GET'])
def prueba():
    if request.method == 'POST':
        diccionario_horarios = {}
        for dia in ['lunes', 'martes', 'miercoles', 'jueves', 'viernes']:
            #Para obtener los datos de los dias debo usar un request.form.get() porque si uso request.form['dias'] esta especificando el valor obtenido
            if request.form.get(f'dias[{dia}]'):#el objeto dias viene de la plantilla hmtl del name name="dias[lunes]" del select y se le pasa la varible dia que es la que recorre la lista de los dias para ver si el dia que el usuario manda esta en la lista que tenemos
                hora_inicio = request.form.get(f'horas[{dia}][inicio]')#Si el dia esta en la lista de dias, procedemos a guardar el diccionario de la hora de inicio correspondiente al dia en la variable correspondiente
                hora_fin = request.form.get(f'horas[{dia}][fin]')#Si el dia esta en la lista de dias, procedemos a guardar el diccionario de la hora de inicio correspondiente al dia en la variable correspondiente
                diccionario_horarios[dia] = {#Una vez guardados el dia, la hora_inicio y la hora_fin en las variables correspondiente creamos un diccionario donde la clave principal seria el dia, y tendria como valor "hora_inicio": hora_inicio, "hora_fin": hora_fin
                    "hora_inicio": hora_inicio,
                    "hora_fin": hora_fin
                }
        return render_template('pruebas.html', diccionario_horarios=diccionario_horarios)
    else:
        return render_template('pruebas.html')


if __name__ == "__main__":
    app.run(debug=True)