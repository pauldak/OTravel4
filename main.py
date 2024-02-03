import streamlit as st
def main():
    st.title("Copy Paste in streamlit")
    prompt = "I just want to test it"
    pathinput = st.text_input(prompt)

    #you can place your path instead
    Path = f'''{prompt}'''
    st.code(Path, language="python")
    st.markdown("Now you get option to copy")
if __name__ == "__main__":main()