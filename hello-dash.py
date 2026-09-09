import streamlit as st
import pandas as pd 
st.title("hello streamlit")
dataframe = pd.read_csv("https://raw.githubusercontent.com/luis-pseudo/data-science-5sem/blob/master/Amazon_Reviews.csv")
st.dataframe(dataframe)
st.write("by adsoftsito")
