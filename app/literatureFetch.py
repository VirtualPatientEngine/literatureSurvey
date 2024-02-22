"""
A class to extract the data from Uniprot
for a given protein
"""

import requests
from jinja2 import Environment, FileSystemLoader

class Arxiv:
    """
    A class to extract the data from Arxiv
    for a given arxiv id
    """
    def __init__(self, paper_id) -> None:
        """
        Initialize the class

        Args:
            arxiv_id (str): arxiv id
            title (str): title of the paper
            published (str): published date
            link (str): link to the paper
        
        Returns:
            None
        """
        self.arxiv_id = paper_id
        self.semantic_scholar_data = {}
    def get_semantic_scholar_data(self) -> dict:
        """
        Return the semantic scholar data for a given arxiv id

        Args:
            None
        Returns:
            dict: semantic scholar data
        """
        return self.semantic_scholar_data
    def get_arxiv_id(self):
        """
        Return the arxiv id

        Args:
            None
        Returns:
            str: arxiv id
        """
        return self.arxiv_id

def get_semantic_scholar(article_ids):
    """
    Return the semantic scholar data for a given arxiv ids

    Args:
        arxiv_ids (list): list of arxiv ids
    Returns:
        dict: dictionary of arxiv ids and their semantic scholar data
    """

    fields = 'referenceCount,citationCount,title,authors,'
    fields += 'journal,fieldsOfStudy,publicationTypes,publicationDate,url'
    r = requests.post(
        'https://api.semanticscholar.org/graph/v1/paper/batch',
        params={'fields': fields},
        json={"ids": article_ids},
        timeout=10
    )
    # print(json.dumps(r.json(), indent=2))
    return r.json()

if __name__ == "__main__":
    # Run the script from command line
    import markdownify
    import feedparser
    # Define the query
    # QUERY = 'stat.ML:causal+link+prediction'
    QUERY = 'stat.ML:learned+differentiable+simulator'
    # Define the base url
    BASE_URL = 'http://export.arxiv.org/api/query?search_query='
    # Define the search parameters
    START = 0
    MAX_RESULTS = 500
    SORT_BY = 'relevance'
    SEARCH_PARAMS = f'&start={START}&max_results={MAX_RESULTS}&sortBy={SORT_BY}'
    # Define the url link
    URL_LINK = BASE_URL + QUERY + SEARCH_PARAMS
    # Parse the url link
    feed = feedparser.parse(URL_LINK)
    num_entries = len(feed.entries)
    arxiv_ids = [] # List to store the arxiv ids
    dic_arxiv_ids = {} # Dictionary to store the arxiv ids
    for i in range(num_entries):
        # print (feed.entries[i]['title'], feed.entries[i]['published'], feed.entries[i]['link'])
        arxiv_id = feed.entries[i]['link'].split('/')[-1].split('v')[0]
        dic_arxiv_ids[arxiv_id] = Arxiv(arxiv_id)
    arxiv_ids = ["ARXIV:"+arxiv_id for arxiv_id in dic_arxiv_ids]
    # print (arxiv_ids)
    results = get_semantic_scholar(arxiv_ids)
    # print (results)
    print (len(results))

    articles = []
    for i in range(num_entries):
        arxiv_id = arxiv_ids[i].split(':')[1]
        print (results[i])
        if results[i] is None:
            continue
        dic_arxiv_ids[arxiv_id].semantic_scholar_data = results[i]
        # Append the articles
        if dic_arxiv_ids[arxiv_id].semantic_scholar_data is not None:
            if int(dic_arxiv_ids[arxiv_id].semantic_scholar_data['citationCount']) > 200:
                # Extract author names
                authors = []
                for author in dic_arxiv_ids[arxiv_id].semantic_scholar_data['authors']:
                    authors.append(author['name'])
                articles.append({"title": results[i]['title'],
                                 'url': results[i]['url'],
                                 "authors": ', '.join(authors),
                                "citations": results[i]['citationCount'],
                                'journal': results[i]['journal'],
                                'fieldsOfStudy': results[i]['fieldsOfStudy'],
                                'publicationTypes': results[i]['publicationTypes'],
                                'publicationDate': results[i]['publicationDate']
                             })
    # Set the template environment
    environment = Environment(loader=FileSystemLoader("../templates/"))
    # Get the template
    template = environment.get_template("message.txt")
    # Render the template
    content = template.render(
        articles=articles,
        query=QUERY,
    )
    # Convert the content to markdown
    markdown_text = markdownify.markdownify(content)
    # Write the markdown text to a file
    with open('../docs/index.md', 'w', encoding='utf-8') as file:
        file.write(markdown_text)
