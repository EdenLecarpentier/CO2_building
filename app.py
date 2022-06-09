
import pandas as pd
import streamlit as st
import os
import pickle


st.title("""
# Co2 Building
""")

#if uploaded_file is not None:
#    df = pd.read_csv(uploaded_file)
#    df.drop('Unnamed: 0', inplace=True, axis=1)
#    st.write(df.head())
#    st.line_chart(df)
model = None

MODEL_DIR = os.path.join(os.path.dirname('file'), 'model.pickle')
with open(MODEL_DIR , 'rb') as handle:
    model = pickle.load(handle)

uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    if st.button('Predict'):
            #test_x = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
            val = model.predict(handle)
            #.reshape(-1, 28, 28,1))
            st.write(handle)
            


#original_list = ["None","Office" , "Parking" , "Other" , "Retail Store" , "Self-Storage Facility" , "Other-Services" , "Restaurant" , "Supermarket" , "Bar/nightclub" , "Other-Education" , "Data Center" , "Non refregirated warehouse"]
#type_of_building = st.sidebar.selectbox("select your first main building type : " , original_list)
#
#type_of_building = st.sidebar.selectbox("select your second main building type : " , original_list)
#
#type_of_building = st.sidebar.selectbox("select your third main building type : " , original_list)
#
#number_of_floor_list = ["1" , "2" , "3" , "4" , "5"]
#number_of_floor = st.sidebar.selectbox("select the number of floor in your buildings : " , number_of_floor_list)
#
## year_it_was_built_list = ["2021", "2022"]
#
#date = st.sidebar.date_input('date the building(s) where created :')
#test_x = pd.read_csv("C:/Users/edenl/Desktop/ia_coding/machine_learning/co2/data/Clean.csv")

                  