import streamlit as st
from options import options
from zTicker import *
from file_explorer import file_explorer

st.set_page_config(page_title="SMA OPS TOOLS")
st.title("SMA OPS TOOLS")

selection = st.selectbox("Choose Tool Type", options)

if selection == "Z-Ticker Cleaner":
  zticker()
elif selection == "File Explorer Search":
  file_explorer()

st.markdown("**Author: Kevin Vo**")
