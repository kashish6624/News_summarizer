from transformers import pipeline

summarizer = None   # global model


def get_model():
    global summarizer

    if summarizer is None:
        summarizer = pipeline(
            "summarization",
            model="sshleifer/distilbart-cnn-12-6",
            device=-1   # CPU only
        )

    return summarizer


def summarize_text(article_text):
    model = get_model()

    result = model(
        article_text[:1500],
        max_length=300,
        min_length=150,
        do_sample=False
    )

    return result[0]["summary_text"]
