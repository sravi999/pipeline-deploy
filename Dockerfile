FROM python:3.6
RUN pip install flask

ADD flask/ /opt
CMD ["python","/opt/app.py"]
