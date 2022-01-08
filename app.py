import streamlit as st
import easyocr
from PIL import Image

image_file = st.file_uploader("Upload An Image",type=['png','jpeg','jpg'])


if image_file is not None:
    file_details = {"FileName":image_file.name,"FileType":image_file.type}
    st.write(file_details)
    img = Image.open(image_file)
    
    
    st.image(img)
    st.write(image_file.name)
    
    with open(image_file.name,"wb") as f: 
      f.write(image_file.getbuffer())         
    st.success("Saved File")
    
    reader = easyocr.Reader(['ch_sim','en']) # this needs to run only once to load the model into memory
    result = reader.readtext(image_file.name)
    st.write(result)
