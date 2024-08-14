import streamlit as st
import pandas as pd

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

content2 = """
Below you can find anything you want, feel free to contact me! And I'm adding extra text to prove myself that this can go beyond the column!!"
"""

st.write(content2)

col3, col4, col5 = st.columns([1.5, 0.5, 1.5])


df = pd.read_csv("data.csv", sep=";")

with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image(f"images/{row['image']}")
        st.write(f"[Source Code]({row['url']})")

with col4:
    pass

with col5:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image(f"images/{row['image']}")
        st.write(f"[Source Code]({row['url']})")
