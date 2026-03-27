import os
os.environ["TOKENIZERS_PARALLELISM"] = "false"

from transformers import pipeline

# GLOBAL MODEL (loads once)
summarizer = None


def get_model():
    global summarizer

    if summarizer is None:
        print("Loading summarization model...")

        summarizer = pipeline(
            "summarization",
            model="sshleifer/distilbart-cnn-12-6",
            device=-1,      # CPU only
            framework="pt"
        )

    return summarizer


def summarize_text(article_text):
    model = get_model()

    # LIMIT INPUT SIZE (VERY IMPORTANT FOR RENDER MEMORY)
    article_text = article_text[:1200]

    result = model(
        article_text,
        max_length=200,
        min_length=80,
        do_sample=False
    )

    return result[0]["summary_text"]
