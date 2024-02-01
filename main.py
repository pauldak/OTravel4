import streamlit as st

if st.button('Click to copy "Hello, World!" to clipboard'):
    js_script = """
    <script defer>
    navigator.clipboard.writeText('Hello, World!').then(function() {
      alert('Text copied successfully!');
    }, function(err) {
      console.error('Could not copy text: ', err);
    });
    </script>
    """
    st.write(js_script, unsafe_allow_html=True)