FROM python:3.9.15-slim-buster

RUN mkdir BartLevel
COPY main.py ./BartLevel
COPY requeriments.txt ./BartLevel
RUN mkdir BartLevel/Homer
RUN touch BartLevel/Homer/Homer.csv
RUN mkdir BartLevel/Lisa
RUN touch BartLevel/Lisa/Lisa.csv
RUN mkdir BartLevel/Resto
RUN touch BartLevel/Resto/Resto.csv

RUN pip install --upgrade pip
RUN pip install -r ./BartLevel/requeriments.txt
CMD ["python","BartLevel/main.py"]