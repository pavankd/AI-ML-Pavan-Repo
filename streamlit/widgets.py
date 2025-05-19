import streamlit as st
import pandas as pd


#button
primary_button = st.button("Primary Button",type="primary")
secondary_button = st.button("Secondary Button",type="secondary")
if primary_button:
    st.write("Primary Button Clicked")
if secondary_button:
    st.write("Secondary Button Clicked")
st.divider()    
checkbox = st.checkbox("Remember Me")
if checkbox:
    st.write("ok i will remember you")

st.divider()   
df = pd.read_csv("bonus_dataset.csv")
radio_btn = st.radio("Select an option", df.columns[:], index=1,horizontal=True)
st.write(radio_btn)   
st.divider()    
st.divider()    
st.divider()    
st.divider()    
st.divider()    
st.divider()    
st.divider()    
st.divider()    