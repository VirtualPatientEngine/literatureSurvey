#!/usr/bin/env python3

'''
This script demonstrates how to use the Semantic Scholar API to search for papers 
and retrieve their details.
'''

import os
import time
import pandas as pd
from jinja2 import Environment, FileSystemLoader

DIC = {}

def create_template(template,
                    topic_name,
                    paper_ids,
                    df_citations) -> str:
    """
    Return the markdown content for a given template

    Args:
        template_file (str): template file
        topic (str): topic of the category
        dic (dict): dictionary with the most cited and most recent articles
        df (pd.DataFrame): dataframe with the metrics over time
        dic_all_citations (dict): dictionary with the number of citations for all categories
    Returns:
        str: markdown content

    Example:
    category_name = "category1"
    DF = pd.DataFrame({
        'date': ['2020-01-01', '2019-01-01'],
        'num_citations': [10, 20],
        'num_articles': [10, 20]
    })

    markdown_text = create_template("category.txt", category_name, DF)
    """
    # Set the template environment
    environment = Environment(loader=FileSystemLoader(template[0]))
    # Get the template
    template = environment.get_template(template[1])
    # Render the template
    if df_citations.empty:
        content = template.render(
            # current time
            current_time=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
            positive_paper_ids=paper_ids,
            category_name=topic_name,
            title=topic_name,
        )
    else:
        content = template.render(
            # current time
            current_time=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
            positive_paper_ids=paper_ids['positive'],
            recommended_paper_ids=paper_ids['recommended'],
            category_name=topic_name,
            title=topic_name,
            x_year = df_citations['Year'].tolist(),
            y_num_citations = df_citations['num_citations'].tolist(),
        )
    # return markdownify.markdownify(content)
    return content

if os.path.exists('../../docs/recommendations') is False:
    os.mkdir('../../docs/recommendations')

