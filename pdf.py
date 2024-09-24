import pdfplumber
import streamlit as st

#pdf extracter
def read_pdf_with_pdfplumber(file):
    with pdfplumber.open(file) as pdf:
        page = pdf.pages[0]
        return page.extract_text()


#file input
def pdf_ex():
        docx_file = st.file_uploader("Upload File", type=['txt', 'docx', 'pdf'])
        if docx_file is not None:
            file_details = {"Filename": docx_file.name, "FileType": docx_file.type, "FileSize": docx_file.size}

            if docx_file.type == "application/pdf":
                try:
                    text = read_pdf_with_pdfplumber(docx_file)
                    st.write(text)
                except:
                    st.write("Error reading PDF file")

pdf_ex()