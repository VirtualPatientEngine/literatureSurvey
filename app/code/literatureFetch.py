#!/usr/bin/env python3

'''
This script demonstrates how to use the Semantic Scholar API to search for papers 
and retrieve their details.
'''

import requests
import time
from jinja2 import Environment, FileSystemLoader
import markdownify
import utils

# Define the paper search endpoint URL
URL = 'https://api.semanticscholar.org/graph/v1/paper/search/bulk'
# Define the required query parameter and its value
# (in this case, the keyword we want to search for)
BASE_PARAMS = {
    # 'limit': 5,
    'publicationTypes': 'JournalArticle',
    # 'year': '2020-',
    'fields': 'paperId,url,journal,\
               title,publicationTypes,publicationDate,\
               citationCount,publicationVenue',
    # 'sort': 'citationCount:desc',
    'token': None
}
N = 10
DIC = {}

def fetch_articles(search_query,
                   sort='citationCount:desc') -> list:
    """
    Return the most cited articles for a given query

    Args:
        query (str): query to search for
    Returns:
        list: list of articles
    """
    query_params = BASE_PARAMS.copy()
    query_params['query'] = search_query
    query_params['sort'] = sort

    fetched_data = []
    while True:
        status_code_429 = 0
        while True:
            # Make the GET request to the paper search endpoint with the URL and query parameters
            search_response = requests.get(URL, params=query_params, timeout=None)
            print ('status code', search_response.status_code)
            # WHen the status code is 429, sleep for 5 minutes
            if search_response.status_code == 429:
                status_code_429 += 1
                if status_code_429 > 10:
                    print ('Too many requests!')
                    print ('Sleeping for 5 minutes and 10 seconds....')
                    time.sleep(310)
                    continue
            # When the status code is 200, break the loop
            if search_response.status_code == 200:
                break
        search_response_json = search_response.json()
        fetched_data += search_response_json['data']
        # End the loop if we have fetched enough data
        # or if there is no more data to fetch
        if len(fetched_data) >= N or search_response_json['token'] is None:
            break
        # Update the token to fetch the next page of data
        # if the token is not None
        if search_response_json['token'] is not None:
            query_params['token'] = search_response_json['token']
    return fetched_data

def create_template(template_file, category_name) -> str:
    """
    Return the markdown content for a given template

    Args:
        template_file (str): template file
        most_cited_articles (list): list of most cited articles
        most_recent_articles (list): list of most recent articles
    Returns:
        str: markdown content
    """
    # Set the template environment
    environment = Environment(loader=FileSystemLoader("../../templates/"))
    # Get the template
    template = environment.get_template(template_file)
    # Render the template
    content = template.render(
        most_cited_articles=DIC[category_name]['most_cited_articles'][0:N],
        most_recent_articles=DIC[category_name]['most_recent_articles'][0:N],
        category_name=category_name,
        title=DIC[category_name]['title'],
        query=DIC[category_name]['query'],
        hide_nav="---\nhide:\n\t- navigation---\n",
    )
    return markdownify.markdownify(content)

def main():
    """
    Main function

    Args:
        None

    Returns:
        None
    """
    # Work with all the categories in the file
    with open('../data/query.tsv', 'r', encoding='utf-8') as f:
        for line in f:
            if line.split('\t')[0] == 'Title':
                continue
            print (line.split('\t'))
            title = line.split('\t')[0]
            query = line.split('\t')[1].rstrip()
            category_name = title.replace(' ', '_')
            ################################
            ## Fetch the most cited articles
            data = fetch_articles(query)
            DIC[category_name] = {'title': title, 'query': query, 'most_cited_articles': data}
            plot = utils.metrics_over_time(data, category_name, title)
            plot.savefig(f'../../docs/assets/{category_name}.png')
            ################################
            ## Fetch the most recent articles
            data = fetch_articles(query, sort = 'publicationDate:desc')
            DIC[category_name]['most_recent_articles'] = data
            # print (data[0])
            markdown_text = create_template("category.txt", category_name)
                                            # DIC[category_name]['most_cited_articles'][0:N],
                                            # DIC[category_name]['most_recent_articles'][0:N])
            # Add the hide navigation
            markdown_text = "---\nhide:\n - navigation\n---\n" + markdown_text
            # Write the markdown text to a file
            with open(f'../../docs/{category_name}.md', 'w', encoding='utf-8') as file:
                file.write(markdown_text)
            ################################

    # End of file
    title = 'All'
    query = ' | '.join([category_items['query'] for _, category_items in DIC.items()])
    category_name = 'All'
    ################################
    ## Fetch the most cited articles
    data = fetch_articles(query)
    DIC[category_name] = {'title': title, 'query': query, 'most_cited_articles': data}
    plot = utils.metrics_over_time(data, category_name, title)
    plot.savefig(f'../../docs/assets/{category_name}.png')
    ################################
    ## Fetch the most recent articles
    data = fetch_articles(query, sort = 'publicationDate:desc')
    DIC[category_name]['most_recent_articles'] = data
    # print (data[0])
    markdown_text = create_template("category.txt", category_name)
                                    # DIC[category_name]['most_cited_articles'][0:N],
                                    # DIC[category_name]['most_recent_articles'][0:N])
    # Add the hide navigation
    markdown_text = "---\nhide:\n - navigation\n---\n" + markdown_text
    # Write the markdown text to a file
    with open(f'../../docs/{category_name}.md', 'w', encoding='utf-8') as file:
        file.write(markdown_text)
    ################################

if __name__ == '__main__':
    # Run the main function
    main()
