# Design Home Page
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

import streamlit as st
from streamlit_option_menu import option_menu

import json
import requests
import pandas as pd
import numpy as np

from io import StringIO
import langdetect
from langdetect import DetectorFactory, detect, detect_langs
from PIL import Image

isDataLoaded = False

st.set_page_config(
    page_title="Streamlit Attrition",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'mailto:mk797@cphbusiness.dk',
        'About': "https://docs.streamlit.io"
    }
)

st.sidebar.header("Choose an example!", divider='rainbow')
# st.sidebar.success("Select a demo case from above")

banner = """
    <body style="background-color:yellow;">
            <div style="background-image: linear-gradient(90deg, rgb(255, 75, 75), rgb(28, 3, 204)); ;padding:10px">
                <h2 style="color:white;text-align:center;">Streamlit Attrition App</h2>
            </div>
    </body>
    <style>
        section[data-testid="stSidebar"][aria-expanded="true"]{
            display: none;
        }
    </style>
    """

st.markdown(banner, unsafe_allow_html=True)


st.markdown(
    """
    ###
        
    ### To learn more
    - Check out [Streamlit Documentation](https://docs.streamlit.io)
    - Contact me by [email](mailto://mk797@cphbusiness.dk)
"""
)

def readData(tab):
    prepData(tab)

def prepData(file):
    # We start by loading in the data and just take a quick peek at the first few rows and the shape of the data to see that the data is correctly loaded.
    try:
        df = pd.read_excel(file)
    except:
        df = pd.read_excel(".\\Data\\WA_Fn-UseC_-HR-Employee-Attrition.xlsx")

    # Clean redundant columns
    cleaned_df = df.drop(["Over18"], axis=1) # All values are "Y"
    cleaned_df = cleaned_df.drop(["EmployeeNumber"], axis=1) # All values are unique
    cleaned_df = cleaned_df.drop(["EmployeeCount"], axis=1) # All values are 1
    cleaned_df = cleaned_df.drop(["StandardHours"], axis=1) # All values are 80

    # Convert categorical data to numerical data using one-hot encoding
    cleaned_df = pd.get_dummies(cleaned_df, columns=['Attrition', 'BusinessTravel', 'Department', 'EducationField', 'Gender', 'JobRole', 'MaritalStatus', 'OverTime'], dtype=pd.Int64Dtype())
    cleaned_df = cleaned_df.drop(["Attrition_No"], axis=1) # Redundant

    # Remove columns with low correlation to attrition
    df_corr = cleaned_df.corr()

    df_attrition_yes_corr = df_corr['Attrition_Yes'].sort_values(ascending=False)
    cleaned_df = cleaned_df.drop(df_attrition_yes_corr[(df_attrition_yes_corr < 0.05) & (df_attrition_yes_corr > -0.05)].index, axis=1)

    # Save the cleaned data
    cleaned_df.to_excel(".\\Data\\cleaned_data.xlsx", index=False)

    st.success("Data has been loaded and cleaned. You can now proceed to the next step.")

    banner = """
    <style>
        section[data-testid="stSidebar"][aria-expanded="true"]{
            display: block;
        }
    </style>
    """
    st.markdown(banner, unsafe_allow_html=True)


st.success("Select a file that contains attrition data, using the file loading tool. The file must match the format of the example file: https://www.kaggle.com/datasets/pavansubhasht/ibm-hr-analytics-attrition-dataset/data")
tab = st.file_uploader("Your file")
if tab is not None:  
    try:
        readData(tab) 
    except:
        pass