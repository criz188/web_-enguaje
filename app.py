from flask import Flask, render_template, request
import os

app = Flask(__name__)

# Define tus conjuntos de palabras aquí
palabras_sustantivos = {
    "casa", "persona", "animal", "automóvil", "gobierno", "hogar",
    "tarde", "compromisos", "proyecto", "asunto", "reunión", "estrategia",
    "ejemplo", "proceso", "resultado", "informe", "propuesta", "colaboración",
    "implementación", "desarrollo"
}
palabras_verbos = {
    "ser", "estar", "hacer", "decir", "tener", "encontrarse",
    "escribir", "invitar", "compartir", "aceptar", "acordar",
    "realizar", "disfrutar", "analizar", "comprender", "estudiar",
    "solicitar", "notificar", "confirmar", "proporcionar", "agradecer"
}
palabras_adjetivos = {
    "grande", "pequeño", "importante", "rápido", "lento", "tranquilo",
    "eficiente", "satisfactorio", "creativo", "adaptable", "cordial"
}
palabras_interjecciones = {
    "¡eh!", "¡oh!", "¡wow!", "¡bah!", "obvio", "finde", "tipo", "chévere",
    "bacán", "genial"
}
palabras_informales = {
    "súper", "charlar", "planes", "rol", "guay", "movida", "está bien",
    "joder", "así", "pana", "bro", "amigo", "Hola", "Chido", "Genial",
    "Cosa", "Tío", "Tía", "Qué onda", "Vale", "Bicho", "Güey",
    "Locura", "Broma", "Chamba", "Jato", "Pelea", "Flipar"
}
palabras_groseras = {
    "pinche", "chelas", "jodido", "pedo", "güey", "chingados",
    "madre", "desmadre", "huevo", "mierda", "coño", "pendejo",
    "cabrón", "hijo de puta", "joder", "culero", "pendejada", 
    "mamar", "hueva", "picha", "chafa", "hijo de la chingada", 
    "idiota"
}

def detectar_formal(texto):
    palabras = texto.split()
    return [palabra for palabra in palabras if palabra in palabras_sustantivos or palabra in palabras_verbos or palabra in palabras_adjetivos]

def detectar_informal(texto):
    palabras = texto.split()
    return [palabra for palabra in palabras if palabra in palabras_interjecciones or palabra in palabras_informales]

def detectar_grosero(texto):
    palabras = texto.split()
    return [palabra for palabra in palabras if palabra in palabras_groseras]

def calcular_porcentaje_lenguaje(texto):
    palabras = texto.split()
    total_palabras = len(palabras)
    if total_palabras == 0:
        return (0, 0, 0)

    num_formales = len(detectar_formal(texto))
    num_informales = len(detectar_informal(texto))
    num_groseras = len(detectar_grosero(texto))

    porcentaje_formal = (num_formales / total_palabras) * 100
    porcentaje_informal = (num_informales / total_palabras) * 100
    porcentaje_groserias = (num_groseras / total_palabras) * 100

    return porcentaje_formal, porcentaje_informal, porcentaje_groserias

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Verifica si se ha subido un archivo
        if 'file' not in request.files:
            return "No se ha subido ningún archivo."
        
        file = request.files['file']
        
        if file.filename == '':
            return "No se ha seleccionado ningún archivo."
        
        if file:
            texto = file.read().decode('utf-8')
            porcentaje_formal, porcentaje_informal, porcentaje_groserias = calcular_porcentaje_lenguaje(texto)
            return render_template('index.html', 
                                   porcentaje_formal=porcentaje_formal,
                                   porcentaje_informal=porcentaje_informal,
                                   porcentaje_groserias=porcentaje_groserias,
                                   texto=texto)
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)