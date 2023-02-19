# -*- coding: utf-8 -*-
"""
Created on Sun Jun 12 11:36:48 2022

@author: siddhardhan
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import pickle
import json


app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class model_input(BaseModel):

    age : int
    sex : int
    cp : int
    trestbps : int
    chol : int
    fbs : float
    restecg :  float
    thalach : int
    exang : int
    oldpeak : float
    slope : int
    ca : int
    thal : int

# loading the saved model
diabetes_model = pickle.load(open('diabetes_model_LR_model.sav','rb'))


@app.post('/diabetes_model_LR_model')
def diabetes_pred(input_parameters : model_input):

    input_data = input_parameters.json()
    input_dictionary = json.loads(input_data)

    age = input_dictionary['age']
    sex = input_dictionary['sex']
    cp = input_dictionary['cp']
    trestbps = input_dictionary['trestbps']
    chol = input_dictionary['chol']
    fbs = input_dictionary['fbs']
    restecg = input_dictionary['restecg']
    thalach = input_dictionary['thalach']
    exang = input_dictionary['exang']
    oldpeak = input_dictionary['oldpeak']
    slope = input_dictionary['slope']
    slope = input_dictionary['slope']
    ca = input_dictionary['ca']


    input_list = [age, sex, bp, skin, insulin, bmi, dpf, age]

    prediction = diabetes_model.predict([input_list])

    if prediction[0] == 0:
        return 'The person is not Diabetic'

    else:
        return 'The person is Diabetic'
