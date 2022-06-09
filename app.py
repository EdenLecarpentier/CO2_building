
import pandas as pd
import streamlit as st
import os
import pickle

st.title("""
# Home Credit Default Risk
""")

uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
#if uploaded_file is not None:
#    df = pd.read_csv(uploaded_file)
#    df.drop('Unnamed: 0', inplace=True, axis=1)
#    st.write(df.head())
#    #Select ID
#    st.selectbox('Choose ID', df)
#    #Graphique
#    df = pd.DataFrame(
#        np.random.randn(20, 3),
#        columns=['EXT_SOURCE_1', 'EXT_SOURCE_2','EXT_SOURCE_3'])
#    st.line_chart(df)

MODEL_DIR = os.path.join(os.path.dirname('file'), 'model.pickle')
with open(MODEL_DIR , 'rb') as handle:
    model = pickle.load(handle)


original_list = ["None","Office" , "Parking" , "Other" , "Retail Store" , "Self-Storage Facility" , "Other-Services" , "Restaurant" , "Supermarket" , "Bar/nightclub" , "Other-Education" , "Data Center" , "Non refregirated warehouse"]
type_of_building = st.sidebar.selectbox("select your first main building type : " , original_list)

type_of_building = st.sidebar.selectbox("select your second main building type : " , original_list)

type_of_building = st.sidebar.selectbox("select your third main building type : " , original_list)

number_of_floor_list = ["1" , "2" , "3" , "4" , "5"]
number_of_floor = st.sidebar.selectbox("select the number of floor in your buildings : " , number_of_floor_list)

year_it_was_built_list = ["2021", "2022"]

date = st.sidebar.date_input('date the building(s) where created :' , year_it_was_built_list)