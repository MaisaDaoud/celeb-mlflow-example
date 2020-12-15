FROM python:3.7

COPY req.txt .

RUN pip install --upgrade pip
RUN pip install  tensorflow==2.1.0
RUN pip install -r req.txt
COPY load_data.py .

RUN python load_data.py