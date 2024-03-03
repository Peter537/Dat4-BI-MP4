import pickle
import pandas as pd
import streamlit as st
st.sidebar.header("Choose a module!", divider='rainbow')

def loadPredictionHistory():
    try:
        with open('.\\Data\\prediction_history.csv', 'r') as f:
            return pd.read_csv(f)
    except:
        return pd.DataFrame(columns=['Date', 'Model', 'Attrition'])

def savePredictionHistory(history):
    with open('.\\Data\\prediction_history.csv', 'w') as f:
        history.to_csv(f, index=False)

filename = ".\\" + st.session_state["model"]
loaded_model = pickle.load(open(".\\bestfit_model.save", 'rb'))
df = pd.read_excel('Data\\cleaned_data.xlsx')

history = loadPredictionHistory()

# Create a new dataframe and remove all the data
template_df = df.copy()
template_df = template_df.iloc[0:1]
template_df = template_df.drop('Attrition_Yes', axis=1)

st.write('Fill in the data to predict if an employee will leave or not.')
with st.expander('The model is trained on the following data:'):
    st.write(df)
data = st.data_editor(template_df)

st.warning('The model will often favor if an employee is working over time or not and this will skew certain predictions.')

if st.button('Predict'):
    prediction = loaded_model.predict(data)
    print(prediction)
    if prediction[0] == 0:
        prediction = 'No'
    else:
        prediction = 'Yes'
    st.write('The prediction is:', prediction)

    history = pd.concat([history, pd.DataFrame({'Date': [pd.Timestamp.now()], 'Model': [st.session_state["model"]], 'Attrition': [prediction]})], ignore_index=True)
    savePredictionHistory(history)



st.write('Prediction history:')
st.write(history)

if st.button('Clear history'):
    history = pd.DataFrame(columns=['Date', 'Model', 'Attrition'])
    savePredictionHistory(history)
    st.write('History cleared.')
    
    # Reload the page to update the history
    st.rerun()