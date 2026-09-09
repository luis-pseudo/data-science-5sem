import streamlit as st
import pandas as pd 
st.title("hello streamlit")
dataframe = pd.read_csv("https://github.com/luis-pseudo/data-science-5sem/blob/f345dfc03ca02ff9fed2b34c32d62ffa141a66f8/Amazon_Reviews.csv")
st.dataframe(dataframe)
st.write("by adsoftsito")
