FROM python:3
# ADD . /
ADD bot.py /
ADD requirements.txt /
RUN pip install -U -r requirements.txt
CMD [ "python", "./bot.py" ]
# FROM ubuntu:latest
# RUN apt-get update -y
# RUN apt-get install -y python-pip python-dev build-essential
# COPY . /app
# WORKDIR /app
# RUN pip install -r requirements.txt
# ENTRYPOINT ["python"]
# CMD ["bot.py"]
