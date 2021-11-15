FROM python:3.7
ENV PORT 8501
WORKDIR /app
COPY requirements.txt ./requirements.txt
RUN pip3 install -r requirements.txt

COPY . .
CMD streamlit run --global.metrics=true  app.py 
