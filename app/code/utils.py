#!/usr/bin/env python3

'''
script to define utility functions
'''

import sys
import re
import matplotlib.pyplot as plt
import pandas as pd
import yaml
import requests

FIELDS = 'paperId,url,authors,journal,title,'
FIELDS += 'publicationTypes,publicationDate,citationCount,'
FIELDS += 'publicationVenue,externalIds,abstract'

def add_negative_articles(topic_obj, dic, max_num_articles=10):
    """
    Add the negative articles to the topic object
    """
    if 'negative' not in topic_obj.paper_ids:
        topic_obj.paper_ids['negative'] = {}
    num_topics = len(dic) - 1
    while len(topic_obj.paper_ids["negative"]) < max_num_articles:
        for topic in dic:
            if topic == topic_obj.topic:
                continue
            articles_per_topic = max_num_articles // num_topics
            for paper_id in dic[topic].paper_ids['positive']:
                if paper_id in topic_obj.paper_ids['negative']:
                    continue
                topic_obj.paper_ids['negative'][paper_id]=dic[topic].paper_ids['positive'][paper_id]
                articles_per_topic -= 1
                if articles_per_topic == 0:
                    break
                if len(topic_obj.paper_ids["negative"]) == max_num_articles:
                    break
            if len(topic_obj.paper_ids["negative"]) == max_num_articles:
                break
    print (f'Added {len(topic_obj.paper_ids["negative"])} negative articles for {topic_obj.topic}.')

def update_paper_details(topic_obj):
    """
    Fetch the details of all the papers
    """
    all_paper_ids = list(topic_obj.paper_ids['positive'].keys())
    all_paper_ids += list(topic_obj.paper_ids['negative'].keys())
    all_paper_ids = list(set(all_paper_ids))
    all_paper_data = get_paper_details(all_paper_ids)
    # Check if the paper id matches the paper data
    # If not, change the paper id to the new paper id
    for paper_id, paper_data in zip(all_paper_ids, all_paper_data):
        if paper_id == paper_data['paperId']:
            continue
        print (f'Paper ID {paper_id} does not match {paper_data["paperId"]}.\
               Changing the paper ID.')
        if paper_id in topic_obj.paper_ids['positive']:
            # change the paper id in the positive articles
            topic_obj.paper_ids['positive'][paper_data['paperId']] = \
                            topic_obj.paper_ids['positive'].pop(paper_id)
        elif paper_id in topic_obj.paper_ids['negative']:
            # change the paper id in the negative articles
            topic_obj.paper_ids['negative'][paper_data['paperId']] = \
                            topic_obj.paper_ids['negative'].pop(paper_id)
    return all_paper_data

def add_paper_details(article_obj, article_data):
    """
    Add the details of the article
    """
    article_obj.info.journal = update_journal(
                                article_data['journal'],
                                article_data['publicationVenue'],
                                article_data['externalIds'])
    article_obj.info.title = article_data['title']
    article_obj.info.url = article_data['url']
    article_obj.info.abstract = article_data['abstract']
    article_obj.info.publication_date = article_data['publicationDate']
    article_obj.info.citation_count = article_data['citationCount']
    # print (article_obj.info)

def update_h_index(article_obj, dic):
    """
    Update the h-index of the article based on
    the h-index of its authors
    """
    # print (dic)
    authors_h_index_list = []
    for row in dic:
        if row is None:
            continue
        for author in article_obj.authors:
            author_id = author.author_id
            # print (author_id, row)
            if author_id == row['authorId']:
                author.h_index = row['hIndex']
                author.name = row['name']
                author.citation_count = row['citationCount']
                if row['hIndex'] is None:
                    continue
                authors_h_index_list.append(row['hIndex'])
    if len(authors_h_index_list) == 0:
        authors_avg_h_index = 0
    else:
        authors_avg_h_index = sum(authors_h_index_list) / len(authors_h_index_list)
        authors_avg_h_index = max(authors_h_index_list)
    # article_obj.info.h_index = authors_avg_h_index
    article_obj.info.h_index = authors_avg_h_index

