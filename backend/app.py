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
    response = generator(prompt, max_length=5, do_sample=True, top_p=0.9, temperature=0.7)  # Adjust parameters
    response_text = response[0]["generated_text"]
    
    return jsonify({"blog": response_text})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)


# from flask import Flask, request, jsonify
# from flask_cors import CORS
# import threading
# from ctransformers import AutoModel

# app = Flask(__name__)
# CORS(app)

# # Load the LLaMA model using ctransformers
# model = AutoModel.from_pretrained("TheBloke/Llama-2-7B-Chat-GGML", model_file="llama-2-7b-chat.ggmlv3.q8_0.bin")

# print("Model loaded successfully!")

# def run_with_timeout(func, args=(), timeout=30):
#     """Runs a function with a timeout using threading."""
#     result = [None]

#     def wrapper():
#         try:
#             result[0] = func(*args)
#         except Exception as e:
#             result[0] = str(e)

#     thread = threading.Thread(target=wrapper)
#     thread.start()
#     thread.join(timeout)

#     if thread.is_alive():
#         return None  # Timeout occurred
#     return result[0]

# @app.route("/generate", methods=["POST"])
# def generate_blog():
#     data = request.json
#     print("Received request:", data)

#     prompt = data.get("prompt", "")
#     if not prompt:
#         return jsonify({"error": "No prompt provided"}), 400

#     try:
#         response_text = model(prompt, max_new_tokens=256)  # Corrected text generation

#         if response_text is None:
#             return jsonify({"error": "Generation timeout"}), 500

#         print("Generated text:", response_text)  # Debugging
#         return jsonify({"blog": response_text})

#     except Exception as e:
#         print("Error:", str(e))  # Debugging
#         return jsonify({"error": str(e)}), 500

# if __name__ == "__main__":
#     app.run(host="0.0.0.0", port=8000, debug=True)
