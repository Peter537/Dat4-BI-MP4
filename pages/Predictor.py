import pickle
import pandas as pd
import streamlit as st

loaded_model = pickle.load(open(".\\bestfit_model.save", 'rb'))
df = pd.read_excel('Data\\cleaned_data.xlsx')

# Create a new dataframe and remove all the data
template_df = df.copy()
template_df = template_df.iloc[0:1]
template_df = template_df.drop('Attrition_Yes', axis=1)

data = st.data_editor(template_df)


if st.button('Predict'):
    prediction = loaded_model.predict(data)
    print(prediction)
    if prediction[0] == 0:
        prediction = 'No'
    else:
        prediction = 'Yes'
    st.write('The prediction is:', prediction)