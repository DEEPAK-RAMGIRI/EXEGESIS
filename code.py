from transformers import BartTokenizer, BartForConditionalGeneration

# Load pre-trained BART model and tokenizer
model_name = "facebook/bart-large-cnn"
tokenizer = BartTokenizer.from_pretrained(model_name)
model = BartForConditionalGeneration.from_pretrained(model_name)

# Input text to be summarized
input_text = """
Artificial Intelligence (AI) is transforming the world at an unprecedented pace.
From healthcare and finance to education and entertainment, AI applications are everywhere.
In healthcare, AI helps doctors diagnose diseases faster and more accurately.
In finance, it detects fraud and manages investments.
In education, AI-powered platforms personalize learning for students.
However, AI also raises concerns, such as job loss due to automation, data privacy issues, and the ethical use of algorithms.
Despite these challenges, experts believe AI will continue to grow and shape the future in unimaginable ways.
"""

# Tokenize and summarize the input text using BART
inputs = tokenizer.encode("summarize: " + input_text, return_tensors="pt", max_length=1024, truncation=True)
summary_ids = model.generate(inputs, max_length=100, min_length=50, length_penalty=2.0, num_beams=4, early_stopping=True)

# Decode and output the summary
summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
print("Original Text:")
print(input_text)
print("\nSummary:")
print(summary)