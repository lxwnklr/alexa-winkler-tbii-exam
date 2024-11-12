import streamlit as st
import segno
import time
import os

st.set_page_config(page_title= "Hi", page_icon="laughing")
st.image("images/IMG_1901.jpg")

def qrcode_generator_page():
    st.title("QR Code Generator")

    qr_url = st.text_input(label="Enter your link here:")

    #option 2, use a colour picker but it defaults to black
    dark_colour = st.color_picker("Pick a colour for the dark squares", "#8569a8")

    # thanks Aneeka for suggesting we could create a button
    button = st.button("Click here to generate")

    def generate_qrcode(qr_url, dark_colour):
        directory_path="images"
        os.makedirs(directory_path, exist_ok=True)
        qrcode=segno.make_qr(qr_url)
        qrcode.save("images/qrcode_saved.png", scale=5)

    if button and qr_url:
        with st.spinner("Generate QR Coe:"):
            time.sleep(2)
        generate_qrcode(qr_url, dark_colour)
        st.image("images/qrcode_saved.png", caption= qr_url)

    # warning for when user clicks on button without a url
    if button and qr_url == "":
        st.warning("Please enter the data you would like to encode")

st.markdown("MADE BY ALEXA")

#st.write(qr_url)
