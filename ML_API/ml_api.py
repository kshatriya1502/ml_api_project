from fastapi import FastAPI
import pickle 
from pydantic import BaseModel
import json


app = FastAPI()

class model_input(BaseModel):

    Pregnancies : int
    Glucose  : int
    BloodPressure : int
    SkinThickness : int
    Insulin  : int
    BMI : float
    DiabetesPedigreeFunction : float
    Age  : int



#loading the saved model : 
diabetes_model = pickle.load(open('trained_model/diabetes_model.pkl' , 'rb'))


@app.post('/diabetes_prediction')
def diabetes_pred(input_parameters : model_input):
    input_data = input_parameters.model_dump_json()
    input_dictionary = json.loads(input_data)

    preg  = input_dictionary['Pregnancies']
    glu  = input_dictionary['Glucose']
    bp  = input_dictionary['BloodPressure']
    skin = input_dictionary['SkinThickness']
    insulin = input_dictionary['Insulin']
    bmi  = input_dictionary['BMI']
    dpf  = input_dictionary['DiabetesPedigreeFunction']
    age  = input_dictionary['Age']


    input_list = [preg , glu , bp , skin , insulin , bmi , dpf , age]
    prediction = diabetes_model.predict([input_list])

    if prediction[0] == 0 : 
        return  'The person is not Diabetic'
    else:
        return "The person is Diabetic"
    



    #command to start api : uvicorn ml_api:app

    #comamnd to make requirement.txt : pip freeze > requirements.txt
