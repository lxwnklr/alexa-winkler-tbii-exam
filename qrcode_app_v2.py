import streamlit as st
import segno
import time
from decode_qrcode_page import decode_qrcode_page
from qrcode_generator_app import qrcode_generator_page

st.set_page_config(page_title= "Hi", page_icon="laughing")
st.image("images/IMG_1901.jpg")

options =["Create QR code", "Decode QR code", "About me"]
page_selection =st.sidebar.selectbox("Menu", options)


if page_selection == "Create QR code":
    qrcode_generator_page()
elif page_selection == "Decode QR code":
    decode_qrcode_page()
elif page_selection == "About me":
    st.write("Hi im alexa")



