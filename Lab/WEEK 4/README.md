WEEK 4 - Comparison of BPE, WordPiece and SentencePiece Tokenizers

This experiments compares BPE, WordPiece and SentencePiece tokenizers using English, Telugu and Hindi texts.

In this experiment, the same sentences in three different languages are processed using GPT‑2 (BPE), Multilingual BERT (WordPiece) and XLM‑R (SentencePiece). 
The program displays the generated tokens, token IDs and token counts for each tokenizer.
By comparing the outputs, we can observe how different tokenization techniques handle multilingual text.

Requirements: Python 3.14, transformers, sentencepiece

Setup:
1. Create and activate a virtual environment
2. Install dependencies using pip install -r requirements.txt.

Run: python tokenizer_comparison.py

Input: English, Telugu and Hindi sentences provided in the code.

Output: Tokens, Token IDs and Token Counts produced by GPT‑2, Multilingual BERT and XLM‑R tokenizers.
