FROM python:3.8.6-slim
COPY . /process
WORKDIR /process
EXPOSE 8000
RUN python -m pip install -r requirements.txt
# CMD python -m flask run --host=0.0.0.0
CMD gunicorn app:app -b 0.0.0.0:8000
