import streamlit as st
import smtplib, ssl
from send_email import send_email


with st.form(key="email_form"):
    users_email = st.text_input("Your email address")
    email_body = st.text_area("Your message")
    button = st.form_submit_button("Submit")
    if button:
        message = f"""
        From: {users_email}
        {email_body}
                    """
        send_email(message)
        st.info("Your email sent successfully")







