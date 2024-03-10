#!/usr/bin/env python3

'''
script to define utility functions
'''

import matplotlib.pyplot as plt
import pandas as pd
import yaml

#A26, B1

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
    for paper in data:
        # Exclude the articles with no publication date or citation count
        publication_date = paper['publicationDate']
        if publication_date is None or publication_date == '':
            continue
        citation_count = paper['citationCount']
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
