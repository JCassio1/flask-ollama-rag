import requests

def test_ollama():
    try:
        OLLAMA_API = "http://localhost:11434/api/chat"
        HEADERS = {"Content-Type": "application/json"}
        MODEL = "llama3.2"

        messages = [
        {"role": "user", "content": "Say hello in English and Portuguese"}
]
        
        payload = {
        "model": MODEL,
        "messages": messages,
        "stream": False
        }
    

        response = requests.post(OLLAMA_API, json=payload, headers=HEADERS,
            timeout=30)

        if response.status_code == 200:
            print("✅ Ollama is working!")
            print('Response:', response.json()['message']['content'])
        else:
            print("❌ Ollama request failed")
    except Exception as e:
        print("❌ Error:", str(e))
        print("Make sure Ollama is running: ollama serve")

if __name__ == "__main__":
    test_ollama()