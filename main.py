import streamlit as st

# Triggered by a button click
if st.button('Click to copy "Hello, World!" to clipboard'):
    # JavaScript to copy text
    js_script = """
        <script>
        navigator.clipboard.writeText('Hello, World!').then(function() {
            /* Success */
            alert('Text copied successfully!');
        }, function(err) {
            /* Error */
            console.error('Could not copy text: ', err);
        });
        </script>
    """

    # Display the JavaScript
    st.markdown(js_script, unsafe_allow_html=True)
