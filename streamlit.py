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

st.sidebar.header("Try Me!", divider='rainbow')
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