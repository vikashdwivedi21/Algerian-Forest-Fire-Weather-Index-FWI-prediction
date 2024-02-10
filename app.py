from flask import Flask, request,jsonify,render_template
import pickle
import numpy as np
import pandas as np
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)

# import Ridge Regressor and Standard scaler pickel file
ridge_model = pickle.load(open('Models/ridge.pkl','rb'))
standard_scaler = pickle.load(open('Models/scaler.pkl','rb'))

# # Rout for Home Page
# @app.route('/')
# def index():
#     return render_template('index.html')

@app.route('/',methods=['GET','POST'])
def predict_datapoint():
    if request.method == 'POST':

        Temperature = float(request.form.get('Temperature'))
        RH    = float(request.form.get('RH'))
        Ws    = float(request.form.get('Ws'))
        Rain  = float(request.form.get('Rain'))
        FFMC  = float(request.form.get('FFMC'))
        DMC   = float(request.form.get('DMC'))
        ISI   = float(request.form.get('ISI'))
        Classes = float(request.form.get('Classes'))
        Region  = float(request.form.get('Region'))
        
        new_data_scaled = standard_scaler.transform([[Temperature,RH,Ws,Rain,FFMC,DMC,ISI,Classes,Region]])
        result = ridge_model.predict(new_data_scaled)

        return render_template('home.html',prediction=result[0])
        
    else:
        return render_template('home.html')


if __name__=="__main__":
    app.run(host="0.0.0.0")



