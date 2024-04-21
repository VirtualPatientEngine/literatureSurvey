#!/usr/bin/env python3
"""
This script demonstrates how to use the Semantic Scholar API to search for papers
and retrieve their details.
"""

from dataclasses import dataclass
from dataclasses import field

@dataclass
class Topic:
    """
    Class to represent a topic
    """
    topic: str
    paper_ids: dict = field(default_factory= lambda: {'positive': {},
                                                      'negative': {},
                                                      'recommended': {}
                                                      })
    limit: int = 500
    def get_all_authors_ids(self):
        """
        Get all the authors of the articles
        """
        all_authors_ids = []
        for _, article_type_values in self.paper_ids.items():
            for _, paper_obj in article_type_values.items():
                all_authors_ids += paper_obj.get_author_ids()
        all_authors_ids = list(set(all_authors_ids))
        print (f'Found {len(all_authors_ids)} authors for {self.topic}.')
        return all_authors_ids
