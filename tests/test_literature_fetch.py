"""Test Uniprot class functions"""

import os
import pandas as pd
from bs4 import BeautifulSoup
from app.code import literature_fetch, utils

def test_fetch_articles() -> None:
    """Test fetch_articles function"""
    search_query="Attention"
    articles = literature_fetch.fetch_articles(search_query)
    assert articles[0]['title'] == "Attention is All you Need"

def test_manually_curated_articles() -> None:
    """Test fetch_manually_curates_articles function"""
    curated_file = 'app/data/manually_curated_articles.tsv'
    articles = literature_fetch.fetch_manually_curated_articles(curated_file)
    assert len(articles) > 0

def test_metrics_over_time_js() -> pd.DataFrame:
    """Test metrics_over_time function"""
    data = [
        {
            'title': 'title1',
            'publicationDate': '2020-01-01',
            'citationCount': 10
        },
        {
            'title': 'title2',
            'publicationDate': '2019-01-01',
            'citationCount': None
        },
        {
            'title': 'title3',
            'publicationDate': None,
            'citationCount': 30
        }
    ]
    df = utils.metrics_over_time_js(data)
    assert df['num_citations'].iloc[0] == 10

def test_all_citations_js() -> dict:
    """Test all_citations function"""
    dic = {
        'category1': {
            'most_cited_articles': [
                {
                    'title': 'title1',
                    'citationCount': 10
                },
                {
                    'title': 'title2',
                    'citationCount': None
                },
                {
                    'title': 'title3',
                    'citationCount': 20
                }
            ]
        },
        'category2': {
            'most_cited_articles': [
                {
                    'title': 'title1',
                    'citationCount': 10
                },
                {
                    'title': 'title2',
                    'citationCount': 10
                }
            ]
        }
    }
    dic_all_citations = utils.all_citations_js(dic)
    assert dic_all_citations['category1'] == 30

def test_read_yaml() -> None:
    """Test read_yaml function"""
    file_path = "base.yml"
    data = utils.read_yaml(file_path)
    assert 'theme' in data

def test_write_yaml() -> None:
    """Test write_yaml function"""
    data = utils.read_yaml('base.yml')
    utils.write_yaml(data, "test.yml")
    data = utils.read_yaml("test.yml")
    # Delete test.yml
    os.remove("test.yml")
    assert 'theme' in data

def assert_keyword_in_html(html_content, keyword):
    """Assert that a keyword is in the HTML content"""
    soup = BeautifulSoup(html_content, 'html.parser')
    # Find all occurrences of the keyword in the HTML content
    occurrences = soup.find_all(string=lambda text: keyword in str(text))
    return occurrences

def test_create_template() -> None:
    """Test create_template function"""
    df = pd.DataFrame({
        'Year': ['2020-01-01', '2019-01-01'],
        'num_citations': [10, 20],
        'num_articles': [10, 20]
    })
    dic = {
        'category1': {
            'most_cited_articles': [
                {
                    'title': 'title1',
                    'citationCount': 10
                },
                {
                    'title': 'title2',
                    'citationCount': 10
                }
            ],
            'most_recent_articles': [
                {
                    'title': 'title1',
                    'publicationDate': '2020-01-01',
                    'citationCount': 10
                },
                {
                    'title': 'title2',
                    'publicationDate': '2019-01-01',
                    'citationCount': 20
                }
            ],
            'manually_curated_articles': [
                {
                    'title': 'title1',
                    'publicationDate': '2019-03-01',
                    'citationCount': 1
                },
                {
                    'title': 'title2',
                    'publicationDate': '2015-10-01',
                    'citationCount': 0
                }
            ],
            'title': 'title1',
            'query': 'query1'
        }
    }
    html = literature_fetch.create_template(
                                            ("templates/","category.txt"),
                                            "category1",
                                            dic,
                                            df)
    occurrences = assert_keyword_in_html(html, "title1")
    assert occurrences

    dic2 = {
        'category1': 20,
        'category2': 30
    }
    html = literature_fetch.create_template(
                                            ("templates/","overview.txt"),
                                            "category1",
                                            dic,
                                            df,
                                            dic_all_citations=dic2)
    occurrences = assert_keyword_in_html(html, "title1")
    assert occurrences
