import streamlit as st
st.title("Bank & Marketing Prediction")
import pickle
import numpy as np
with open("bank_machine.pkl","rb") as file:
    bank_model= pickle.load(file)
def prediction(age, job,marital,education,default,balance,housing,loan,contact,day,month,duration, campaign, pdays,previous,poutcome):
    input_array=np.array([[age, job, marital,education,default,balance,housing,loan,contact,day,month,duration,campaign,pdays,previous,poutcome]])
    Result= bank_model.predict(input_array)
    return int(Result[0])
age= st.slider("age",0,100)
job= st.slider("job",0,100)
marital= st.slider("marital",0,100)
education= st.slider("education",0,100)
default= st.slider("default",0,100)
balance=st.slider("balance",0,100000)
housing=st.slider("housing",0,100)
loan= st.slider("loan",0,100)
contact=st.slider("contact",0,100)
day=st.slider("day",0,31)
month=st.slider("month",0,12)
duration=st.slider("duration",0,100)
campaign=st.slider("campaign",0,100)
pdays=st.slider("pdays",-10,1000)
previous=st.slider("previous",0,100)
poutcome=st.slider("poutcome",0,100)
if st.button("Final Result"):
    pred= prediction(age,job,marital,education,default,balance,housing,loan,contact,day,month,duration, campaign, pdays,previous,poutcome)
    st.write(f"The predicted outcome is: {pred} (0 = No, 1 = Yes)")
