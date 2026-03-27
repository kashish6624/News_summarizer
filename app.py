from flask import Flask, render_template, request, redirect
from summarizer import summarize_text
from fetcher import fetch_article_from_url
from models import db, ArticleHistory
import os


app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///history.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

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
            summary = summarize_text(article_text)

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
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
