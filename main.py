import streamlit as st
from options import options
import zTicker

st.set_page_config(page_title="SMA OPS TOOLS")
st.title("SMA OPS TOOLS")

selection = st.selectbox("Choose Tool Type", options)

