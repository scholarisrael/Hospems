from flask import request, url_for,jsonify
from flask_api import FlaskAPI, status, exceptions

app = FlaskAPI(__name__)
patients = [{'file' : '0'}]
#Getting the list of all the patients
@app.route('/helpneeded', methods = ['GET'])
def returnPatients():
    return jsonify({'Patient\'s names' : patients})

#Adding a patient to the list
@app.route('/helpneeded', methods = ['POST'])
def addPatient():
    patient = {'file' : request.json['file']}
    patients.append(patient)
    #return the list of all the patients including the new ones
    return jsonify({'Patient\s names' : patients})


if __name__ == "__main__":
    app.run(debug=True)