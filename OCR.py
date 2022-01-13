import streamlit as st

# upload your documents

# paste the link of your model 

st.sidebar.selectbox('Select your detect model', )


if task == 'OCR':
    st.header('Optical Character Recognition')
    st.markdown('## Scene based:')

    st.markdown('### 1. Image Preprocessing')

    st.markdown('### 2. Text Region Detection')

    st.markdown('### 3. Text Recognition')


    st.markdown('## Document based:')

    st.write('AI Documents Processing can save a lot of time for us, so we can focus on more important decisions.')

    st.image('di.jpg', use_column_width=True)

    st.write('General pipeline for OCR is as follows. This is from the open source tool Tesseract. Most of the solutions also follow similar pipeline.')

    st.image('tsrt.png', caption='Top-level block diagram of Tesseract')

    st.markdown('### 1. Image Preprocessing')
    st.image('pre.png', use_column_width=True)

    st.markdown('### 2. Layout Analysis')

    st.image('layout.png', use_column_width=True, caption='from DocBank: A Benchmark Dataset for Document Layout Analysis')

    st.markdown('#### Table Extraction and Recognition')

    st.image('table.jpg', use_column_width=True)

    st.markdown('### 3. Text Region Detection')

    st.markdown('#### SSD')

    st.markdown('#### Faster-RCNN')
    
    st.markdown('#### CPTN')

    st.write('Example of using Faster-RCNN for text detection.')

    st.image('detection.png', use_column_width=True, caption='from DocBank: A Benchmark Dataset for Document Layout Analysis')
  
    st.markdown('### 4. Text Recognition')

    st.markdown('#### CRNN')
    st.image('crnn.png', use_column_width=True, caption='from An End-to-End Trainable Neural Network for Image-based Sequence Recognition and Its Application to Scene Text Recognition')



    st.markdown('### 5. Information Extraction')

    st.markdown('#### NLP')

    st.markdown('#### NLP + CV')

    st.image('lm.jpg', use_column_width=True, caption='from LayoutLM: Pre-training of Text and Layout for Document Image Understanding')

    st.markdown('#### GCN')

    st.image('gcn.jpeg', use_column_width=True, caption='from Graph Convolution for Multimodal Information Extraction from Visually Rich Documents')

    st.image('arc.png', use_column_width=True, caption='from Graph Convolution for Multimodal Information Extraction from Visually Rich Documents')

    st.header('Open Dataset and Benchmark for OCR')

    st.image('dataset.jpg', use_column_width=True)

    st.header('Document Analysis and Rcognition Conference and Competition')

    st.subheader('ICDAR 2019 SORIE')
    
    st.markdown('#### Task 1. Text Localization')

    st.image('tl.png', use_column_width=True)
    st.markdown('#### Task 2. Scanned Receipt OCR')
    st.markdown('#### Task 3. Key Information Extraction')

    st.subheader('ICDAR 2019 cTDaR')

    st.header('Reference')
