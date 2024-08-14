import streamlit as st


with st.form(key="email_form"):
    users_email = st.text_input("Your email address")
    email_body = st.text_area("Your message")
    button = st.form_submit_button("Submit")
    if button:
        message = email_body + users_email

