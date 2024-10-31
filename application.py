from flask import Flask, render_template, request, jsonify
from transformers import GPT2LMHeadModel, GPT2Tokenizer
import torch

# Initialize the Flask app
app = Flask(__name__)

# Load the fine-tuned model and tokenizer
model_path = "model/fine_tuned_emergency_bot_new"
tokenizer = GPT2Tokenizer.from_pretrained(model_path)
model = GPT2LMHeadModel.from_pretrained(model_path)

# Set pad_token_id to eos_token_id to prevent warnings
tokenizer.pad_token = tokenizer.eos_token

# Function to generate response from the model
def generate_response(prompt):
    inputs = tokenizer(prompt, return_tensors="pt", padding=True, truncation=True)
    outputs = model.generate(
        inputs["input_ids"], 
        attention_mask=inputs["attention_mask"], 
        max_length=300,  # Increase max_length to 300 or your desired length
        num_return_sequences=1, 
        do_sample=True, 
        top_k=50,
        pad_token_id=tokenizer.eos_token_id
    )
    return tokenizer.decode(outputs[0], skip_special_tokens=True)

# Define the homepage route
@app.route('/')
def home():
    return render_template("index.html")

# Define the route to get the response from the model
@app.route('/get_response', methods=['POST'])
def get_response():
    user_input = request.json.get("user_input", "")
    response_text = generate_response(user_input)
    return jsonify({"response": response_text})

if __name__ == "__main__":
    app.run(debug=True)