import streamlit as st
import streamlit.components.v1 as components

components.iframe("https://cdn.jsdelivr.net/npm/@streamlit/styletron-provider@0.1.0/build/bundle.js", height=0)

if st.button('Click to copy "Hello, World!" to clipboard'):
    js_script = """
    <script defer>
        navigator.clipboard.writeText('Hello, World!').then(function() {
            st.success('Text copied successfully!');
        }, function(err) {
            st.error('Failed to copy text: ' + err);
        });
    </script>
    """
    st.write(js_script, unsafe_allow_html=True)
