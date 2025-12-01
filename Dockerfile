FROM python:3.14-alpine

COPY main.py ./

ENTRYPOINT ["python","./main.py"]