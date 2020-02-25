from flask import Flask, render_template, url_for, request
import numpy as np
import pandas as pd
import pickle

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('predict.html')

@app.route('/result',methods=['POST','GET'])
def result():
    if request.method == 'POST':
        body = request.form

        # Age
        Age = int(input['Age'])

        # Balance
        Balance = int(input['Balance'])

        # Duration
        Duration = int(input['Duration'])
        
        # Campaign
        Campaign = int(input['Campaign'])
        
        # Job
        Job = input['Job']
        strJob = ''
        if Job == 'Admin':
            job1 = 1; job2 = 0; job3 = 0; job4 = 0; job5 = 0; job6 = 0; job7 = 0; job8 = 0; job9 = 0; job10 = 0; job11 = 0; job12 = 0; strJob = 'Admin.'
        if Job == 'Blue-Collar':
            job1 = 0; job2 = 1; job3 = 0; job4 = 0; job5 = 0; job6 = 0; job7 = 0; job8 = 0; job9 = 0; job10 = 0; job11 = 0; job12 = 0; strJob = 'Blue-Collar'
        if Job == 'Entrepreneur':
            job1 = 0; job2 = 0; job3 = 1; job4 = 0; job5 = 0; job6 = 0; job7 = 0; job8 = 0; job9 = 0; job10 = 0; job11 = 0; job12 = 0; strJob = 'Entrepreneur'
        if Job == 'Housemaid':
            job1 = 0; job2 = 0; job3 = 0; job4 = 1; job5 = 0; job6 = 0; job7 = 0; job8 = 0; job9 = 0; job10 = 0; job11 = 0; job12 = 0; strJob = 'Housemaid'
        if Job == 'Management':
            job1 = 0; job2 = 0; job3 = 0; job4 = 0; job5 = 1; job6 = 0; job7 = 0; job8 = 0; job9 = 0; job10 = 0; job11 = 0; job12 = 0; strJob = 'Management'
        if Job == 'Retired':
            job1 = 0; job2 = 0; job3 = 0; job4 = 0; job5 = 0; job6 = 1; job7 = 0; job8 = 0; job9 = 0; job10 = 0; job11 = 0; job12 = 0; strJob = 'Retired'
        if Job == 'Self Employed':
            job1 = 0; job2 = 0; job3 = 0; job4 = 0; job5 = 0; job6 = 0; job7 = 1; job8 = 0; job9 = 0; job10 = 0; job11 = 0; job12 = 0; strJob = 'Self-Employed'
        if Job == 'Services':
            job1 = 0; job2 = 0; job3 = 0; job4 = 0; job5 = 0; job6 = 0; job7 = 0; job8 = 1; job9 = 0; job10 = 0; job11 = 0; job12 = 0; strJob = 'Services'
        if Job == 'Student':
            job1 = 0; job2 = 0; job3 = 0; job4 = 0; job5 = 0; job6 = 0; job7 = 0; job8 = 0; job9 = 1; job10 = 0; job11 = 0; job12 = 0; strJob = 'Student'
        if Job == 'Technician':
            job1 = 0; job2 = 0; job3 = 0; job4 = 0; job5 = 0; job6 = 0; job7 = 0; job8 = 0; job9 = 0; job10 = 1; job11 = 0; job12 = 0; strJob = 'Technician'
        if Job == 'Unemployed':
            job1 = 0; job2 = 0; job3 = 0; job4 = 0; job5 = 0; job6 = 0; job7 = 0; job8 = 0; job9 = 0; job10 = 0; job11 = 1; job12 = 0; strJob = 'Unemployed'
        if Job == 'Unknown':
            job1 = 0; job2 = 0; job3 = 0; job4 = 0; job5 = 0; job6 = 0; job7 = 0; job8 = 0; job9 = 0; job10 = 0; job11 = 0; job12 = 1; strJob = 'Unknown'
        
        # Marital
        Marital = input['Marital']
        strMar = ''
        if Marital == 'Divorced':
            div = 1; mar = 0; sgl = 0; strMar = 'Divorced'
        if Marital == 'Married':
            div = 0; mar = 1; sgl = 0; strMar = 'Married'
        if Marital == 'Single':
            div = 0; mar = 0; sgl = 1; strMar = 'Single'
        
        # Education
        Education = input['Education']
        strEdu = ''
        if Education == 'Primary':
            pri = 1; sec = 0; ter = 0; unkEdu = 0; strEdu = 'Primary'
        if Education == 'Secondary':
            pri = 0; sec = 1; ter = 0; unkEdu = 0; strEdu = 'Secondary'
        if Education == 'Tertiary':
            pri = 0; sec = 0; ter = 1; unkEdu = 0; strEdu = 'Tertiary'
        if Education == 'Unknown':
            pri = 0; sec = 0; ter = 0; unkEdu = 1; strEdu = 'Unknown'
        
        # Default
        Default = input['Default']
        strDft = ''
        if Default == 'No':
            dftNo = 1; dftYes = 0; strDft = 'No'
        else:
            dftNo = 0; dftYes = 1; strDft = 'Yes'
                
        # Housing
        Housing = input['Housing']
        strHos = ''
        if Housing == 'No':
            hosNo = 1; hosYes = 0; strHos = 'No'
        else:
            hosNo = 0; hosYes = 1; strHos = 'Yes'
        
        # Loan
        Loan = input['Loan']
        strLon = ''
        if Loan == 'No':
            lonNo = 1; lonYes = 0; strLon = 'No'
        else:
            lonNo = 0; lonYes = 1; strLon = 'Yes'
        
        # Contact
        Contact = input['Contact']
        strCon = ''
        if Contact == 'Cellular':
            cel = 1; tel = 0; unkCon = 0; strCon = 'Cellular'
        if Contact == 'Telephone':
            cel = 0; tel = 1; unkCon = 0; strCon = 'Telephone'
        if Contact == 'Unknown':
            cel = 0; tel = 0; unkCon = 1; strCon = 'Unknown'
                
        # Month
        Month = input['Month']
        strMon = ''
        if Month == 'April':
            apr = 1; aug = 0; dec = 0; feb = 0; jan = 0; jul = 0; jun = 0; mar = 0; may = 0; nov = 0; oct = 0; sep = 0; strMon = 'April'
        if Month == 'August':
            apr = 0; aug = 1; dec = 0; feb = 0; jan = 0; jul = 0; jun = 0; mar = 0; may = 0; nov = 0; oct = 0; sep = 0; strMon = 'August'
        if Month == 'December':
            apr = 0; aug = 0; dec = 1; feb = 0; jan = 0; jul = 0; jun = 0; mar = 0; may = 0; nov = 0; oct = 0; sep = 0; strMon = 'December'
        if Month == 'February':
            apr = 0; aug = 0; dec = 0; feb = 1; jan = 0; jul = 0; jun = 0; mar = 0; may = 0; nov = 0; oct = 0; sep = 0; strMon = 'February'
        if Month == 'January':
            apr = 0; aug = 0; dec = 0; feb = 0; jan = 1; jul = 0; jun = 0; mar = 0; may = 0; nov = 0; okt = 0; sep = 0; strMon = 'January'
        if Month == 'July':
            apr = 0; aug = 0; dec = 0; feb = 0; jan = 0; jul = 1; jun = 0; mar = 0; may = 0; nov = 0; okt = 0; sep = 0; strMon = 'July'
        if Month == 'June':
            apr = 0; aug = 0; dec = 0; feb = 0; jan = 0; jul = 0; jun = 1; mar = 0; may = 0; nov = 0; okt = 0; sep = 0; strMon = 'June'
        if Month == 'March':
            apr = 0; aug = 0; dec = 0; feb = 0; jan = 0; jul = 0; jun = 0; mar = 1; may = 0; nov = 0; okt = 0; sep = 0; strMon = 'March'
        if Month == 'May':
            apr = 0; aug = 0; dec = 0; feb = 0; jan = 0; jul = 0; jun = 0; mar = 0; may = 1; nov = 0; okt = 0; sep = 0; strMon = 'May'
        if Month == 'November':
            apr = 0; aug = 0; dec = 0; feb = 0; jan = 0; jul = 0; jun = 0; mar = 0; may = 0; nov = 1; okt = 0; sep = 0; strMon = 'November'
        if Month == 'October':
            apr = 0; aug = 0; dec = 0; feb = 0; jan = 0; jul = 0; jun = 0; mar = 0; may = 0; nov = 0; okt = 1; sep = 0; strMon = 'October'
        if Month == 'September':
            apr = 0; aug = 0; dec = 0; feb = 0; jan = 0; jul = 0; jun = 0; mar = 0; may = 0; nov = 0; okt = 0; sep = 1; strMon = 'September'
        
        datainput = [[Age, Balance, Duration, Campaign, job1, job2, job3, job4, job5, job6, job7, job8, job9, job10, job11, job12, div, mar, sgl, pri, sec, ter, unkEdu, dftNo, dftYes, hosNo, hosYes, lonNo, lonYes, cel, tel, unkCon, apr, aug, dec, feb, jan, jul, jun, mar, may, nov, okt, sep]]
        pred = model.predict(datainput)[0]
        proba = model.predict_proba(datainput)[0]
        
        if pred == 0:
            prbb = round((proba[0] * 100), 1)
            rslt = 'YES'
            color = 'green'
        else:
            prbb = round((proba[1] * 100), 1)
            rslt = 'NO'
            color = 'red'        
        
        return render_template(
            'result.html', Age = Age, Balance = Balance, Duration = Duration, Campaign = Campaign, Job = strJob,
            Marital = strMar, Education = strEdu, Default = strDft, Housing = strHos, Loan = strLon,
            Contact = strCon, Month = strMon, result = rslt, proba = prbb, color = color
        )

if __name__ == '__main__':
    with open('modelPickle', 'rb') as modelku:
        model = pickle.load(modelku)
    app.run(debug=True, port=5050)