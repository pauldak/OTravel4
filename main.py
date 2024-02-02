import streamlit as st

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
    st.markdown(js_script, unsafe_allow_html=True)
