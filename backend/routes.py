from flask import Blueprint, request, jsonify
from model import generator
import config

generate_bp = Blueprint("generate", __name__)

@generate_bp.route("/generate", methods=["POST"])
def generate_blog():
    data = request.json
    prompt = data.get("prompt", "")

    print("Generating response...")
    response = generator(
        prompt,
        max_length=config.MAX_LENGTH,
        do_sample=True,
        top_p=config.TOP_P,
        temperature=config.TEMPERATURE
    )
    response_text = response[0]["generated_text"]

    return jsonify({"blog": response_text})
