FROM python:3.6.13
COPY ./source_files /app
WORKDIR /app
RUN pip install -r requirements.txt
RUN pip install redis==3.5.3
RUN pip install hotqueue==0.2.8
RUN pip install matplotlib==3.3.4
RUN pip install numpy
ENTRYPOINT ["python"]

