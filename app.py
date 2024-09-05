import streamlit as st
st.set_page_config(page_title = "Lab manager")
st.title("IST 688 HW Ankit")
st.write("Hello there")
lab1_page = st.Page("labs/lab1.py", title = "Lab 1")
lab2_page = st.Page("labs/lab2.py", title = "Lab 2")
pg = st.navigation([lab1_page, lab2_page])

pg.run()