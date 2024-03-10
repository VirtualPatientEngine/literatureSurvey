#!/usr/bin/env python3

'''
This script demonstrates how to use the Semantic Scholar API to search for papers 
and retrieve their details.
'''

import time
import requests
from jinja2 import Environment, FileSystemLoader
import utils

# Define the paper search endpoint URL
URL = 'https://api.semanticscholar.org/graph/v1/paper/search/bulk'
# Define the required query parameter and its value
# (in this case, the keyword we want to search for)
FIELDS = 'paperId,url,authors,journal,title,'
FIELDS += 'publicationTypes,publicationDate,citationCount,'
FIELDS += 'publicationVenue'
BASE_PARAMS = {
    # 'limit': 5,
    'publicationTypes': 'JournalArticle',
    # 'year': '2020-',
    'fields': FIELDS,
    # 'sort': 'citationCount:desc',
    'token': None
}
N = 7
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
        while True:
            # Make the GET request to the paper search endpoint with the URL and query parameters
            search_response = requests.get(URL, params=query_params, timeout=None)
            # When the status code is 200, break the loop
            if search_response.status_code != 200:
                print ('status code', search_response.status_code)
                print ('Retrying....')
            else:
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
    # fix the publicationVenue and journal
    for paper in fetched_data:
        # print (paper)
        publication_venue = paper['publicationVenue']
        # if publication_venue is None:
        #     paper['publicationVenue'] = 'NotAvbl'
        # elif 'name' in publication_venue:
        #     paper['publicationVenue'] = publication_venue['name']
        # else:
        #     paper['publicationVenue'] = 'NotAvbl'
        paper['publicationVenue'] = publication_venue.get('name', 'NotAvbl')\
                                    if publication_venue is not None else 'NotAvbl'
        journal = paper['journal']
        paper['journal'] = journal.get('name', 'NotAvbl') if journal is not None else 'NotAvbl'

        # if journal is None:
        #     paper['journal'] = 'NotAvbl'
        # elif 'name' in journal:
        #     paper['journal'] = journal['name']
        # else:
        #     paper['journal'] = 'NotAvbl'
        # Set journal to publicationVenue if journal is not available
        if paper['journal'] == 'NotAvbl':
            paper['journal'] = paper['publicationVenue']
        # Set authors to NotAvbl if authors are not available
        authors = []
        for author in paper['authors']:
            authors.append(author['name'])
        if len(authors) == 0:
            authors = ['NotAvbl']
        paper['authors'] = ', '.join(authors)
    return fetched_data

def create_template(template_file, category_name, df, dic_all_citations=None) -> str:
    """
    Return the markdown content for a given template

    Args:
        template_file (str): template file
        category_name (str): category name
        df (pd.DataFrame): dataframe with the metrics over time
        dic_all_citations (dict): dictionary with the number of citations for all categories
    Returns:
        str: markdown content
    """
    # Set the template environment
    environment = Environment(loader=FileSystemLoader("../../templates/"))
    # Get the template
    template = environment.get_template(template_file)
    if dic_all_citations is None:
        categories = None
        num_citations_across_categories = None
    else:
        categories = []
        num_citations_across_categories = []
        for category, num_citations_categories in dic_all_citations.items():
            if category == category_name:
                continue
            categories.append(category)
            num_citations_across_categories.append(num_citations_categories)
    
    # Render the template
    content = template.render(
        # current time
        current_time=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
        most_cited_articles=DIC[category_name]['most_cited_articles'][0:N],
        most_recent_articles=DIC[category_name]['most_recent_articles'][0:N],
        category_name=category_name,
        title=DIC[category_name]['title'],
        query=DIC[category_name]['query'],
        x_year=df['Year'].tolist(),
        y_num_articles=df['num_articles'].tolist(),
        y_num_citations=df['num_citations'].tolist(),
        categories=categories,
        num_citations_across_categories=num_citations_across_categories
    )
    # return markdownify.markdownify(content)
    return content

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
            title = line.split('\t')[0]
            query = line.split('\t')[1].rstrip()
            print (f'Title: {title}\nQuery: {query}')
            category_name = title.replace(' ', '_')
            ################################
            ## Fetch the most cited articles
            data = fetch_articles(query)
            DIC[category_name] = {'title': title, 'query': query, 'most_cited_articles': data}
            # plot = utils.metrics_over_time_js(data, category_name, title)
            # plot.savefig(f'../../docs/assets/{category_name}.png')
            df = utils.metrics_over_time_js(data)
            ################################
            ## Fetch the most recent articles
            data = fetch_articles(query, sort = 'publicationDate:desc')
            DIC[category_name]['most_recent_articles'] = data
            # print (data[0])
            markdown_text = create_template("category.txt", category_name, df)
                                            # DIC[category_name]['most_cited_articles'][0:N],
                                            # DIC[category_name]['most_recent_articles'][0:N])
            # Add the hide navigation
            markdown_text = "---\nhide:\n - navigation\n---\n" + markdown_text
            # Write the markdown text to a file
            with open(f'../../docs/{category_name}.md', 'w', encoding='utf-8') as file:
                file.write(markdown_text)
            ################################

    # End of file
    title = 'Overview'
    query = ' | '.join([category_items['query'] for _, category_items in DIC.items()])
    category_name = 'Overview'
    ################################
    ## Fetch the most cited articles
    data = fetch_articles(query)
    # print (data)
    DIC[category_name] = {'title': title, 'query': query, 'most_cited_articles': data}
    # plot = utils.metrics_over_time_js(data, category_name, title)
    # plot.savefig(f'../../docs/assets/{category_name}.png')
    df = utils.metrics_over_time_js(data)
    ################################
    ## Fetch the most recent articles
    data = fetch_articles(query, sort = 'publicationDate:desc')
    DIC[category_name]['most_recent_articles'] = data
    # print (data[6])
    # Make bar plot for the number of citations of top 100 articles
    # in each category
    dic_all_citations = utils.all_citations_js(DIC)
    markdown_text = create_template("overview.txt", category_name, df, dic_all_citations=dic_all_citations)
                                    # DIC[category_name]['most_cited_articles'][0:N],
                                    # DIC[category_name]['most_recent_articles'][0:N])
    # Add the hide navigation
    markdown_text = "---\nhide:\n - navigation\n---\n" + markdown_text
    # Write the markdown text to a file
    with open('../../docs/index.md', 'w', encoding='utf-8') as file:
        file.write(markdown_text)
    ################################
    # Read YAML file
    file_path = '../../base.yml'
    data = utils.read_yaml(file_path)

    # Add more stuff to the YAML data
    data['nav'] = []
    for category_name, category_items in DIC.items():
        if category_name == 'Overview':
            data['nav'].append({category_items['title']: 'index.md'})
        else:
            data['nav'].append({category_items['title']: category_name + '.md'})

    # reverser the order so that Overview appears first
    data['nav'] = data['nav'][::-1]
    # print (data['nav'])
    # Write modified YAML data back to file
    utils.write_yaml(data, '../../mkdocs.yml')

if __name__ == '__main__':
    # Run the main function
    main()
