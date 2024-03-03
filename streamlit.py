# Design Home Page
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
import pickle

import streamlit as st
from streamlit_option_menu import option_menu

import pandas as pd
import numpy as np

import supervisedml as sml
from sklearn.model_selection import train_test_split
from sklearn.ensemble import VotingClassifier, RandomForestClassifier
from sklearn.naive_bayes import BernoulliNB

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

st.sidebar.header("Choose a module!", divider='rainbow')
# st.sidebar.success("Select a demo case from above")

banner = """
    <body style="background-color:yellow;">
            <div style="background-image: linear-gradient(90deg, rgb(255, 75, 75), rgb(28, 3, 204)); ;padding:10px">
                <h2 style="color:white;text-align:center;">Streamlit Attrition App</h2>
            </div>
    </body>
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
    cleaned_df = cleaned_df.drop(df_attrition_yes_corr[(df_attrition_yes_corr < correlation) & (df_attrition_yes_corr > -correlation)].index, axis=1)

    # Save the cleaned data
    cleaned_df.to_excel(".\\Data\\cleaned_data.xlsx", index=False)

    if correlation != 0.05:
        test_size = 0.2
        seed = 42

        df = cleaned_df.dropna()

        # Split the data into features and target
        X = df.drop('Attrition_Yes', axis=1)
        y = df['Attrition_Yes']

        # Split the data into training and validation sets
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=seed)

        st.spinner("Retraining model...")
        # Random Forest Classifier with transformed data
        print("--- Model Checker ---")
        print("Random Forest Classifier")
        RFCModelChecker = sml.ModelChecker(RandomForestClassifier(n_estimators=100), X_train, y_train, X_test, y_test)
        RFCModelChecker.run()
        RFCR2 = RFCModelChecker.show_accuracy()
        RFCmodel = RFCModelChecker.model

        # Bernoulli Naive Bayes with transformed data
        print("\nBernoulli Naive Bayes")
        BNBModelChecker = sml.ModelChecker(BernoulliNB(), X_train, y_train, X_test, y_test)
        BNBModelChecker.run()
        BNBR2 = BNBModelChecker.show_accuracy()
        BNBmodel = BNBModelChecker.model

        # Voting classifier with transformed data, Random Forest and Bernoulli Naive Bayes
        print("\nVoting Classifier")
        VCModelChecker = sml.ModelChecker(VotingClassifier(estimators=[('rf', RFCmodel), ('nb', BNBmodel)], voting='soft'), X_train, y_train, X_test, y_test)
        VCModelChecker.run()
        VCR2 = VCModelChecker.show_accuracy()
        VCmodel = VCModelChecker.model

        if RFCR2[0] > BNBR2[0] and RFCR2[0] > VCR2[0]:
            bestfit_model = RFCmodel
        elif BNBR2[0] > RFCR2[0] and BNBR2[0] > VCR2[0]:
            bestfit_model = BNBmodel
        else:
            bestfit_model = VCmodel
        
        # Save the best model
        filename = "bestfit_model.save"
        pickle.dump(bestfit_model, open(filename, 'wb'))
        st.success("Model has been retrained and saved.")
        st.session_state["model"] = filename
    else:
        st.session_state["model"] = "bestfit_model.save"

    st.success("Data has been loaded and cleaned. You can now proceed to the next step.")


st.success("Select a file that contains attrition data, using the file loading tool. The file must match the format of the example file: https://www.kaggle.com/datasets/pavansubhasht/ibm-hr-analytics-attrition-dataset/data")

correlation = st.number_input("Minumum correlation with attrition (Standard is 0.05)", min_value=0.0, max_value=1.0, value=0.05, step=0.01)
if correlation != 0.05:
    st.warning("Selecting a correlation different from 0.05 will require the model to be retrained, which will trigger when file is uploaded. This may take a while...")

file = st.file_uploader("Your file")
if file is not None:  
    try:
        readData(file) 
    except:
        pass