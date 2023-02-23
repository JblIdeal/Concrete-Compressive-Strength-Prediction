import streamlit as st
import pandas as pd
import numpy as np
#from PIL import Image
from prediction import predict
import base64

st.set_page_config(layout="wide", page_title="Concrete Compressive Strength Prediction")

@st.cache(allow_output_mutation=True)
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def set_png_as_page_bg(png_file):
    bin_str = get_base64_of_bin_file(png_file)
    page_bg_img = '''
    <style>
    .stApp {
    background-image: url("data:image/png;base64,%s");
    background-size: cover;
    }
    </style>
    ''' % bin_str
    
    st.markdown(page_bg_img, unsafe_allow_html=True)
    return

#set_png_as_page_bg('concrete_image.jpeg')

st.title(":black[Concrete Compressive Strength Prediction] :+1:")
st.sidebar.write("## Menu")
st.subheader("Web App to Predict the Concrete Compressive Strength Using a Gradient Boosting Regression Model")
#st.subheader("Using a Gradient Boosting Regression Model ")

#img = Image.open("concrete_image.jpeg")
#st.image(img, width=700)

st.info("**Please Enter the Values of the Concrete Compressive Strength Attributes**")
col1, col2, = st.columns(2)

with col1:
    Cement = st.slider("**Cement Component (kg in a m3 mixture)**", 102, 540, value=280, step=1)
    BFS = st.slider("**Blast Furnace Slag (kg in a m3 mixture)**", 0, 359, value=73, step=1)
    Fly_Ash = st.slider("**Fly Ash (kg in a m3 mixture)**", 0, 200, value=54, step=1)
    Water = st.slider("**Water (kg in a m3 mixture)**", 121, 247, value=181, step=1)
    
with col2:
    Superplasticizer = st.slider("**Superplasticizer (kg in a m3 mixture)**", 0, 32, value=6, step=1)
    Coarse_Agg = st.slider("**Coarse Aggregate (kg in a m3 mixture)**", 801, 1145,  value=972, step=1)
    Fine_Agg = st.slider("**Fine Aggregate (kg in a m3 mixture)**", 594, 992, value=773, step=1)
    Age = st.slider("**Age of Concrete (Days)**", 1, 365, value=45, step=1)
    
    
if st.button("**Predict Concrete Compressive Strength**"):
    result = predict(Cement, BFS, Fly_Ash, Water, Superplasticizer, Coarse_Agg, Fine_Agg, Age)
    st.success("**:green[The concrete compressive strength is {} MPa]**".format(result))