if __name__ == '__main__':
    import utils
    from topic import Topic
    from article import Article
    from author import Author

    QUERY_FILE = '../data/query.tsv'
    # Work with all the topics
    with open(QUERY_FILE, 'r', encoding='utf-8-sig') as f:
        for line in f:
            if line.split('\t')[0] == 'Topic':
                continue
            topic = line.split('\t')[0].lstrip().rstrip()
            if line.split('\t')[1] is None:
                continue
            USE_ARTICLE = bool(line.split('\t')[1].lstrip().rstrip() == '1')
            paper_id = line.split('\t')[2].split('/')[-1].split('?')[0]
            # Check if the topic is already in the dictionary
            topic_obj = Topic(topic) if topic not in DIC else DIC[topic]
            DIC[topic] = topic_obj
            # Add the article to the list of positive articles
            topic_obj.paper_ids['positive'][paper_id] = Article(paper_id,
                                                                use_for_recommendation=USE_ARTICLE)
    # Fetch the recommendations for each topic
    # make the markdown files
    for topic, topic_obj in DIC.items():
        # if topic not in ['Symbolic regression', 'Koopman operator theory', 'PINNs']:
        # if topic not in ['Neural ODEs', 'Latent space simulators (VAMP)']:
        #     continue
        # Add the negative articles
        utils.add_negative_articles(topic_obj, DIC)
        # Update the details of the papers
        all_paper_data = utils.update_paper_details(topic_obj)
        for paper_data in all_paper_data:
            paper_id = paper_data['paperId']
            if paper_id in topic_obj.paper_ids['negative']:
                paper_obj = topic_obj.paper_ids['negative'][paper_id]
            else:
                paper_obj = topic_obj.paper_ids['positive'][paper_id]
            utils.add_paper_details(
                            paper_obj,
                            paper_data)
            # Some articles are used as negative so they already have authors
            # assigned to them. If not, assign the authors to the article
            if len(paper_obj.authors) > 0:
                continue
            for author in paper_data['authors']:
                # if the author id is None, set it to the name
                if author['authorId'] is None:
                    author['authorId'] = author['name']
                    print (f'Author ID is None for {author["name"]}. Setting it to the name.')
                # Add the author to the article
                paper_obj.authors.append(
                                        Author(author['authorId'],
                                        author_name=author['name']))
        ###########################################################
        ## GET THE RECOMMENDATIONS FOR A SINGLE POSITIVE ARTICLE ##
        for article_id, article_obj in topic_obj.paper_ids['positive'].items():
            # utils.add_recommendations_to_positive_articles(article_obj, 2)
            search_response = utils.add_recommendations_to_positive_articles(article_id,
                                                                             limit=10)
            for rec_paper_data in search_response:
                # skip the ones with publication date is null
                if rec_paper_data['publicationDate'] is None:
                    continue
                rec_paper_obj = Article(rec_paper_data['paperId'])
                # rec_paper_obj.add_paper_details(rec_paper_data)
                ##
                for author in rec_paper_data['authors']:
                    # if the author id is None, set it to the name
                    if author['authorId'] is None:
                        author['authorId'] = author['name']
                        print (f'Author ID is None for {author["name"]}. Setting it to the name.')
                    # Add the author to the article
                    rec_paper_obj.authors.append(
                                            Author(author['authorId'],
                                            author_name=author['name']))
                utils.add_paper_details(rec_paper_obj, rec_paper_data)
                if article_obj.recommended_articles is None:
                    article_obj.recommended_articles = []
                article_obj.recommended_articles.append(rec_paper_obj)
            ##########
            if article_obj.recommended_articles is None:
                continue
            # Get the author ids of the recommended articles
            rec_articles_authors_ids = article_obj.get_recommened_articles_authors_ids()
            # Get the details of the authors of the recommended articles
            rec_articles_author_details = utils.get_author_details(rec_articles_authors_ids)
            for article_recommendations_obj in article_obj.recommended_articles:
                utils.update_h_index(article_recommendations_obj,
                                     rec_articles_author_details)
            # Create the markdown text
            markdown_text = create_template(
                                            ("../../templates",
                                            "positive_paper_recommendation.txt"),
                                            article_obj.info.title,
                                            article_obj.recommended_articles,
                                            pd.DataFrame()
                                            )
            # Add the hide navigation
            markdown_text = "---\nhide:\n - navigation\n---\n" + markdown_text
            # Write the markdown text to a file
            with open(f'../../docs/recommendations/{article_id}.md', 'w', encoding='utf-8') as file:
                file.write(markdown_text)
        ##################################################################
        ## GET THE RECOMMENDATIONS FOR ALL POSITIVE ARTICLES IN A TOPIC ##
        # topic_obj.update_recommended_articles() # Update the recommended articles
        print (f'Fetching recommendations for {topic_obj.topic}...')
        if len(topic_obj.paper_ids['positive']) == 0:
            print (f'No positive articles for {topic_obj.topic}. Skipping...')
        else:
            search_response_json = utils.add_recommendations(topic_obj, limit=300)
            for paper_data in search_response_json['recommendedPapers']:
                paper_id = paper_data['paperId']
                # skip the ones with publication date is null
                if paper_data['publicationDate'] is None:
                    continue
                if 'recommended' not in topic_obj.paper_ids:
                    topic_obj.paper_ids['recommended'] = {}
                paper_obj = Article(paper_data['paperId'])
                utils.add_paper_details(paper_obj, paper_data)
                for author in paper_data['authors']:
                    # if the author id is None, set it to the name
                    if author['authorId'] is None:
                        author['authorId'] = author['name']
                        print (f'Author ID is None for {author["name"]}. Setting it to the name.')
                    # Add the author to the article
                    paper_obj.authors.append(
                                            Author(author['authorId'],
                                            author_name=author['name']))
                topic_obj.paper_ids['recommended'][paper_id] = paper_obj
        ##################################################################
        # Get the metrics over time
        df = utils.metrics_over_time_js(topic_obj.paper_ids['recommended'])
        authors_ids = topic_obj.get_all_authors_ids() # Get all the authors of the articles
        author_details = utils.get_author_details(authors_ids) # Get the details of the authors
        for article_type in topic_obj.paper_ids:
            for article_id, article_obj in topic_obj.paper_ids[article_type].items():
                utils.update_h_index(article_obj, author_details)
        print (f'Fetched the details of the authors (n={len(author_details)}) for {topic}.')
        # Create the markdown text
        markdown_text = create_template(
                                        ("../../templates", "topic.txt"),
                                        topic,
                                        topic_obj.paper_ids,
                                        df
                                        )
        # Add the hide navigation
        markdown_text = "---\nhide:\n - navigation\n---\n" + markdown_text
        # Write the markdown text to a file
        with open(f'../../docs/{topic}.md', 'w', encoding='utf-8') as file:
            file.write(markdown_text)
        #################################################################
        # break

    # Read YAML file
    data = utils.read_yaml('../../base.yml')

    # Add more stuff to the YAML data
    # data['nav'] = []
    for topic, topic_obj in DIC.items():
        data['nav'].append({topic: topic + '.md'})

    # reverser the order so that Overview appears first
    # data['nav'] = data['nav'][::-1]
    # Write modified YAML data back to file
    utils.write_yaml(data, '../../mkdocs.yml')
    print (f'Completed at {time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())}')
