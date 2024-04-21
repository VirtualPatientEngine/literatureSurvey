#!/usr/bin/env python3
"""
Test the Author class
"""

from app.code.author import Author

def test_author() -> None:
    """
    Test the Author class
    """
    author_name = "Gurdeep Singh"
    author_id = "122085692"
    author_obj = Author(author_id, author_name=author_name)
    assert author_obj.author_name == author_name
    assert author_obj.author_id == author_id
