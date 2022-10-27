FROM python:3.9.15-slim-buster

RUN mkdir MaggieLevel
COPY main.py ./MaggieLevel
COPY requeriments.txt ./MaggieLevel
RUN mkdir MaggieLevel/Homer
RUN touch MaggieLevel/Homer/Homer.csv
RUN mkdir MaggieLevel/Lisa
RUN touch MaggieLevel/Lisa/Lisa.csv
RUN mkdir MaggieLevel/Resto
RUN touch MaggieLevel/Resto/Resto.csv

RUN pip install --upgrade pip
RUN pip install -r ./MaggieLevel/requirements.txt
CMD ["python","MaggieLevel/main.py"]