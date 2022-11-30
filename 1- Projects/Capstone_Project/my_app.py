import streamlit as st
import pickle
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from PIL import Image
import base64
from sklearn.compose import make_column_transformer
from sklearn.preprocessing import OrdinalEncoder

st.image("churn.png", use_column_width=True)
html_temp = """
<div style="background-color:blue;padding:10px">
<h2 style="color:white;text-align:center;">Employee Churn Prediction </h2>
</div>"""
st.sidebar.markdown(html_temp,unsafe_allow_html=True)
html_temp = """
<div style="background-color:tomato;padding:10px">
<h2 style="color:white;text-align:center;">Streamlit ML Cloud App </h2>
</div>"""
st.sidebar.image("churn.png", use_column_width=True)
st.markdown(html_temp,unsafe_allow_html=True)


satisfaction_level = st.sidebar.slider(label="Satisfaction Level", min_value=0.0, max_value=1.0, step=0.01)
time_spend_company = st.sidebar.slider("Time Spend in Company", min_value=1, max_value=20, step=1)
number_project = st.sidebar.slider(label="number_project", min_value=0, max_value=15, step=1)
last_evaluation = st.sidebar.slider(label="Last Evaluation", min_value=0.0, max_value=1.0, step=0.01)
average_monthly_hours = st.sidebar.slider(label="average_monthly_hours", min_value=0, max_value=350, step=10)

capstone_2_model = pickle.load(open('xgb_model_final', 'rb'))

scalerfile = 'scaler.sav'
scaler = pickle.load(open(scalerfile, 'rb'))

my_dict = {'satisfaction_level':satisfaction_level, 
	   'last_evaluation':last_evaluation, 
	   'number_project':number_project, 
	   'average_montly_hours':average_monthly_hours,
	   'time_spend_company':time_spend_company
	   }

df = pd.DataFrame.from_dict([my_dict])

user_inputs = df

user_inputs_transformed = scaler.transform(user_inputs)

prediction = capstone_2_model.predict(user_inputs_transformed)


st.header("The inputs are below")
st.table(df)

st.subheader('Click PREDICT if configuration is OK')

if st.button('PREDICT'):
	if prediction[0]==0:
		st.success(prediction[0])
		st.success(f'Employee will STAY :)')
	elif prediction[0]==1:
		st.warning(prediction[0])
		st.warning(f'Employee will LEAVE :(')
    
