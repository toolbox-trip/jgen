FROM python:3.8.6-slim
COPY . /process
WORKDIR /process
RUN python -m pip install -r requirements.txt
EXPOSE 5000
CMD python -m flask run --host=0.0.0.0
