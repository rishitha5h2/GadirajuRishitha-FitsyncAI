from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline

# Load the model and tokenizer
model_name = "microsoft/DialoGPT-medium"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

# Define chatbot function
def chatbot_response(user_input):
    input_ids = tokenizer.encode(user_input + tokenizer.eos_token, return_tensors="pt")
    response_ids = model.generate(input_ids, max_length=1000, pad_token_id=tokenizer.eos_token_id)
    response_text = tokenizer.decode(response_ids[:, input_ids.shape[-1]:][0], skip_special_tokens=True)
    return response_text

# Test chatbot
user_input = "Can you suggest me a diet plan?"
response = chatbot_response(user_input)
print("Chatbot:", response)
