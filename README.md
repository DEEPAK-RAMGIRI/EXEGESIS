BART (Bidirectional and Auto-Regressive Transformers) is a sequence-to-sequence model developed by Facebook AI. It is designed for tasks like text summarization, translation, question answering, and text generation. BART combines the strengths of BERT (bidirectional encoder that understands context) and GPT (autoregressive decoder that generates text). Because of this, it is very effective at abstractive summarization (rephrasing text in new words instead of just extracting sentences).

1. Loading the model and tokenizer

We first load the pre-trained model and tokenizer from Hugging Face’s Transformers library. The model (facebook/bart-large-cnn) is already fine-tuned on large summarization datasets like CNN/DailyMail, which makes it good at creating short summaries of news or articles. The tokenizer converts normal text into tokens (smaller units of words) and then into token IDs (numbers the model understands). Without the tokenizer, the model cannot process the text input.

2. Preparing the input text

Next, we define the input text (the paragraph we want to summarize). This text is then encoded using the tokenizer. During encoding, the text is split into tokens, and each token is mapped to a number (token ID). We also set parameters such as max_length (maximum tokens allowed for input) and truncation (cutting extra text if it is too long). The result is a tensor (a structured array used by deep learning models) that can be passed into BART.

3. Generating the summary

Now, the encoded input is given to the model’s generate() function, which creates the summary step by step. The generation process can be controlled with parameters:

max_length (maximum number of tokens in the output)

min_length (minimum number of tokens in the output)

num_beams (beam search, meaning the model explores multiple candidate summaries and keeps the best one)

length_penalty (penalizes very long or very short summaries to keep them balanced)

early_stopping (stops generation when an optimal summary is found early)

4. Decoding and output

Finally, the model outputs the summary in the form of token IDs (numbers). We use the tokenizer’s decode() function to convert these numbers back into human-readable text. The result is a clean and meaningful summary that captures the essence of the original text. In this way, BART acts like a powerful reader and rewriter—it understands the long text deeply and then rewrites it in a concise, fluent manner.