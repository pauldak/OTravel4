import streamlit as st

text = "Hello World"

if st.button('Copy to Clipboard'):

    # JavaScript to copy text
    js = f"""
    navigator.clipboard.writeText('{text}').catch(error => {{
      console.error(error);
      return false; 
    }});    
  """

    # Execute JavaScript
    result = st.script(js)

    # Notify success or failure
    if result:
        st.success('Text copied to clipboard')
    else:
        st.error('Unable to copy text')