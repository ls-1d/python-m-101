FROM python:3.9
ENV PYTHONUNBFFERED=1

WORKDIR /app

COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

COPY . /app

EXPOSE 8080

CMD [ "python", "manage.py", "runserver" , "0.0.0.0:8000"]