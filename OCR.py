import streamlit as st

# upload your documents

# paste the link of your model 

# you can call different models for your OCR task

# if you want to know how to deploy a production OCR service, check here

st.sidebar.selectbox('Select your detect model', 'SSD', 'Faster-RCNN' , 'CPTN' )


st.header('Optical Character Recognition')

# image preprocessing, layout analysis, Table Extraction and Recognition, Text Region Detection
   
st.image('di.jpg', use_column_width=True)

st.write('General pipeline for OCR is as follows. This is from the open source tool Tesseract. Most of the solutions also follow similar pipeline.')

st.image('tsrt.png', caption='Top-level block diagram of Tesseract')

st.image('pre.png', use_column_width=True)

st.image('layout.png', use_column_width=True, caption='from DocBank: A Benchmark Dataset for Document Layout Analysis')

st.image('table.jpg', use_column_width=True)

st.image('detection.png', use_column_width=True, caption='from DocBank: A Benchmark Dataset for Document Layout Analysis')
  
    
st.sidebar.selectbox('Select your detect model', 'CRNN')

st.markdown('### 4. Text Recognition')

 
st.image('crnn.png', use_column_width=True, caption='from An End-to-End Trainable Neural Network for Image-based Sequence Recognition and Its Application to Scene Text Recognition')

st.sidebar.selectbox('Select your detect model', 'NLP', 'NLP+CV', 'GCN')

st.image('lm.jpg', use_column_width=True, caption='from LayoutLM: Pre-training of Text and Layout for Document Image Understanding')

st.image('gcn.jpeg', use_column_width=True, caption='from Graph Convolution for Multimodal Information Extraction from Visually Rich Documents')

st.image('arc.png', use_column_width=True, caption='from Graph Convolution for Multimodal Information Extraction from Visually Rich Documents')

st.image('dataset.jpg', use_column_width=True)

st.image('tl.png', use_column_width=True)
   
