#!/usr/bin/env python3

'''
This script demonstrates how to use the Semantic Scholar API to search for authors.
'''
from dataclasses import dataclass
from typing import Optional

@dataclass
class Author:
    """
    Class to represent an author
    """
    author_id: str
    author_name: Optional[str] = None
    h_index: Optional[int] = None
    citation_count: Optional[int] = None
