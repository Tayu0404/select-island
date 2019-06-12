FROM python:3

COPY ./island.py /
CMD ["python", "./island.py"]
