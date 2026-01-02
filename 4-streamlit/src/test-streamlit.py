import streamlit as st
import pandas as pd
import numpy as np
import nltk
import random


"""
Arzhang-z
"""

st.write("Hello World")
if st.toggle("On/OFF"):
    st.write("Hi Im ON Now!")

df = pd.DataFrame({
    "First Column": [1,2,3,4],
    "Second Column": [10,20,30,40]
})
df

x = st.slider("Select a Value",0,100,26,2)
st.write(f"x is {x} ")

contact_type = st.selectbox(
    'what istour favorite contact type? ',
    ["Email", "Home Page", "Mobile phone"]
)
st.write(f"You selected {contact_type}")


contact_type = st.radio(
    'what istour favorite contact type? ',
    ["Email", "Home Page", "Mobile phone"]
)
st.write(f"You selected {contact_type}")


contact_type = st.multiselect(
    'what istour favorite contact type? ',
    ["Email", "Home Page", "Mobile phone"]
)
st.write(f"You selected {contact_type}")

if st.checkbox("Show DataFrame"):
    chart_data = pd.DataFrame(
        np.random.randn(10,3),
        columns=["a", "b", "c"]
    )

    st.line_chart(chart_data)
    st.scatter_chart(chart_data)

col1, col2, col3 = st.columns(3)
col1.write("1st column")
col2.multiselect("3rd column",[random.choice(nltk.corpus.words.words()) for i in range(4)])
with col3:
    st.checkbox("2nd column")
    st.write("2nd column")