# OCR and Information Extraction

## Image Preprocessing

### Dewarping

## Layout Analysis

## Table Recognition

## Text Detection

* Faster-RCNN
* CTPN


## Text Recognition

* CRNN
  * CTC Loss 

## Information Extraction

### Deep Learning
* Transformer Based
    * LayoutLM []()
* Graph Network
    * Spatial Dual-Modality Graph Reasoning for Key Information Extraction [`arXiv`](https://arxiv.org/abs/2103.14470)

### Template Based

Define location

Use text recognition to find the 


## Open Source Resources


## Tools

* mmOCR [`github`](https://mmocr.readthedocs.io/en/latest/)
* easyOCR
* AttentionOCR

## Reference

* Timeseries anomaly detection using an Autoencoder [`link`](https://keras.io/examples/timeseries/timeseries_anomaly_detection/)


# OCR With Kubeflow, mlrun

The process of OCR includes 4 steps.
1. Document Preprocessing
2. Text Detection
3. Text Recognition
4. Key-Value Pair Extraction

## Process Flow

Data Annotation --Trigger retraining pipeline--> Retraining models --> CD to deploy the model

## Annotation Images


## Retraining Kubeflow Pipeline (CI/CD/CT)



## Reference:
- LayoutLM
- mmOCR
- ReLIE: Representation-Learning-for-Information-Extraction
