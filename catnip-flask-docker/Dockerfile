FROM python:3.8
#FROM alpine:3.20.3
# set a directory for the app
WORKDIR /app

# copy all the files to the container
COPY requirements.txt /app

# install dependencies
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app
# tell the port number the container should expose
EXPOSE 5000

# run the command
CMD ["python", "./app/app.py"]

