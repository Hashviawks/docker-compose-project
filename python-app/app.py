from flask import Flask
import psycopg2
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "Python service is running!"

@app.route("/db")
def db_test():
    conn = psycopg2.connect(
        host = os.environ["DB_HOST"],
        user = os.environ["DB_USER"],
        password = os.environ["DB_PASS"],
        dbname = os.environ["DB_NAME"]
    )
    return "Connected to DB from python"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
