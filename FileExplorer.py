
def file_explorer(): 
 import streamlit as st
  user_input = st.text_area("Enter values (one per line):", height=200)
  separator = st.selectbox("Choose a separator:", ["AND", "OR"])
  lines = [line.strip() for line in user_input.strip().split("\n") if line.strip()]
  input_count = len(lines)
  st.markdown(f"**Input count:** {input_count}")
  if lines:
    result = f" {separator} ".join(lines)
    st.markdown("**Joined Output:**")
    st.code(result, language="text")
  else:
    st.info("Start typing to see the output...")

  
