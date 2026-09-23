import streamlit as st
import pandas as pd


@st.cache_data
def load_data() -> pd.DataFrame:
	return pd.read_csv(
		"Amazon_Reviews.csv",
		engine="python",
		on_bad_lines="skip",
	)


st.title("hello world web")
st.write("hello world streamlit")
dataframe = load_data()
st.dataframe(dataframe)
