#load all environment variables
from dotenv import load_dotenv
load_dotenv()

#Import required packages and libraries
import streamlit as st #Streamlit to create web application
import os
import google.generativeai as genai #The primary LLM model that resides inside genAI library
from PIL import Image

#Fetch the API key that is defined inside .env
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

#Function that loads Gemini Model and returns the response
def get_model_response(query, user_image):
    model = genai.GenerativeModel('gemini-pro-vision')
    if query != "":
        model_response = model.generate_content([query, user_image])
    else:
        model_response = model.generate_content(user_image)
    return model_response.text

#Set up Streamlit application to visualize results
st.set_page_config(page_title="Visualize Image-Text")
st.header("Bring Image to words ✨!!")

user_input=st.text_input("What do you want to know about the image ? ",key="user_input")
uploaded_file = st.file_uploader("Pick your image ...", type=["jpg", "jpeg", "png"])

image=""   
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.", use_column_width=True)

submit=st.button("See the magic ✨")
if submit:
    model_response=get_model_response(user_input, image)
    st.subheader("Results here 👇🏻")
    st.write(model_response)