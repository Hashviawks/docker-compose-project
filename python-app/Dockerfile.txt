from python:3.13.9
WORKDIR /app
COPY requirements.txt .
RUN pip isntall -r requirements.txt
COPY . .
EXPOSE 5000
CMD ["python", "app.py"]