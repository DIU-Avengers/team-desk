import os

import psycopg2
from dotenv import load_dotenv
from flask import Flask, jsonify, render_template
from redis import Redis
from redis.exceptions import RedisError

# Load environment variables from a .env file if present.
load_dotenv()

app = Flask(__name__)

DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "5432")
DB_NAME = os.getenv("DB_NAME", "appdb")
DB_USER = os.getenv("DB_USER", "appuser")
DB_PASSWORD = os.getenv("DB_PASSWORD", "apppassword")
REDIS_HOST = os.getenv("REDIS_HOST", "localhost")
REDIS_PORT = int(os.getenv("REDIS_PORT", "6379"))
PORT = int(os.getenv("PORT", "5000"))
DEBUG = os.getenv("FLASK_DEBUG", "false").lower() in ("1", "true", "yes")


def get_pg_connection():
    return psycopg2.connect(
        host=DB_HOST,
        port=DB_PORT,
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
    )


def get_redis_client():
    return Redis(host=REDIS_HOST, port=REDIS_PORT, decode_responses=True)


@app.get("/")
def index():
    return render_template("index.html", title="Home", team_name = "Team Avengers")
   


@app.get("/health")
def health():
   index_html = open("index.html", "r").read()
   return index_html


@app.get("/about-us")
def about_us():
    return jsonify(
        {
            "members" : [
                {
                    "name" : "Shagato Chowdhury",
                    "role" : "DevOPS"
                }
            ]
        }
    )
    

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=PORT, debug=DEBUG)


@app.get("/contact")
def contact():
    contact_html = open("contact.html", "r").read()
    return contact_html

