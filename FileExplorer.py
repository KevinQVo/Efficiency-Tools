
def file_explorer(): 
  st.title("Join Inputs with AND/OR")
  user_input = st.text_area("Enter values (one per line):")
  separator = st.selectbox("Choose separator:", ["AND", "OR"])
  if st.button("Generate Output"):
    lines = [line.strip() for line in user_input.strip().split("\n") if line.strip()]
    if lines:
        result = f" {separator} ".join(lines)
        st.success("Output:")
        st.code(result, language="text")
    else:
        st.warning("Please enter at least one value.")

  
