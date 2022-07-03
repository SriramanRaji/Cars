from email import header
import imp
from flask import Flask, render_template, request
import csv

headers = ['cruiseControl', 'headsUpDisplay', 'tractionControl', 'heatedSeats', 'sunRoof', 'rainSensingWipers', 'airBagsCount']

def createFile(header, data):
    with open('target/request.csv', 'w', encoding='UTF8', newline='') as file:

        writer = csv.writer(file)
        writer.writerow(header)
        writer.writerow(data)


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():

    data = []

    if request.method == 'POST':

        # cruiseControl = request.form.get('cruiseControl')
        # headsUpDisplay = request.form.get('headsUpDisplay')
        # tractionControl = request.form.get('tractionControl')
        # heatedSeats = request.form.get('heatedSeats')
        # sunRoof = request.form.get('sunRoof')
        # rainSensingWipers = request.form.get('rainSensingWipers')
        # airbagsCount = request.form.get('airBagsCount')
        #print(cruiseControl, headsUpDisplay, tractionControl, heatedSeats, sunRoof, rainSensingWipers, airbagsCount)

        for key in headers:
            data.append('Yes' if request.form.get(key) == 'on' else '')
        
        createFile(headers, data)

        return render_template('index.html')

if __name__ == '__main__':
    app.debug = True
    app.run()