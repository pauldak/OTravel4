import streamlit as st
import pyperclip

a=st.text_area('Type in the text_area and click copy')

if st.button('Copy'):
    pyperclip.copy(a)
    st.success('Text copied successfully!')