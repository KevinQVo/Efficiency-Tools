import streamlit as st
from options import options
from zTicker import *

st.set_page_config(page_title="SMA OPS TOOLS")
st.title("SMA OPS TOOLS")

selection = st.selectbox("Choose Tool Type", options)

if selection == "Z-Ticker Cleaner":
  zticker()
elif selection == "File Explorer
