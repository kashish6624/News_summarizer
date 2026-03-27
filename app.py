from flask import Flask, render_template, request, redirect
from summarizer import NewsSummarizer
from fetcher import fetch_article_from_url
from models import db, ArticleHistory

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///history.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

summarizer = NewsSummarizer()

# Create DB automatically
with app.app_context():
    db.create_all()


@app.route("/", methods=["GET", "POST"])
def index():
    summary = ""

    if request.method == "POST":
        url = request.form["url"]

        article_text = fetch_article_from_url(url)

        if article_text.strip():
            summary = summarizer.summarize(article_text)

            # SAVE TO HISTORY
            record = ArticleHistory(url=url, summary=summary)
            db.session.add(record)
            db.session.commit()

    return render_template("index.html", summary=summary)


# HISTORY PAGE
@app.route("/history")
def history():
    articles = ArticleHistory.query.order_by(
        ArticleHistory.created_at.desc()
    ).all()

    return render_template("history.html", articles=articles)


if __name__ == "__main__":
    app.run(debug=True)








# from summarizer import NewsSummarizer
# from fetcher import fetch_article_from_url

# if __name__ == "__main__":
#     url = input("Enter news article URL: ")

#     print("\nFetching article...")
#     article_text = fetch_article_from_url(url)

#     if len(article_text.strip()) == 0:
#         print("Failed to extract article text.")
#         exit()

#     summarizer = NewsSummarizer()
#     summary = summarizer.summarize(article_text)

#     print("\n===== ARTICLE SUMMARY =====\n")
#     print(summary)
