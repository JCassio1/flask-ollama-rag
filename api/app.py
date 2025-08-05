from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
import json
import logging
from datetime import datetime

app = Flask(__name__)
CORS(app) 
logger = logging.getLogger(__name__)

OLLAMA_URL = "http://localhost:11434"
DEFAULT_MODEL = "llama3.2"

conversations = {}

@app.route('/')
def home():
    """Welcome endpoint"""
    return jsonify({
        "message": "Welcome to Ollama Flask API",
        "version": "1.0.0",
        "endpoints": {
            "/aihealth": "Check system health",
        }
    })

@app.route('/aihealth')
def health_check():

    try:
        OLLAMA_API = f"{OLLAMA_URL}/api/chat"
        HEADERS = {"Content-Type": "application/json"}
        MODEL = "llama3.2"

        messages = [
            {"role": "system", "content": "You assist users with their random queries"},
            {"role": "user", "content": "Say hello and how your are readg to answer their queries"}
            ]
        
        payload = {
        "model": MODEL,
        "messages": messages,
        "stream": False
        }
    

        response = requests.post(OLLAMA_API, json=payload, headers=HEADERS,
            timeout=30)

        if response.status_code == 200:
            return jsonify({
            "status": "Healthy",
            "ollama_connected": True,
            "model_asnwer": response.json()['message']['content'],
            "timestamp": datetime.now().isoformat()
        })
        else:
            return jsonify({
            "status": "Unhealthy",
            "ollama_connected": False,
            "model_asnwer": "fudged",
            "timestamp": datetime.now().isoformat()
        })
    except Exception as e:
        logger.error(f"Health check failed: {str(e)}")
        return jsonify({
            "status": "unhealthy",
            "error": str(e),
            "timestamp": datetime.now().isoformat()
        }), 500
    

if __name__ == '__main__':
    print("Starting Ollama Flask API...")
    print("API will be available at: http://localhost:5000")
    print("Check health at: http://localhost:5000/aihealth")

    app.run(
        debug=True,
        host='0.0.0.0',
        port=5100
    )