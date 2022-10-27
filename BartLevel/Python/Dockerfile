FROM python:3.9.15-slim-buster

RUN mkdir BartLevel
COPY main.py ./BartLevel
COPY requeriments.txt ./BartLevel


RUN pip install --upgrade pip
RUN pip install -r ./BartLevel/requeriments.txt
CMD ["python","BartLevel/main.py"]