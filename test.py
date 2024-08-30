import google.generativeai as genai
import streamlit as st
import PIL.Image

st.title("Visionary Chatbot: Describe Your Images with Gemini LLM. By - Akash Anandani")

genai.configure(api_key='AIzaSyBl4PlPPFDi-YU39pxwcCpvtZlSd-LPPms')
model = genai.GenerativeModel('gemini-1.5-pro')

img_uploader  = st.file_uploader('')

if img_uploader is not None: 
    img = PIL.Image.open(img_uploader)
    st.write(img)
    query = st.text_input('ask your question : ')
    response = model.generate_content([query,img])
    st.markdown(response.text)
else : 
    st.info('Please upload an image to get started')    