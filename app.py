import os

import psycopg2
from dotenv import load_dotenv
from flask import Flask, jsonify
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
    redis_client = get_redis_client()
    try:
        visits = int(redis_client.incr("visits"))
    except RedisError:
        visits = 0

    db_status = "unavailable"
    try:
        with get_pg_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    "CREATE TABLE IF NOT EXISTS visits (id SERIAL PRIMARY KEY, count INTEGER NOT NULL)"
                )
                cur.execute("INSERT INTO visits (count) VALUES (%s)", (visits,))
                conn.commit()
                db_status = "connected"
    except Exception:
        db_status = "unavailable"

    return jsonify(
        {
            "message": "Hello from Flask!",
            "redis_visits": visits,
            "database": db_status,
        }
    )


@app.get("/health")
def health():
    return jsonify({"status": "ok"})

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
