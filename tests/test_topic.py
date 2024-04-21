#!/usr/bin/env python3
"""
Test the Topic class
"""

from app.code.topic import Topic
from app.code.article import Article

def test_topic():
    """
    Test the Topic class
    """
    topic_name = "topic1"
    paper_ids = {
        'positive': {
            'A': Article("A"),
            'B': Article("B")
        },
        'recommended': {
            'P': Article("P"),
            'Q': Article("Q")
        }
    }
    topic_obj = Topic(topic_name)
    topic_obj.paper_ids = paper_ids
    print (topic_obj.get_all_authors_ids)
    assert not topic_obj.get_all_authors_ids()
