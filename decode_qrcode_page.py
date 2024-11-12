import streamlit as st
import numpy as np
import cv2


def decode_qrcode_page():
    st.title("Decoding QR code")
    qrcode= st.file_uploader("Upload your QR code", type=["jpg","jpeg","png"])

    if qrcode:
        file_bytes=np.asarray(bytearray(qrcode.read()), dtype=np.uint8)
        opencv_image=cv2.imdecode(file_bytes, 1)

        #st.write(file_bytes)
        st.image(qrcode)

        detector = cv2.QRCodeDetector()
        decoded_info, point, straight_qr = detector.detectAndDecode(opencv_image)
        st.write(f"Your QR code contains {decoded_info}")