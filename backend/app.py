from flask import Flask, request, jsonify
from flask_cors import CORS
from transformers import pipeline

app = Flask(__name__)
CORS(app)

print("Loading model...")
generator = pipeline("text-generation", model="meta-llama/Llama-2-7b-chat-hf", device_map="auto")  # Use pipeline
print("Model loaded successfully!")

@app.route("/generate", methods=["POST"])
def generate_blog():
    data = request.json
    prompt = data.get("prompt", "")
    
    print("Generating response...")
    # response = generator(prompt, max_length=5, do_sample=True, top_p=0.9, temperature=0.7)  # Adjust parameters
    response = generator(prompt, max_length=5, truncation=True, do_sample=True, top_p=0.9, temperature=0.7)
    response_text = response[0]["generated_text"]
    
    return jsonify({"blog": response_text})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)


