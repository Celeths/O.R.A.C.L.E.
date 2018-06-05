FROM python:latest

WORKDIR /usr/src/Oracle For Discord X
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY ./ ./

CMD ["python", "Oracle For Discord X"]