import streamlit as st

i = 0
if st.button('Click to copy "Hello, World!" to clipboard'):
    i += 1
    js_script = """
    <script>
        navigator.clipboard.writeText('Hello, World!').then(function() {
            alert('Text copied successfully!');
        }, function(err) {
            alert('Failed to copy text: ' + err);
        });
    </script>
    """
    i += 1
    st.markdown(js_script, unsafe_allow_html=True)
