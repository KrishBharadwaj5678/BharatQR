import qrcode
import streamlit as st
from streamlit import download_button

st.set_page_config(
    page_title="BharatQR | UPI QR Code Generator",
    page_icon="./assets/icons/icon.png",
    menu_items={
        "About":"BharatQR is a simple and secure platform to generate UPI QR codes instantly. Without the need for sign-up, you can create a QR by simply entering your UPI ID."
    }
)

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size= 10,
    border=2,
)

st.write("<h2 style='color:#FF5722;'>Create UPI QR Codes with BharatQR.</h2>",unsafe_allow_html=True)

upiId=st.text_input("UPI ID",placeholder="Enter your UPI ID here...")

payeName=st.text_input("Payee Name",placeholder="Enter your business name here...")

amount = st.number_input("Amount",placeholder="Enter transaction description here...",min_value=0)

desc = st.text_input("Description (Notes)",placeholder="Enter transaction description here...")

generate = st.button("Generate QR Code")

if generate:

    if len(upiId)>0 and len(payeName)>0 and len(str(amount))>0:
        upi = f"upi://pay?pa={upiId}&pn={payeName}&&am={amount}&cu=INR&tn={desc}"
        qr.add_data(upi)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        img.save("upi.png")

        # Show the image and download button
        st.image("upi.png")
        with open("upi.png","rb") as genQR:
            download_button = st.download_button("Download QR Code",genQR.read(),"upi.png")
    else:
        st.error("⚠️ Some required fields are empty.")
