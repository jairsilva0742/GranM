from flask import Flask, request, render_template
import main

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('form.html')
@app.route('/analisis')
def home1():
    
    return render_template('formAnalisis.html')

@app.route('/procesar_ecuacion', methods=['POST'])
def submit():
    if request.form['maxi']=='minimizar':
        m=True
    else:
        m=False
    entrada1_1 = request.form['entrada1_1']
    entrada1_2 = request.form['entrada1_2']
    entrada2_1 = request.form['entrada2_1']
    entrada2_2 = request.form['entrada2_2']
    resultado2= request.form['resultado2']
    entrada3_1 = request.form['entrada3_1']
    entrada3_2 = request.form['entrada3_2']
    resultado3= request.form['resultado3']
    entrada4_1 = request.form['entrada4_1']
    entrada4_2 = request.form['entrada4_2']
    resultado4= request.form['resultado4']
    if request.form['opcion2']=='opcion2_1':
        c=0
    if request.form['opcion2']=='opcion2_2':
        c=-1
    if request.form['opcion2']=='opcion2_3':
        c=1
    else:
        print("fuera")
    if request.form['opcion3']=='opcion3_1':
        d=0
    if request.form['opcion3']=='opcion3_2':
        d=-1
    if request.form['opcion3']=='opcion3_3':
        d=1
    else:
        print("fuera")
    if request.form['opcion4']=='opcion4_1':
        e=0
    if request.form['opcion4']=='opcion4_2':
        e=-1
    if request.form['opcion4']=='opcion4_3':
        e=1
    else:
        print("fuera")
    a,b,tablaInicial,soluciones,tabla2,tabla3,tabla4,tabla5,solutions,sombra,solutions2=main.granM(c,d,e,m,float(entrada1_1),float(entrada1_2),float(entrada2_1),float(entrada2_2),float(resultado2),float(entrada3_1),float(entrada3_2),float(resultado3),float(entrada4_1),float(entrada4_2),float(resultado4))
    return render_template('formulario.html',a=a,b=b,matriz=tablaInicial,soluciones=soluciones,matriz2=tabla2,matriz3=tabla3,matriz4=tabla4,matriz5=tabla5,solutions=solutions,sombra=sombra,solutions2=solutions2)
    #return f'{tablaInicial} Z: {a}, Valor: {b}'

if __name__ == '__main__':
    app.run(debug=True)