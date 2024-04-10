FROM python:3.10
WORKDIR /machine-learning-client
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 5002
CMD ["python", "classification.py"]