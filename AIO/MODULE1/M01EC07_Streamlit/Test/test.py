import streamlit as st

with st.form("My Form"):
    col1, col2 = st.columns(2)
    f_name = col1.text_input("First Name")
    l_name = col2.text_input("Last Name")
    submitted = st.form_submit_button("Submit")
    if submitted:
        st.write("First Name: ", f_name, l_name)
        
upload_file = st.file_uploader("Shoose File", accept_multiple_files = True)
