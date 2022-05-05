from flask import Flask, request
from flask import jsonify
from flask_cors import CORS
import prediction


def create_app():
    app = Flask(__name__)
    return app


app = create_app()
CORS(app)


@app.route('/api/grupo-preguntas', methods=['POST'])
def grupo_preguntas():
    json_data = request.json
    formResponses = json_data["responses"]
    return jsonify(formResponses)


@app.route('/api/hechos', methods=['GET'])
def facts():
    facts = [{'key': 'hola'}]
    return jsonify(facts)


@app.route('/test', methods=['POST'])
def test():
    json_data = request.json
    age = int(json_data["age"])
    job = json_data["job"]
    marital = 'married'
    education = 'primary'
    default = 'no'
    balance = 1787
    housing = 'no'
    loan = 'no'
    contact = 'cellular'
    day = 19
    month = 'oct'
    duration = 79
    campaign = 1
    pdays = -1
    previous = 0
    poutcome = 'unknown'

    prediccion = prediction.predecirNuevoCliente(age, job, marital, education, default,
                                                 balance, housing, loan, contact, day,
                                                 month, duration, campaign, pdays, previous, poutcome)
    if prediccion == 1:
        return jsonify({'res': 'Credito Aprobado'})

    return jsonify({'res': 'Credito no Aprobado'})


if __name__ == '__main__':
    app.run(debug=True)
