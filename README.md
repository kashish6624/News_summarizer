# AI News Article Summarizer

An NLP-powered web application that automatically extracts and summarizes news articles from a URL using state-of-the-art Transformer models.

---

## Project Overview

This project allows users to paste a news article URL and instantly generate a concise summary using Natural Language Processing.

The application:

* Extracts article text from online news websites
* Processes long articles using chunking
* Generates summaries using Facebook's BART Transformer model
* Displays results through a simple Flask web interface

---

## Technologies Used

* Python
* Flask
* HuggingFace Transformers
* BART Large CNN Model
* Newspaper3k

---

## How It Works

1. User enters a news article URL
2. Article text is extracted using Newspaper3k
3. Long text is divided into chunks
4. Each chunk is summarized using a Transformer model
5. Summaries are combined and displayed

---

## Features

* Automatic news scraping
* Transformer-based abstractive summarization
* Handles long articles
* Clean web interface
* Beginner-friendly NLP project

---

## Future Improvements

* Multi-language support
* Model selection options
* Article keyword extraction
* Deploy on Render / HuggingFace Spaces

