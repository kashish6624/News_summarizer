from newspaper import Article
from newspaper.article import ArticleException


def fetch_article_from_url(url):
    try:
        article = Article(url)

        article.download()
        article.parse()

        return article.text

    except ArticleException as e:
        print("Download blocked:", e)
        return ""

    except Exception as e:
        print("Unexpected error:", e)
        return ""
