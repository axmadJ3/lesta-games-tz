from flask import Flask, jsonify
import redis
from dotenv import load_dotenv
import os

load_dotenv()

redis_client = redis.StrictRedis(
    host='redis',
    port=6379,
    decode_responses=True
)

app = Flask(__name__)

@app.route('/ping', methods=['GET'])
def ping():
    return jsonify(status='ok')

@app.route('/count', methods=['GET'])
def visits_count():
    visits = redis_client.incr('visits')
    return jsonify(visits=visits)

if __name__ == '__main__':
    app.run(host=os.getenv('FLASK_HOST', '0.0.0.0'), port=int(os.getenv('FLASK_PORT', 5000)))
