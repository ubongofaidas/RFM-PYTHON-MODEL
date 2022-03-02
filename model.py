#include important modues

import datetime
from dateutil.relativedelta import relativedelta
import pandas as pd
import numpy as np

data_type = { 'S/N': int, 'PHONE': str, 'CUSTOMER_COMPLAINTS': int, 'FREQUENCY': int, 'MONETARY': float }
data_dates = [
    "DOB",
    "REGISTRATION_DATE",
    "FIRST_REFERENCE_TRANSACTION_DATE_SINCE_2020",
    "LAST_TRANSACTION_DATE_WITHIN_30_DAYS"
]
date_format = lambda x: datetime.datetime.strptime(x, '%m/%d/%Y')
rfm = pd.read_csv("input/input.csv", encoding_errors='ignore', engine="python", parse_dates=data_dates, date_parser=date_format, dayfirst=True)

#Define today date
today = datetime.date.today()
#Get age from dob
dob = rfm.DOB
age = []
for d in dob:
    age.append(relativedelta(today, d.date()).years)
rfm['AGE'] = age

#Get time in service from registration date in days
reg_date = rfm.REGISTRATION_DATE
tenure = []
for tn in reg_date:
    tenure.append(relativedelta(today, tn.date()).days)
rfm['TENURE_DAYS'] = tenure

#Get time_2 in date after 30 days
frtds_2020 = rfm.FIRST_REFERENCE_TRANSACTION_DATE_SINCE_2020
timeafterthirtyday = []
for frtds in frtds_2020:
    timeafterthirtyday.append(frtds + datetime.timedelta(days=30))
rfm['DATE_AFTER_THIRTY_DAYS_TIME_2'] = timeafterthirtyday

#Get recency days from time after thirty day and last transaction date within 30 days
recency = (rfm['LAST_TRANSACTION_DATE_WITHIN_30_DAYS'].max() - rfm['DATE_AFTER_THIRTY_DAYS_TIME_2']).dt.days
rfm['RECENCY'] = np.where(recency <= 0, 0, recency)

#Get max and min Recency in days 
maxr = max(rfm.RECENCY)
minr = min(rfm.RECENCY)
#normalize Recency
Rn = round((maxr- rfm['RECENCY'])/(maxr- minr), 2)
rfm['RN'] = Rn

#Get max and min Frequency from rfm.csv
maxf = max(rfm.FREQUENCY)
minf = min(rfm.FREQUENCY)
#normalize Frequency
Fn = round((maxf- rfm['FREQUENCY'])/(maxf- minf), 2)
rfm['FN'] = Fn

#Get max and min Money_generated from rfm.csv
maxm = max(rfm.MONETARY)
minm = min(rfm.MONETARY)
#normalize Money_generated
Mn = round((maxm- rfm['MONETARY'])/(maxm- minm), 2)
rfm['MN'] = Mn

#Get total of Rn, Fn and Mn rfm.csv
Total = round(Rn + Fn + Mn, 2)
rfm["TOTAL"] = Total

#Get average of Rn, Fn and Mn rfm.csv
Avg = round(Total/3, 2)
rfm['AVG'] = Avg 

#Get recency score rs
rfm['R_SCORE'] = np.select([rfm['RN'].le(0.6), rfm['RN'].le(0.7)], [1,2], 3)

#Get frequency score fs
rfm['F_SCORE'] = np.select([rfm['FN'].le(0.6), rfm['FN'].le(0.7)], [1,2], 3)

#Get monetary score ms
rfm['M_SCORE'] = np.select([rfm['MN'].le(0.6), rfm['MN'].le(0.7)], [1,2], 3)

#Get total score from rfm scores
rfm['T_SCORE'] = rfm['R_SCORE'] + rfm['F_SCORE'] + rfm['M_SCORE']

#Get category from total score
rfm['CATEGORY'] = np.select([rfm['T_SCORE'].le(6), rfm['T_SCORE'].le(7)], ["CHURN","POTENTIAL CHURN"], "NO CHURN")


#Generate csv file for our app
rfm.to_csv('output/output.csv', index=False)
print('Data is ready, for further processing...')