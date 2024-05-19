#!/usr/bin/env python3

'''
This script demonstrates how to use the Semantic Scholar API to search for papers
'''
from dataclasses import dataclass

@dataclass
class Info:
    '''
    Class to represent the information of the article
    '''
    journal: str = None
    title: str = None
    abstract: str = None
    url: str = None
    publication_date: str = None
    citation_count: int = None
    h_index: int = None

class Article:
    """
    Class to represent articles
    """
    def __init__(self, article_id, use_for_recommendation=False):
        self.article_id = article_id
        self.use_for_recommendation = use_for_recommendation
        self.authors = []
        self.info = Info()
        self.recommended_articles = []
    def get_author_ids(self):
        """
        Get the author ids
        """
        author_ids = []
        for author in self.authors:
            author_ids.append(author.author_id)
        return author_ids
    def get_recommened_articles_authors_ids(self):
        """
        Get the author ids of the recommended articles
        """
        authors_ids = []
        for article in self.recommended_articles:
            authors_ids += article.get_author_ids()
        return authors_ids
