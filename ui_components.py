import streamlit as st
from streamlit_extras.add_vertical_space import add_vertical_space

def setup_sidebar_and_title():
    with st.sidebar:
        st.title('Zania PDF 📑 Chat App 💬')
        st.markdown('''
        ## Project By
        Nishanth G (g.nishanth@live.com)
        - [Project Repo]()
        - [github](https://github.com/Nishanth-works)
        - [LinkedIn](https://www.linkedin.com/in/nishanth-gandhi-350b54165/)
        - [Portfolio](https://nishanth-works.github.io/life_of_portfolio/)
        ''')
        add_vertical_space(5)
        st.write('')

    st.title('Zania PDF 📑 Chat App 💬')

def upload_pdf_ui():
    pdf = st.file_uploader("Upload your PDF", type='pdf')
    return pdf

def ask_question_ui():
    query = st.text_input("Ask a question about your PDF file:")
    return query

def display_json_response(response):
    st.json(response)

def stop_search_ui():
    return st.button("Stop Search")

def new_pdf_upload_ui():
    return st.button("Upload New PDF")

def display_message(message):
    st.write(message)
