from flask import Flask
from flask import request
from flask import jsonify
from math import log10
from sklearn import linear_model
import pickle
 
app = Flask(__name__)
 
@app.route('/prediction/api/v1.0/RSSI_prediction', methods=['GET'])
def get_prediction():
 distance = float(request.args.get('d'))
 frequency = float(5.9*1000000000.0)
 
 modelname = 'RSSI_linear_prediction_model.pkl'

 
 loaded_model = pickle.load(open(modelname, 'rb'), encoding='latin1')
 RSSI = loaded_model.predict([[log10(distance), log10(frequency), 0.0]])
 
 return jsonify(distance=distance, frequency=frequency, RSSI=RSSI[0])
  
if __name__ == '__main__':
 app.run(port=5000,host='0.0.0.0')
