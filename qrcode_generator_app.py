import streamlit as st
import segno
import time
#import os

st.set_page_config(page_title= "Hi", page_icon="laughing")


def qrcode_generator_page():
    st.title("QR Code Generator")
    #directory_path="images"
    #os.makedirs(directory_path, exist_ok=True)
    st.image("IMG_1901.jpg")

    qr_url = st.text_input(label="Enter your link here:")

    #option 2, use a colour picker but it defaults to black
    dark_colour = st.color_picker("Pick a colour for the dark squares", "#8569a8")

    # thanks Aneeka for suggesting we could create a button
    button = st.button("Click here to generate")

    def generate_qrcode(qr_url, dark_colour):
        qrcode=segno.make_qr(qr_url)
        qrcode.to_pil(scale=10, dark=dark_colour).save("qrcode_saved.png")

    if button and qr_url:
        with st.spinner("Generate QR Coe:"):
            time.sleep(2)
        generate_qrcode(qr_url, dark_colour)
        st.image("qrcode_saved.png", caption= qr_url)

    # warning for when user clicks on button without a url
    if button and qr_url == "":
        st.warning("Please enter the data you would like to encode")

st.markdown("MADE BY ALEXA")

#st.write(qr_url)
