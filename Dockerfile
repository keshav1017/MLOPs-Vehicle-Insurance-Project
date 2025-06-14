# Use an official Python 3.13 image from Docker hub
FROM python:3.10-slim-bullseye

# set working directory 
WORKDIR /app

# copy your application code
COPY . /app

# install dependencies
RUN pip install -r requirements.txt

# expose the port FastAPI will run on
EXPOSE 5000

# command to run the FastAPI app
CMD [ "python3", "app.py"]
# CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8080"]