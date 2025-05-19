import streamlit as st
import pandas as pd

st.title("My Streamlit App")

st.header("Main Header")
st.header("Test")

st.subheader("Sub Header")

st.markdown("## This is a markdown header")
st.markdown('test is akardow **text**')

st.code("""import streamlit as st """)

st.divider()
st.write("This is a write function")
df = pd.read_csv("bonus_dataset.csv")
#st.dataframe(df)
st.table(df)
st.metric(label="Metric Label", value=900, delta=20, delta_color="normal")