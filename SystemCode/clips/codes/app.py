#!/usr/bin/env python
# coding: utf-8

# In[2]:

from flask import Flask,render_template,url_for,request
import pandas as pd 
import numpy as np
import pickle
from sklearn.externals import joblib
from sklearn.ensemble import RandomForestClassifier

app = Flask(__name__)

@app.route('/')
def home():
	return render_template('input.html')

@app.route('/predict',methods=['POST'])
def predict():

	#Usage of Saved Model
	random_forest = open('random_forest.pkl','rb')
	rf2 = joblib.load(random_forest)

	if request.method == 'POST':
		message = request.form['message']
		churn_data = [message]
		churn_data['Family_Person'] = np.where((churn_data['Dependents'] =='Yes') & (churn_data['Partner']=='Yes'),1,0)
		churn_data['Protection'] = np.where((churn_data['TechSupport'] == 'Yes') |\
                                    (churn_data['OnlineSecurity'] == 'Yes') |\
                                    (churn_data['OnlineBackup'] == 'Yes') |\
                                    (churn_data['DeviceProtection'] == 'Yes'),1,0)
		churn_data['TotalServices'] = (churn_data[['PhoneService', 'InternetService', 'OnlineSecurity',
                                       'OnlineBackup', 'DeviceProtection', 'TechSupport',
                                       'StreamingTV', 'StreamingMovies']]== 'Yes').sum(axis=1)
		churn_data['Has_Internet'] = churn_data['InternetService'].replace(['Fiber optic','DSL','No'], [1,1,0])
		churn_data['Streaming'] = np.where((churn_data['StreamingTV'] == 'Yes') | (churn_data['StreamingMovies'] == 'Yes'),1,0)
		churn_data['Tech_Payment'] = np.where((churn_data['PaymentMethod'] != 'Mailed check'),1,0)
		churn_data['Techie'] = np.where((churn_data['Streaming'] == 1) | (churn_data['Tech_Payment']==1),1,0)
		churn_data['Premium_Services'] = np.where((churn_data['MultipleLines'] == 'Yes') & 
                                              (churn_data['InternetService'] == 'Fiber optic'),1,0)
		churn_data['Committed'] = churn_data['Contract'].replace(['Two year','One year','Month-to-month'], [1,1,0])
		churn_data['PhoneService'] = churn_data['PhoneService'].replace(['Yes','No'], [1,0])
		churn_data['PaperlessBilling'] = churn_data['PaperlessBilling'].replace(['Yes','No'], [1,0])
		churn_data['Dependents'] = churn_data['Dependents'].replace(['Yes','No'], [1,0])
		churn_data['Partner'] = churn_data['Partner'].replace(['Yes','No'], [1,0])


        churn_features = churn_data[churn_data['Committed','tenure','MonthlyCharges','Has_Internet',
        'Premium_Services','PaperlessBilling','Protection','SeniorCitizen','TotalServices','Streaming',
        'Family_Person','Techie','Tech_Payment']]

        # Function for label encoding categorical variables
        def label_encoder(dataframe, col_name): 
        	from sklearn.preprocessing import LabelEncoder
        	le = LabelEncoder()
        	le.fit(dataframe[col_name].unique())
        	dataframe[col_name] = le.transform(dataframe[col_name])

        for i in list(churn_features.columns[churn_features.dtypes =='object']):
        	label_encoder(churn_features, i)

		my_prediction = rf2.predict(churn_features)
	return render_template('score.html',prediction = my_prediction)

if __name__ == '__main__':
	app.run(debug=True, port=10)


# In[ ]:




