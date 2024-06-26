# -*- coding: utf-8 -*-
"""Sentiment Analysis

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1RQYXZe_Gw4okbUaEBjBrLIbcRIyiYDGn
"""

pip install transformers torch

import torch
from transformers import BertTokenizer, BertForSequenceClassification

# Load pre-trained BERT model and tokenizer
model_name = 'bert-base-uncased'
tokenizer = BertTokenizer.from_pretrained(model_name)
model = BertForSequenceClassification.from_pretrained(model_name)

# Function to predict sentiment
def predict_sentiment(text):
    # Tokenize text
    inputs = tokenizer(text, return_tensors='pt')

    # Perform forward pass to obtain logits
    outputs = model(**inputs)
    logits = outputs.logits

    # Compute softmax to get probabilities
    probs = torch.softmax(logits, dim=-1)

    # Determine predicted label (0 = negative, 1 = positive)
    predicted_label = torch.argmax(probs, dim=-1).item()

    # Map predicted label to sentiment
    sentiment = "positive" if predicted_label == 1 else "negative"

    return sentiment

# Example usage:
text1 = "I love this product! It's amazing."
text2 = "This movie was terrible. I hated it."

sentiment1 = predict_sentiment(text1)
sentiment2 = predict_sentiment(text2)

print(f"Sentiment of '{text1}': {sentiment1}")
print(f"Sentiment of '{text2}': {sentiment2}")