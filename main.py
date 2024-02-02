import streamlit as st
import time


if st.button('Click to copy "Hello, World!" to clipboard'):

    js_script = """
    <script>
        navigator.clipboard.writeText('Hello, World!').then(function() {
            alert('Text copied successfully!');
        }, function(err) {
            alert('Failed to copy text: ' + err);
        });
    </script>
    """
    time.sleep(10)  # delays for 10 seconds
    st.markdown(js_script, unsafe_allow_html=True)
    time.sleep(10)  # delays for 10 seconds
