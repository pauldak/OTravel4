import streamlit as st
def main():
    st.title("Hit the copy at the bottom right of the prompt")
    prompt = ("I just want to test it bbvbcbvbn vbnbnvnbnv  cbnvncbvcnbbvbn "
              "eyuey uuiruyy vcnvcnif m iiiieiei  "
              "vncvn c v  vc vc  vccv cv fgg f gfgfg")
    # pathinput = st.text_input(prompt)

    #you can place your path instead
    Path = f'''{prompt}'''
    st.code(Path, language="python")
    st.markdown("Now you get option to copy")
if __name__ == "__main__":main()