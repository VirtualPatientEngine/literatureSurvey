#!/usr/bin/env python3
"""
Test the Author class
"""

from app.code.article import Article
from app.code.author import Author

def test_article():
    """
    Test the Article class
    """
    article_id = "XYZ"
    authors = [Author("A"), Author("B")]
    article_obj = Article(article_id)
    article_obj.authors = authors
    article_obj.recommended_articles = [Article("P"), Article("Q")]
    assert article_obj.get_author_ids() == ['A', 'B']
    assert not article_obj.get_recommened_articles_authors_ids()
