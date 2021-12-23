FROM python:3.6
RUN apt update
RUN pip install --upgrade pip
RUN pip install flask

ADD flask/ /opt
CMD ["python","/opt/app.py"]
