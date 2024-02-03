import streamlit as st
def main():
    st.title("Copy Paste in streamlit")
    pathinput = st.text_input("Enter your Path:")
    pathinput += "Just test clipboard"
    #you can place your path instead
    Path = f'''{pathinput}'''
    st.code(Path, language="python")
    st.markdown("Now you get option to copy")
if __name__ == "__main__":main()