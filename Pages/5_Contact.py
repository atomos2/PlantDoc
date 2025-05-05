import streamlit as st  

def contact_page():
    st.title("Contact")

    st.write("""
        If you have any questions, feedback, or wish to collaborate, feel free to get in touch through the form below or via the listed platforms.
    """)

    with st.form(key='contact_form'):
        name = st.text_input("Name")
        email = st.text_input("Email")
        message = st.text_area("Message")
        submit_button = st.form_submit_button(label='Send')

        if submit_button:
            st.success("Thank you for reaching out. I will get back to you shortly.")

st.markdown("---")

st.subheader("Connect")
st.write("📧 Email: [alamiftikhar0006@gmail.com](mailto:alamiftikhar0006@gmail.com)")
st.write("🔗 GitHub: [github.com/atomos2](https://github.com/atomos2)")
st.write("💼 LinkedIn: [linkedin.com/in/iftikhar-alam-07b05b287/](https://www.linkedin.com/in/iftikhar-alam-07b05b287/)")