def add_recommendations_to_positive_articles(article_id,
                                             limit=500,
                                             fields=FIELDS):
    """
    Add the recommendations to the positive articles
    """
    endpoint = 'https://api.semanticscholar.org/recommendations/v1/papers/forpaper/'
    endpoint += f'{article_id}'
    params={'fields': fields, 'limit': limit, 'from': 'all-cs'}
    status_code = 0
    while status_code not in [200, 400]:
        # Make a POST request to the paper search batch
        # endpoint with the URL
        search_response = requests.get(endpoint,
                                        params=params,
                                        # json=json,
                                        timeout=None)
        status_code = search_response.status_code
        # print (article_id, status_code)
        if status_code == 400:
            print ('Bad query parameters.',
                    status_code,
                    search_response.json())
            sys.exit()
    return search_response.json()['recommendedPapers']

def update_journal(journal, publication_venue, external_ids):
    """
    Update the journal of the recommended articles
    """
    journal_name = []
    if journal is not None:
        if 'name' in journal:
            # self.journal = journal['name']
            journal_name.append(journal['name'])
    if publication_venue is not None:
        if 'name' in publication_venue:
            # self.journal = publication_venue['name']
            for name in journal_name.copy():
                if publication_venue['name'].lower() == name.lower():
                    continue
                journal_name.append(publication_venue['name'])
    if not journal_name:
        for external_id in external_ids:
            if external_id in ['CorpusId', 'DOI']:
                continue
            journal_name.append(external_id)
    if not journal_name:
        journal_name = None
    else:
        journal_name = list(set(journal_name))
        journal_name = ', '.join(journal_name)
    return journal_name

def add_recommendations(topic_obj,
                        limit=500,
                        fields=FIELDS):
    """
    Add the recommendations to the positive articles

    Args:
        topic_obj (object): object of the topic class

    Returns:
        search_response.json() (dict): dictionary of the search response
    """
    endpoint = 'https://api.semanticscholar.org/recommendations/v1/papers/'
    params = {'fields': fields, 'limit': limit}
    # Select positive articles that have use_for_recommendation set to True
    positive_paper_ids = []
    count = 0
    for paper_id, paper_obj in topic_obj.paper_ids['positive'].items():
        if paper_obj.use_for_recommendation is False:
            continue
        positive_paper_ids.append(paper_id)
        count += 1
        if count == 10:
            break
    json = {
            # 'positivePaperIds': list(topic_obj.paper_ids['positive'].keys())[:10],
            'positivePaperIds': positive_paper_ids,
            'negativePaperIds': list(topic_obj.paper_ids['negative'].keys())[:10],
            }
    status_code = 0
    while status_code not in [200, 400, 404]:
        # Make a POST request to the paper search batch
        # endpoint with the URL
        search_response = requests.post(endpoint,
                                        params=params,
                                        json=json,
                                        timeout=None)
        status_code = search_response.status_code
        if status_code == 400:
            print (f'Bad query parameters for {topic_obj.topic}.',
                    status_code,
                    search_response.json())
            sys.exit()
        elif status_code == 404:
            print (f'Input papers not found for {topic_obj.topic}.',
                    status_code,
                    search_response.json())
            break
    return search_response.json()

def get_paper_details(paper_ids, fields=FIELDS):
    """
    Get the paper details

    Args:
        paper_ids (list): list of paper ids

    Returns:
        search_response.json() (dict): dictionary of the search response
    """
    endpoint = 'https://api.semanticscholar.org/graph/v1/paper/batch'
    params = {'fields': fields}
    json = {'ids': list(paper_ids)}
    status_code = 0
    while status_code != 200:
        # Make a POST request to the paper search batch
        # endpoint with the URL
        search_response = requests.post(endpoint, params=params, json=json, timeout=None)
        status_code = search_response.status_code
    return search_response.json()

