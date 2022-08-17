# -*- coding: utf-8 -*-
"""
Created on Tue Aug 16 16:06:59 2022

 @author: miadmin
"""
import pickle
import streamlit as st
from streamlit_option_menu import option_menu


#loading the saved models
\
diabetes_model=pickle.load(open("diabetes_model.sav", 'r'))
heart_disease_model=pickle.load(open("heart_disease_model.sav", 'r'))

#side bar fro navigation
with st.sidebar:
    selected = option_menu('multiple disease prediction system',
                        ['Diabetes Prediction',
                         'Heart Disease Prediction'],
                        default_index = 0)
    
    
#diabetes prediction page
if (selected == 'Diabetes Prediction'):
     
     #page title
     st.title('Diabetes Prediction using ML')

#getting the input data from user
col1, col2, col3, =st.columns(3)

with col1:
    Pregnancies = st.text_input('number of Pregencies')
    
with col2:
    Glucose = st.text_input('Glucose Level')
    
    
with col3:
   BloodPressure = st.text_input('Blood Pressure Level')
   
    
with col1:
    SkinThickness= st.text_input('Skin Thickness Value')   
    
    
with col2:
    Insulin = st.text_input('Insulin Level')
    
    
with col3:
    BMI = st.text_input('BMI Value')    
    
with col1:
   DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function')  
   
with col2:
    Age= st.text_input('Age of the person')   
     
    
    #code for prediction diabetes_diagenosis=''

    #creating a button for prediction

    if st.button('diabetes test result'):diabetes_prediction = diabetes_model.predict([[ Pregnancies, Glucose, BloodPressure, Age, SkinThickness,
                                                                                        Insulin,BMI,DiabetesPedigreeFunction,Age]]) 
    if (diabetes_prediction[0] == 1):
        diabetes_diagnosis = 'the person is diabetic'
    else:
         diabetes_diagnosis = 'the person is not diabetic'
st.success(diabetes_diagnosis)   

#hheart diasease prediction page

if (selected == 'Heart Disease Prediction'):
    
    #page title 
    st.title('Heart Disease Prediction using ML')
    
col1, col2, col3, =st.columns(3) 
   
with col1:
    Age= st.text_input('Age')
    
with col2:
    Sex = st.text_input('Sex')
    
    
with col3:
   CP = st.text_input('Chest Pain Types')
   
    
with col1:
   Trestbps = st.text_input('Serum Cholestoral in mg/dl')   
    
    
with col2:
    Chol = st.text_input('Insulin Level')
    
with col3:
    fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')
    
with col1:
    restecg = st.text_input('Resting Electrocardiographic Results')
    
    
with col2:
     thalach = st.text_input('Maximum Heart Rate Achieved')
   
    
with col3:
      exang = st.text_input('Excercise Induced Angina')   
    
    
with col1:
     oldpeak = st.text_input('ST depression induced by excercise')
       
with col2:
      slope = st.text_input('Slope Of The Peak Excercise ST Segment')   
    
    
with col3:
    ca = st.text_input('Major Vessels Colored By Flourosopy') 
    
with col1:
   thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')     

    
#code for prediction heart_diagenosis=''

#creating a button for prediction

if st.button('heart disease test result'):
    heart_prediction = heart_disease_model.predict([[Age, Sex, CP, Trestbps, Chol, fbs, restecg, thalach, exang, oldpeak, slope, 
                                                     ca, thal]]) 
if (heart_prediction[0]  == 1):
    heart_diagnosis = 'the person is having heart disease'
else:
    heart_diagnosis = 'the person is not having heart disease'
    
st.success(heart_diagnosis) 