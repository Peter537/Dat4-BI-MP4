import pandas as pd
import streamlit as st
st.sidebar.header("Choose a module!", divider='rainbow')
import re

import plotly.express as px
import plotly.io as pio

import seaborn as sns
import matplotlib.pyplot as plt

def columnPicker(df):
        st.header('Grouping by a Nominal Attribute')
        x = st.selectbox('**Select the nominal attribute, X**', df.columns)
        y = st.selectbox('**Select first measure, Y**', df.columns)
        z = st.selectbox('**Select extra measure, Z**', df.columns)     
        return x, y, z

# Design the visualisation
def charts():
        
            tab1, tab2, tab3 = st.tabs(['Bar chart', 'Scatter plot', 'Line chart'])
            with tab1:
                fig = px.bar(readableDataframe(df), x=x, y=y, color=z, title=f'{x} vs {y} by {z}')
                st.plotly_chart(fig)
            
            with tab2:
                fig = px.scatter(readableDataframe(df), x=x, y=y, color=z, title=f'{x} vs {y} by {z}')
                st.plotly_chart(fig)
            
            with tab3:
                fig = px.line(readableDataframe(df), x=x, y=y, color=z, title=f'{x} vs {y} by {z}')
                st.plotly_chart(fig)
                  

def createTable(df):
    df = df.copy() # Copy of the frame to break the reference to the original frame
    df_attrition_yes_corr = df['Attrition_Yes'].sort_values(ascending=False)
    df_attrition_yes_corr = df_attrition_yes_corr.drop('Attrition_Yes')

    # Make the correlation data into percentage and round for better understanding
    df_attrition_yes_corr = df_attrition_yes_corr * 100
    df_attrition_yes_corr = df_attrition_yes_corr.round(2)

    # Change column names for better understanding
    df_attrition_yes_corr.index = df_attrition_yes_corr.index.str.replace('_', ' ')
    df_attrition_yes_corr.index = df_attrition_yes_corr.index.str.replace(' ', '\n')
    df_attrition_yes_corr.index = [re.sub(r'([A-Z])', r' \1', col) for col in df_attrition_yes_corr.index]

    df_attrition_yes_corr = df_attrition_yes_corr.rename(index='Correlation Percentage')
    
    st.write('Correlation of Attrition_Yes with other attributes. The table shows the percentage of correlation. A positive percentage indicates a positive correlation, and a negative percentage indicates a negative correlation. The closer the percentage is to 100 or -100, the stronger the correlation, meaning the more likely or unlikely an employee is to leave.')
    st.write(df_attrition_yes_corr, use_container_width=True)        

    st.markdown(
        """
        <style>
            div[data-testid="stFullScreenFrame"] {
                text-align: center;
            }
        </style>
    """, unsafe_allow_html=True)

def readableDataframe(dataframe):
    dataframe = dataframe.copy() # Copy of the frame to break the reference to the original frame
    dataframe.columns = dataframe.columns.str.replace('_', ' ')
    dataframe.columns = dataframe.columns.str.replace(' ', '\n')

    # Find all capital letters and replace them with a space and the capital letter
    dataframe.columns = [re.sub(r'([A-Z])', r' \1', col) for col in dataframe.columns]

    return dataframe

df = pd.read_excel('Data\\cleaned_data.xlsx')
df_corr = df.corr() # Raw correlation data

df_corr_readable = readableDataframe(df_corr)

createTable(df_corr)

x, y, z = columnPicker(df_corr_readable)

if st.button(":green[Explore]"):
    st.subheader("Explore the Data in Diagrams")
    st.write('Click on tabs to explore')
    container = st.container()
    charts()