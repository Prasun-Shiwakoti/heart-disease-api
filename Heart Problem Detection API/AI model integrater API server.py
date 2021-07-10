import pickle
import numpy as np
from sklearn.preprocessing import StandardScaler


from flask import Flask, Response, jsonify, request

app = Flask(__name__)


model = pickle.load(open("backend/finalized_model.sav", "rb"))
scaler = StandardScaler()

mean_values = np.array([0.68211921,   0.96357616, 131.60264901, 246.5,
                        149.56953642,   0.32781457,   1.04304636,   1.39735099,
                        0.71854305,   2.31456954])

std_values = np.array([ 0.46642574,  1.03204364, 17.56339423, 51.75348866, 22.90352725,
        0.47019596,  1.16145229,  0.61627398,  1.00674826,  0.61302554])


def get_prediction(data):
    data = np.array([float(i) for i in data.values()])
    data = (data - mean_values) / std_values

    data = data.reshape(1, -1)
    percentage = (model.predict_proba(data).flatten()[0])*100

    return round(percentage, 2)


@app.route('/predict', methods=['POST'])
def region():
    json_data = request.json
    print("dadada")
    print(json_data)
    pred = get_prediction(json_data)
    response = {}
    if pred > 0.75:
        response['status'] = "success"
        response['value'] = str(pred)
        response['vernarabilty'] = True
    else:
        response['status'] = "success"
        response['value'] = str(pred)
        response['vernarabilty'] = False

    return jsonify(response)


app.run(host='localhost', port=5001)

# app.run(host='0.0.0.0', port=80)