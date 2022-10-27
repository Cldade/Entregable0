FROM python:3.9.15-slim-buster

COPY ./main.py /BartLevel/
COPY ./requirements.txt /BartLevel/

WORKDIR /BartLevel/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
CMD ["python","main.py"]