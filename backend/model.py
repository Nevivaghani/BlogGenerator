from transformers import pipeline
import config

print("Loading model...")
generator = pipeline(
    "text-generation",
    model=config.MODEL_NAME,
    device_map="auto"
)
print("Model loaded successfully!")
