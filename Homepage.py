import streamlit as st

image="BGImage.jpg"
st.set_page_config(page_title="Plant Doc",page_icon="🌿",layout="centered",initial_sidebar_state="expanded")

st.markdown("<h1 style='text-align:center'> Welcome to Plant Doc!</h1>",unsafe_allow_html=True)
st.markdown("This is a web app that uses a deep learning model to detect plant diseases. To get started, click on the 'Plant Doc' button on the left sidebar.")
st.image(image, caption=None, width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto", use_container_width=False)
st.sidebar.success("Navigation")