from transformers import pipeline

class NewsSummarizer:
    def __init__(self):
        self.summarizer = pipeline(
            "summarization",
            model="sshleifer/distilbart-cnn-12-6""
        )
        
    def chunk_text(self, text, max_chars=3000):
        chunks = []
        for i in range(0, len(text), max_chars):
            chunks.append(text[i:i + max_chars])
        return chunks
    
    def summarize(self, article_text):
        chunks = self.chunk_text(article_text)

        summaries = []
        for chunk in chunks:
            summary = self.summarizer(
                chunk,
                max_length=300,
                min_length=150,
                do_sample=False
            )
            summaries.append(summary[0]["summary_text"])

        # Final combined summary
        return " ".join(summaries)
