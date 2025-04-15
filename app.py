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

    @Rule(Sintomas(dor_peito=True))
    def dor_no_peito(self):
        self.diagnostico = "Dor no peito"
        self.acao = "Chamar o SAMU imediatamente e monitorar o paciente."
        self.explicacao.append("Paciente com dor no peito → Regra de Dor no Peito ativada.")

    @Rule(Sintomas(dificuldade_falar=True))
    def dificuldade_para_falar(self):
        self.diagnostico = "Possível AVC"
        self.acao = "Chamar o SAMU imediatamente e manter o paciente calmo."
        self.explicacao.append("Paciente com dificuldade para falar → Regra de Possível AVC ativada.")

    @Rule(Sintomas(convulsao=True))
    def convulsao(self):
        self.diagnostico = "Convulsão"
        self.acao = "Proteger a cabeça do paciente e evitar que ele se machuque."
        self.explicacao.append("Paciente com convulsão → Regra de Convulsão ativada.")

    @Rule(Sintomas(queimadura_grave=True))
    def queimadura_grave(self):
        self.diagnostico = "Queimadura Grave"
        self.acao = "Resfriar a área com água corrente e cobrir com um pano limpo. Não aplicar pomadas."
        self.explicacao.append("Paciente com queimadura grave → Regra de Queimadura Grave ativada.")

    @Rule(Sintomas(envenenamento=True))
    def envenenamento(self):
        self.diagnostico = "Suspeita de Envenenamento"
        self.acao = "Chamar o SAMU imediatamente e informar o possível agente tóxico."
        self.explicacao.append("Paciente com suspeita de envenenamento → Regra de Envenenamento ativada.")

    @Rule(Sintomas(asma=True))
    def crise_de_asma(self):
        self.diagnostico = "Crise de Asma"
        self.acao = "Ajudar o paciente a usar o inalador e mantê-lo calmo."
        self.explicacao.append("Paciente com crise de asma → Regra de Crise de Asma ativada.")

    @Rule(Sintomas(hipotermia=True))
    def hipotermia(self):
        self.diagnostico = "Hipotermia"
        self.acao = "Aqueça o paciente gradualmente e chame o SAMU."
        self.explicacao.append("Paciente com sinais de hipotermia → Regra de Hipotermia ativada.")

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
            "fratura": 'fratura' in request.form,
            "dor_peito": 'dor_peito' in request.form,
            "dificuldade_falar": 'dificuldade_falar' in request.form,
            "convulsao": 'convulsao' in request.form,
            "queimadura_grave": 'queimadura_grave' in request.form,
            "envenenamento": 'envenenamento' in request.form,
            "asma": 'asma' in request.form,
            "hipotermia": 'hipotermia' in request.form
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