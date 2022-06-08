
import numpy as np
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
    df.drop('Unnamed: 0', inplace=True, axis=1)
    st.write(df.head())
    #Select ID
    st.selectbox('Choose ID', df)
    #Graphique
    df = pd.DataFrame(
        np.random.randn(20, 3),
        columns=['EXT_SOURCE_1', 'EXT_SOURCE_2','EXT_SOURCE_3'])
    st.line_chart(df)

MODEL_DIR = os.path.join(os.path.dirname('file'), 'model.pickle')
with open(MODEL_DIR , 'rb') as handle:
    model = pickle.load(handle)