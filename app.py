# app.py
import streamlit as st

st.title("簡単なPythonウェブアプリ")
name = st.text_input("あなたの名前は？")
st.write(f"こんにちは、{name}さん！")
