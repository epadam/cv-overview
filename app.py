import streamlit as st
import easyocr

uploaded_file = st.file_uploader("Choose a file")

image_file = st.file_uploader("Upload An Image",type=['png','jpeg','jpg'])

if image_file is not None:
    file_details = {"FileName":image_file.name,"FileType":image_file.type}
    st.write(file_details)
    img = load_image(image_file)
    st.image(img,height=250,width=250)
    file_name = image_file.name
    with open(file_name ,"wb") as f: 
      f.write(image_file.getbuffer())         
    st.success("Saved File")
    
    
reader = easyocr.Reader(['ch_sim','en']) # this needs to run only once to load the model into memory

result = reader.readtext(file_name)

st.write(result)
