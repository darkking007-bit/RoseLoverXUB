FROM python:latest

WORKDIR .

RUN pip install -r -U requirements.txt
CMD ["python3", "-m", "Wylie"]
