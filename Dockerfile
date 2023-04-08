FROM python:3.10.6

ADD * .

RUN pip install -r requirements.txt

CMD ["python", "./nepse.py"]