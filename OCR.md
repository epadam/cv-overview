# OCR and Information Extraction

A demo streamlit app comparing between different Algorithm/models

## General

No matter scene text or documents it needs text detection followed by text recognition 

### Text Detection

* Faster-RCNN
* CTPN

### Text Recognition

* CRNN
  * CTC Loss 

#### Hand Written Recognition

## Information Extraction for Documents

Form, Reciept,etc

Image preprocessing --> Document Classification --> Key-Value Extraction

Book, Articles, Reports

Image preprocessing --> Document Classification --> Layout Analysis --> Table, Text Extraction


### Image Preprocessing

#### Document Rectification and Illumination Correction

* https://github.com/xiaoyu258/DocProj

### Document Classification

### Layout Analysis

* DeepDeSRT: Deep Learning for Detection and Structure Recognition of Tables in Document Images

### Table Recognition

* https://arxiv.org/ftp/arxiv/papers/2010/2010.08591.pdf


### Key-Value Extraction

#### Template Based

Pre_define location


#### Deep Learning Based

* Transformer Based
    * [LayoutLM]()
    
* Graph Network
    * Spatial Dual-Modality Graph Reasoning for Key Information Extraction [`arXiv`](https://arxiv.org/abs/2103.14470)

* [Google Document](https://ai.googleblog.com/2020/06/extracting-structured-data-from.html)

* [ReLIE: Representation-Learning-for-Information-Extraction]()

* https://github.com/Praneet9/Representation-Learning-for-Information-Extraction

* [CUTIE: Learning to Understand Documents with Convolutional Universal Text Information Extractor]()

* Deep Reader: Information extraction from Document images via relation extraction and Natural Language

* Key Information Extraction From Documents: Evaluation And Generator


## Data Augmentation for OCR

## Active Learning for OCR

## Open Source Resources



## Tools

* mmOCR [`github`](https://mmocr.readthedocs.io/en/latest/)
* easyOCR
* AttentionOCR

## Reference

* Timeseries anomaly detection using an Autoencoder [`link`](https://keras.io/examples/timeseries/timeseries_anomaly_detection/)




## Process Flow

Data Annotation --Trigger retraining pipeline--> Retraining models --> CD to deploy the model

## Annotation for OCR

## MLOps for OCR

### Retraining Kubeflow Pipeline (CI/CD/CT)



## Reference:
- LayoutLM
- mmOCR
- ReLIE: Representation-Learning-for-Information-Extraction

## Public Dataset

## Open Source

### https://github.com/miaomiaosoft/PandaOCR
