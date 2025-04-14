from flask import Flask, render_template, request
from experta import *

app = Flask(__name__)

class Sintomas(Fact):
    pass

class SistemaSAMU(KnowledgeEngine):

    @Rule(Sintomas(inconsciente=True, nao_respirando=True))
    def parada_cardiaca(self):
        self.diagnostico = "Parada cardiorrespiratória"
        self.acao = "Aplicar RCP imediatamente."
        self.explicacao.append("Paciente inconsciente e não respirando → Regra de Parada Cardiorrespiratória ativada.")

    @Rule(Sintomas(sangramento_intenso=True))
    def hemorragia(self):
        self.diagnostico = "Hemorragia"
        self.acao = "Fazer compressão e elevar o membro afetado."
        self.explicacao.append("Paciente com sangramento intenso → Regra de Hemorragia ativada.")

    @Rule(Sintomas(fratura=True))
    def fratura(self):
        self.diagnostico = "Fratura"
        self.acao = "Imobilizar o local da fratura."
        self.explicacao.append("Paciente com fratura aparente → Regra de Fratura ativada.")

    def __init__(self):
        super().__init__()
        self.diagnostico = "Não identificado"
        self.acao = "Aguardar orientação médica."
        self.explicacao = [] 


@app.route("/", methods=["GET", "POST"])
def index():
    resultado = None

    if request.method == "POST":
        sintomas = {
            "inconsciente": 'inconsciente' in request.form,
            "nao_respirando": 'nao_respirando' in request.form,
            "sangramento_intenso": 'sangramento_intenso' in request.form,
            "fratura": 'fratura' in request.form
        }

        engine = SistemaSAMU()
        engine.reset()
        engine.declare(Sintomas(**sintomas))
        engine.run()

        resultado = {
        "diagnostico": engine.diagnostico,
        "acao": engine.acao,
        "explicacao": engine.explicacao
        }


    return render_template("index.html", resultado=resultado)

if __name__ == "__main__":
     app.run(debug=True, port=5001)
