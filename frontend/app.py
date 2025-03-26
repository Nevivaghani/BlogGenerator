from flask import Flask
from flask_cors import CORS
from routes import generate_bp  # Import routes

app = Flask(__name__)
CORS(app)

# Register blueprints
app.register_blueprint(generate_bp)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)