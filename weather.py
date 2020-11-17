import pickle
import os.path

zip_code = '90002'
api_key = None
with open('weather_token.pkl', 'rb') as token:
    api_key = pickle.load(token)
api_call = "api.openweathermap.org/data/2.5/weather?zip={}&appid={}".format(zip_code, api_key)

print(api_call)


    

