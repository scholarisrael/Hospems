from flask import request, url_for,jsonify
from flask_api import FlaskAPI, status, exceptions
from datetime import datetime

app = FlaskAPI(__name__)

# Something to increase the value of id
id = 0
def increment():
    global id
    id +=1
    return id

patients = [{
    'id' : id,
    'time' : datetime.now(),
    'patientNo' : None,
    'wardNo' : None,
    'roomNo' : None,
    'bedNo' : None,
    'Status' : 'Pending'
}]

#Getting the list of all the patients
@app.route('/helpneeded', methods = ['GET'])
def returnPatients():
    return jsonify({'Patient\'s details' : patients})

#Adding a patient to the list
@app.route('/helpneeded', methods = ['POST'])
def addPatient():
    # print("Called AddPatient method")
    increment()
    global id
    # print(f"The new id is: {id}" )
    patient = {
    'id' : id,
    'time' : datetime.now(),
    'patientNo' : request.json['patientNo'],
    'wardNo' : request.json['wardNo'],
    'roomNo' : request.json['roomNo'],
    'bedNo' : request.json['bedNo'],
    'Status' : 'Pending'
    }
    patients.append(patient)
    #return the list of all the patients including the new ones
    return jsonify({'Patient\s names' : patients})


if __name__ == "__main__":
    app.run(debug=True)