import streamlit as st
from utils import REGISTRY

METRICS = REGISTRY.get_metrics()

@METRICS.REQUEST_TIME.time()
def i_sleep():
    sleep(1.0)


i_sleep()



st.title('Computer Vision Overview')
st.text('')

tasks = ['Select a Task','Image Classification', 'Object Detection', 'Semantic Segmentation', 'Instance Segmentation', 'Depth Estimation', 'Pose Estimation', 'Object Tracking', 'Face Recognition', 'Emotion Detection', 'Action Recognition', 'Anomaly Detection', 'Video Analysis', '3D Computer Vision']
task = st.sidebar.selectbox('Computer Vision Tasks', tasks)

if task == 'Select a Task':
    st.write('This app gives the overview of different CV tasks and their proposed solutions and challenges. Alough a lot of structured data can use traditional machine learning, computer vision is dominated by deep learning methods. Deep learning is mostly useful for high dimension data. Most solutions in this overview are based on deep learning')


if task == 'Image Classification':
    st.header('Image Classification')
    st.subheader('Dataset')
    st.markdown('#### 1. ImageNet')

    st.subheader('Data Preprocessing')
    st.write('Most of time labeled data is not sufficient. Some data augmentation techniques can increase the dataset.')
    st.markdown('#### Data Augmentation')
    st.image('da.png', use_column_width=True, caption='from 1000x Faster Data Augmentation')

    st.subheader('Models for Image Classification')

    model = st.selectbox('Select the model', ('ResNet', 'Inception', 'EfficientNet'))

    if model == 'ResNet':
        
        st.write('Architecture:')

        st.image('res.png', use_column_width=True)

    if model == 'Inception':
        st.write('Architecture:')

        st.image('incep.png', use_column_width=True)

    if model == 'EfficientNet':
        st.write('Architecture:')

        st.image('eff.png', use_column_width=True)

    st.subheader('Model Compression')

    st.subheader('Model Comparison between Models')  

    
    st.subheader('Model Exploration and Interpretation')
    st.write('model-specific and model agnostic, perturbation oe gradient, local or global ')
    viz = ['Choose a method', 'LIME', 'Saliency Map', 'Grad-CAM']
    visualization = st.selectbox('Model Decision Visualization', viz)  
    if visualization == 'LIME':
        pass
    elif visualization == 'Saliency Map':
        pass    
    elif visualization == 'Grad-CAM':
        pass

    st.write('There are also some cool websites for image visualizations')

    st.subheader('Demo')

    st.button('upload your image')



if task == 'Object Detection':
    st.header('Object Detection')
    st.subheader('Dataset')
    st.markdown('#### COCO')

    st.subheader('Models for Object Detection')

    

    st.markdown('### 1. Two Stage')

    model = st.selectbox('Select the model', ('R-FCN', 'FPN','Faster R-CNN'))

    if model == 'R-FCN':
        st.write('Architecture:')


    st.markdown('### 2. One Stage')

    model = st.selectbox('Select the model', ('SSD', 'YOLO'))

    if model == 'SSD':
        st.write('Architecture:')


    st.subheader('Demo')

    st.button('upload your image')


if task == 'Semantic Segmentation':
    st.header('Semantic Segmentation')
    st.subheader('Dataset')
    st.markdown('#### COCO')
    st.markdown('#### Cityscapes')


    st.subheader('Models for Semantic Segmentation')

    model = st.selectbox('Select the model', ('FCN', 'U-Net', 'SegNet', 'DeepLab'))

    if model == 'FCN':
        st.write('Architecture:')

    st.subheader('Demo')

    st.button('upload your image')



    

if task == 'Instance Segmentation':
    st.header('Instance Segmentation')
    st.subheader('Dataset')
    st.markdown('#### COCO')
    st.markdown('#### Cityscapes')

    st.subheader('Data Preprocessing')
    st.markdown('#### Data Augmentation')

    st.subheader('Models for Instance Segmentation')

    st.markdown('### Mask-R-CNN')

    st.subheader('Demo')

    st.button('upload your image')






if task == 'Depth Estimation':

    

    st.header('Depth Estimation')
    
    st.subheader('Dataset')
    #st.markdown('#### COCO')
    st.subheader('Models for Depth Estimation')
    st.markdown('Autoencoder')

    st.subheader('FastDepth')
    st.image('fd.png', caption='from FastDepth: Fast Monocular Depth Estimation on Embedded Systems', use_column_width=True)


    st.subheader('Demo')

    st.button('upload your image')




if task == 'Pose Estimation':
    st.header('Pose Estimation')
    st.subheader('Dataset')
    #st.markdown('#### COCO')
    st.subheader('Models for Pose Estimation')

    st.subheader('Demo')

    st.button('upload your image')



if task == 'Object Tracking':
    st.header('Object Tracking')
    st.subheader('Dataset')
    #st.markdown('#### COCO')
    st.subheader('Models for Object Tracking')

    st.subheader('Demo')

    st.button('upload your image')


if task == 'Face Recognition':
    st.header('Face Recognition')
    st.subheader('Dataset')
    #st.markdown('#### COCO')
    st.subheader('Models for Face Recognition')

    st.subheader('Demo')

    st.button('upload your image')




if task == 'Emotion Detection':
    st.header('Emotion Detection')
    st.subheader('Dataset')
    #st.markdown('#### COCO')
    st.subheader('Models for Emotion Detection')

    st.subheader('Demo')

    st.button('upload your image')


if task == 'Action Recognition':
    st.header('Action Recognition')
    st.subheader('Dataset')
    #st.markdown('#### COCO')
    st.subheader('Models for Action Recognition')

    st.subheader('Demo')

    st.button('upload your image')





if task == 'Anomaly Detection':

    st.subheader('Intrusion Detection')

    st.subheader('Fraud Detection')

    st.subheader('Malware Detection')

    st.subheader('Medical Anomaly Detection')

    st.subheader('Log Anomaly Detection')

    st.subheader('IoT Anomaly Detection')

    st.subheader('Industrial Anomaly Detection')

    st.subheader('Time Series Anomaly Detection')
    

    st.subheader('Reference')

    st.markdown( '1. [Anomaly Detection With Multiple-Hypotheses Predictions]()')

    st.markdown( '2. [A Survey on GANs for Anomaly Detection]()')

    st.markdown( '3. [Real-world Anomaly Detection in Surveillance Videos]()')


if task == 'Video Analysis':
    st.header('Video Analysis')
    st.subheader('Dataset')
    #st.markdown('#### COCO')
    st.subheader('Models for Video Analysis')


if task == '3D Computer Vision':
    st.header('3D Computer Vision')
    st.subheader('Dataset')
    #st.markdown('#### COCO')
    st.subheader('Models for 3D Computer Vision')

i_sleep()




