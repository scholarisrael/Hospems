# from datetime import datetime
import requests
def PostWithJson():
    # Declare the json file to be posted
    patient = {
    'patientNo' : '1234',
    'wardNo' : '5',
    'roomNo' : '32',
    'bedNo' : '4',
    }
    headers = {'Content-Type' : 'application/json'}
    r = requests.post(url = 'http://127.0.0.1:5000/helpneeded', json = patient, headers = headers )
    return r

PostWithJson()