def get_author_details(all_authors_ids):
    """
    Get the author details

    Args:
        authors_ids (list): list of authors ids

    Returns:
        authors_details (list): list of authors details
    """
    # Some authors have no ids assigned, and in that case their ID is their name
    # So here we exclude such authors and already prepare their output
    author_details_wo_id = []
    authors_ids = []
    for author_id in all_authors_ids:
        # check if author id contains only alphabets
        if re.fullmatch(r'[A-Za-z ]+', author_id):
            author_details_wo_id.append({'authorId': author_id,
                                    'hIndex': None,
                                    'name': author_id,
                                    'citationCount': None})
            continue
        authors_ids.append(author_id)
    # Loop over every 1000 authors
    authors_details = []
    for start_index in range(0, len(authors_ids), 1000):
        end_index = start_index + 1000
        if end_index > len(authors_ids):
            end_index = len(authors_ids)
        # Get the h-index of the authors
        endpoint = 'https://api.semanticscholar.org/graph/v1/author/batch'
        params={'fields': 'name,hIndex,citationCount'}
        json = {
                'ids': authors_ids[start_index:end_index]
                }
        status_code = 0
        while status_code not in [200, 400]:
            # Make a POST request to the paper search batch
            # endpoint with the URL
            search_response = requests.post(endpoint,
                                            params=params,
                                            json=json,
                                            timeout=None)
            status_code = search_response.status_code
            if status_code == 400:
                print ('Bad query parameters.',
                        status_code,
                        search_response.json())
                sys.exit()
        authors_details += search_response.json()
    authors_details += author_details_wo_id
    return authors_details

def metrics_over_time_js(data) -> plt:
    """
    Return the metrics over time

    Args:
        data (list): list of dictionaries
        category_name (str): category name
        title (str): title of the graph
    
    Returns:
        None

    Example:
    data = [
        {
            'title': 'title1',
            'publicationDate': '2020-01-01',
            'citationCount': 10
        },
        {
            'title': 'title2',
            'publicationDate': '2020-01-01',
            'citationCount': 10
        }
    ]
    """
    dic = {}
    for _, paper_obj in data.items():
        # Exclude the articles with no publication date or citation count
        publication_date = paper_obj.info.publication_date
        if publication_date is None or publication_date == '':
            continue
        citation_count = paper_obj.info.citation_count
        if citation_count is None or citation_count == '':
            continue
        year = publication_date.split('-')[0]
        if year not in dic:
            dic[year] = {'num_articles': 0, 'num_citations': 0}
        dic[year]['num_articles'] += 1
        dic[year]['num_citations'] += citation_count
    # Using noc and yop, plot the line graph with years on x-axis and number of citations on y-axis
    df = pd.DataFrame(dic).T
    # Make another colum for the year
    df['Year'] = df.index
    # Sort by year
    df = df.sort_values(by='Year', ascending=True)
    # print (df)
    return df

def all_citations_js(dic) -> list:
    """
    Return the number of citations for all categories

    Args:
        dic (dict): dictionary of categories

    Returns:
        dic_all_citations (dict): dictionary with the number of citations for all categories

    Example:
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
    """
    dic_all_citations = {}
    for category_name, category_name_items in dic.items():
        sum_citations = 0
        # categories.append(category_name)
        for item in category_name_items['most_cited_articles']:
            if item['citationCount'] is None:
                continue
            sum_citations += int(item['citationCount'])
        # num_citations.append(sum_citations)
        dic_all_citations[category_name] = sum_citations
    return dic_all_citations

# Function to read YAML file
def read_yaml(file_path):
    '''
    Function to read YAML file

    Args:
        file_path (str): path to the YAML file

    Returns:
        dict: data from the YAML file

    Example:
        data = read_yaml('data.yaml')
    '''
    with open(file_path, 'r', encoding='utf-8') as file:
        data = yaml.safe_load(file)
    return data

# Function to write YAML file
def write_yaml(data, file_path):
    '''
    Function to write YAML file

    Args:
        data (dict): data to write to the YAML file
        file_path (str): path to the YAML file

    Returns:
        None

    Example:
        write_yaml(data, 'data.yaml')
    '''
    with open(file_path, 'w', encoding='utf-8') as file:
        yaml.dump(data, file, default_flow_style=False)
