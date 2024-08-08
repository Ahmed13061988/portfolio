import streamlit as st
st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.JPG")


with col2:
    st.title("Ahmed Hussein")
    content = """
    Hello all! My name is Ahmed, I'm from Iraq. I finished my dental school 2016, but I found my passion in
        coding.
    """
    st.info(content)


