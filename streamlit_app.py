import streamlit as st, requests, json

st.title("🧠 Pattern-Based Data Representation System")
file = st.file_uploader("Upload text", type=["txt"])
if file and st.button("Extract Patterns"):
    res = requests.post("http://localhost:8000/patterns/extract/", files={"file": file}).json()
    st.write(res)

if st.button("Run Feedback Cycle"):
    st.write(requests.post("http://localhost:8000/feedback/cycle").json())
