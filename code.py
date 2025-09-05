# ============================
# Step 1: Install & Import
# ============================
!pip install transformers sentencepiece nltk scikit-learn matplotlib

import nltk
nltk.download("punkt")
nltk.download("punkt_tab")  # needed for sentence tokenization
nltk.download("stopwords")

from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from transformers import pipeline
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# ============================
# Step 2: Input Text
# ============================
text = """
Artificial Intelligence (AI) is transforming the world.
From healthcare to transportation, AI systems are helping improve efficiency,
reduce costs, and even save lives. However, AI also raises important questions
about ethics, bias, and job displacement. Experts believe AI will continue to
grow rapidly in the coming decade.
"""

# ============================
# Step 3: Preprocessing
# ============================
words = word_tokenize(text.lower())
stop_words = set(stopwords.words("english"))
filtered_words = [w for w in words if w.isalnum() and w not in stop_words]

print("🔹 Step 3: Preprocessed Words (after cleaning):")
print(filtered_words)

# ============================
# Step 4: Feature Extraction (TF-IDF)
# ============================
sentences = sent_tokenize(text)
vectorizer = TfidfVectorizer(stop_words="english")
X = vectorizer.fit_transform(sentences)

df_tfidf = pd.DataFrame(X.toarray(), columns=vectorizer.get_feature_names_out(), index=sentences)
print("\n🔹 Step 4: TF-IDF Feature Matrix (rows=sentences, cols=words):\n")
print(df_tfidf)

# ============================
# Step 5: Sentence Scoring
# ============================
scores = np.array(X.sum(axis=1)).ravel()

print("\n🔹 Step 5: Sentence Scores:")
for sent, score in zip(sentences, scores):
    print(f"Score={score:.3f} | {sent}")

# 🔸 Visualization of scores
plt.figure(figsize=(8,4))
plt.barh(range(len(sentences)), scores, color="skyblue")
plt.yticks(range(len(sentences)), sentences)
plt.xlabel("Importance Score")
plt.title("Sentence Importance (TF-IDF Scores)")
plt.show()

# ============================
# Step 6: Extractive Summary
# ============================
top_n = 2
top_sentence_idx = scores.argsort()[-top_n:][::-1]
extractive_summary = " ".join([sentences[i] for i in top_sentence_idx])

print("\n🔹 Step 6: Extractive Summary:\n", extractive_summary)

# ============================
# Step 7: Abstractive Summary (BART)
# ============================
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

abstractive_summary = summarizer(
    extractive_summary,
    max_length=50,
    min_length=15,
    do_sample=False
)

print("\n🔹 Step 7: Abstractive Summary:\n", abstractive_summary[0]['summary_text'])
