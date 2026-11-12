from flask import Flask, render_template , request 
from google import genai

app = Flask(__name__)

cliente = genai.Client(api_key="KEY")

@app.route('/', methods=['GET', 'POST'])
def inicio():
    respuesta = None
    if request.method == 'POST':
        pregunta = request.form['pregunta']
        resultado = cliente.models.generate_content(
            model="gemini-3.5-flash-lite",
            contents=pregunta
        )
        respuesta = resultado.text
    return render_template('index.html', respuesta=respuesta)
    



app.run(debug=True)
