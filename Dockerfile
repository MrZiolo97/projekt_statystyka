FROM python:3.8.2

 
WORKDIR /app/
 
COPY requirements.txt /app/
RUN pip install -r requirements.txt
 
COPY app.py __init__.py /app/
COPY RSSI_linear_prediction_model.pkl /app/
 
EXPOSE 5000
 
ENTRYPOINT python ./app.py
 
