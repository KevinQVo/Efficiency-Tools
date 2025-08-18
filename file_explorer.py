
def file_explorer():
    import streamlit as st
    user_input = st.text_area("Enter values:", height=200)
    separator = st.selectbox("Choose a separator:", ["AND", "OR"])
    
    if user_input:
        lines = user_input.split("\n")
        total_entries = len(lines)
        
        cleaned = []
        for line in lines:
            line = line.strip()
            if len(line) > 0:
                cleaned.append(line)
            else:
                st.warning("Blank or whitespace-only line detected and ignored.")
        
        if cleaned:
            result = f" {separator} ".join(cleaned)
            st.subheader("Joined Output:")
            st.code(result, language="text")
            st.info(f"Total Entries: {len(cleaned)}")
        else:
            st.info("No valid input lines to process.")
