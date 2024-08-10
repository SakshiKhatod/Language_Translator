import streamlit as st
from dotenv import load_dotenv



def main():
    load_dotenv() 
    st.set_page_config(page_title="Chat with Multiple Documents", page_icon=":books:")
    st.header("Chat with PDFs :books:")
    st.text_input("Ask a question about your documents:")
    with st.sidebar:
        st.subheader("Your documents")
        pdf_docs=st.file_uploader("Upload your pdf's here and click on 'Process'",accept_multiple_files=True)
        if st.button("Process"):
            # get pdf text


            #get text chunks


            #create vector store


if __name__ == "__main__":
    main()
