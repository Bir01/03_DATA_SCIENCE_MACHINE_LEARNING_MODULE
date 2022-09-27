import streamlit as st

# Text/Title
st.title("Streamlit Tutorials")
# Header /Subheader
st.header("This is header")
st.subheader("This is subheader")

# Text
st.text("Hello Streamlit")

# Markdown
st.markdown("### This is a Markdown")

# Error/Colorful Text
st.success("Successful")
st.info("Information!")
st.warning("This is a warning")
st.error("This is an error Danger")
st.exception("NameError('name three not defined')")

# Get Help Info About Python
st.help(range)

# Writing Text
st.write("Text with write")
st.write(range(10))


