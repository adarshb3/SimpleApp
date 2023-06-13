import streamlit as st
import pandas as pd
def main():
    st.title("Simple Streamlit App")
    name = st.text_input("Enter your name:")
    if st.button("Submit"):
        st.write("Hello, " + name + "!")

if __name__ == "__main__":
    main()
