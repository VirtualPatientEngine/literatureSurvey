#!/usr/bin/env python3

'''
script to define utility functions
'''

import matplotlib.pyplot as plt
import pandas as pd
import yaml

def metrics_over_time(data, category_name, title) -> plt:
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
        publication_date = paper['publicationDate']
        if publication_date is None or publication_date == '':
            continue
        year = publication_date.split('-')[0]
        if year not in dic:
            dic[year] = {'num_articles': 0, 'num_citations': 0}
        dic[year]['num_articles'] += 1
        citation_count = paper['citationCount']
        if citation_count is None or citation_count == '':
            continue
        dic[year]['num_citations'] += citation_count
    # Using noc and yop, plot the line graph with years on x-axis and number of citations on y-axis
    df = pd.DataFrame(dic).T
    # Make another colum for the year
    df['Year'] = df.index
    # Sort by year
    df = df.sort_values(by='Year', ascending=True)
    # Plot the graph
    ax = df.plot(x='Year', y='num_articles', kind='line', color='b', legend=False)
    ax.set(xlabel='Year', ylabel='Number of Articles')
    # Set the second y-axis
    ax2 = plt.twinx()
    df.plot(x='Year', y='num_citations', kind='line', color='r', ax=ax2, legend=False)
    ax2.set(ylabel='Number of Citations')
    # plot legend inside the graph and set its text
    ax.figure.legend(loc='upper center', ncol=2)
    # Set the title with bold font
    # plt.title(f'{title} Articles and Citations Over Time')
    # Set grid lines with a dashed style, thickness of 0.5, color grey and transparency of 0.5
    # and only vertical lines
    ax.grid(axis='x', linestyle='--', linewidth=0.5, color='grey', alpha=0.5)
    # Remove top and bottom spines
    ax.spines['top'].set_visible(False)
    ax2.spines['top'].set_visible(False)
    # Make sure the figure doesn't get cut off
    plt.tight_layout()
    # Save the graph
    return plt
    

    #A26, B1

def metrics_over_time_js(data, category_name, title) -> plt:
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
        publication_date = paper['publicationDate']
        if publication_date is None or publication_date == '':
            continue
        year = publication_date.split('-')[0]
        if year not in dic:
            dic[year] = {'num_articles': 0, 'num_citations': 0}
        dic[year]['num_articles'] += 1
        citation_count = paper['citationCount']
        if citation_count is None or citation_count == '':
            continue
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
    """
    categories = []
    num_citations = []
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
    with open(file_path, 'r') as file:
        data = yaml.safe_load(file)
    return data

# Function to write YAML file
def write_yaml(data, file_path):
    with open(file_path, 'w') as file:
        yaml.dump(data, file, default_flow_style=False)
