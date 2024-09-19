import json 
import requests

url = "http://localhost:80/diabetes_prediction"

input_data_for_model = {
    'Pregnancies' :  20,
    'Glucose'  : 200,
    'BloodPressure' : 200,
    'SkinThickness' : 200,
    'Insulin'  : 100,
    'BMI' : 36.6,
    'DiabetesPedigreeFunction' : 0.351,
    'Age'  : 60
}


input_json  = json.dumps(input_data_for_model)
response = requests.post(url , data = input_json)

print(response.text)


