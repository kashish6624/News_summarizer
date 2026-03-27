from newspaper import Article

def fetch_article_from_url(url):
    article = Article(url)
    article.download()
    article.parse()
    return article.text
