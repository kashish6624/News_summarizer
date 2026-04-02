import os
os.environ["TOKENIZERS_PARALLELISM"] = "false"

from huggingface_hub import InferenceClient

# Create client ONCE (global)
client = InferenceClient(
    model="facebook/bart-large-cnn",
    token=os.getenv("HF_TOKEN")   # secure token
)


def summarize_text(article_text):

    # limit input size (important)
    article_text = article_text[:1200]

    result = client.summarization(
        article_text,
        max_length=200,
        min_length=80
    )

    return result["summary_text"]
