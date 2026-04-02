import os
os.environ["TOKENIZERS_PARALLELISM"] = "false"

from huggingface_hub import InferenceClient

# Create client ONCE (global)
client = InferenceClient(
    model="facebook/bart-large-cnn",
    token=os.getenv("HF_TOKEN")   # secure token
)


def summarize_text(article_text):

    article_text = article_text[:1200]

    result = client.summarization(
        article_text,
        parameters={
            "max_length": 200,
            "min_length": 80,
            "do_sample": False
        }
    )

    return result["summary_text"]
