[![TESTS](https://github.com/VirtualPatientEngine/literatureSurvey/actions/workflows/tests.yml/badge.svg)](https://github.com/VirtualPatientEngine/literatureSurvey/actions/workflows/tests.yml)
[![RELEASE](https://github.com/VirtualPatientEngine/literatureSurvey/actions/workflows/release.yml/badge.svg)](https://github.com/VirtualPatientEngine/literatureSurvey/actions/workflows/release.yml)
[![mkdocs-deploy](https://github.com/VirtualPatientEngine/literatureSurvey/actions/workflows/mkdocs-deploy.yml/badge.svg)](https://github.com/VirtualPatientEngine/literatureSurvey/actions/workflows/mkdocs-deploy.yml)
[![pages-build-deployment](https://github.com/VirtualPatientEngine/literatureSurvey/actions/workflows/pages/pages-build-deployment/badge.svg)](https://github.com/VirtualPatientEngine/literatureSurvey/actions/workflows/pages/pages-build-deployment)

<h1 align="center" style="border-bottom: none;">🚀 Literature Survey</h1>

Welcome to the Literature Survey Template Repository! 📚✨ This repository provides you with a quick setup to create your very own automated literature survey repository using Semantic Scholar's [Recommendation API](https://api.semanticscholar.org/api-docs/recommendations).

### But Wait, There's More!
Not only does this repo automatically fetch the recommended articles in your field, but it also presents them to you in pretty web pages with interactive tables and plots!

### Types of Recommendations
Semantic Scholar provides 2 types of recommendations:

1. ```Using one positive article```: Each article you provide will be used to generate recommendations specifically for that article. You can access these recommendations by clicking on the <kbd>Open a new tab</kbd> icon in the last column of the first table. I refer to this as "recommendation for the article".
2. ```Using positive and negative articles```: For this literature survey version, the first 10 articles related to the topic you provide will be selected. Additional articles may be provided beyond this count but they shall not be considered to retrieve the recommendations. Negative articles will be selected by sampling the top N articles from other topics, ensuring that the total number of sampled articles is 10 and equal from each topic whenever possible. These positive and negative articles will be used to retrieve recommendations from Semantic Scholar, which will be displayed in the second table on the page. I refer to this as "recommendation for the topic".

### Example Usage
For demonstration purposes, this template repository uses the articles related to the simulator module of Team VPE as an example. You can easily customize it to your own fields of interest by following the steps outlined below. To see how the automated literature survey repo looks like, visit this [link](https://virtualpatientengine.github.io/literatureSurvey).

Let's dive in and set up your own literature survey adventure!

### Getting Started
Follow these simple steps to set up your literature survey repository:

1. Click on the ```Use this template``` button to create your own repository based on this template.

2. Open up the ```app/data/test.tsv``` file in your favorite code editor or Excel.

3. Get creative! Under the title columns, give catchy titles to your sections and under the URL column, specify the correspondng URLs to Semantic Scholar article. Need help? Check out Semantic Scholar's query [parameter definition](https://api.semanticscholar.org/api-docs/#tag/Paper-Data/operation/get_graph_paper_bulk_search).

4. Let's create a venv:
```
> python -m venv env
# On Windows
> .\env\Scripts\activate

# On macOS and Linux
> source env/bin/activate
```

5. Install all the necessary requirements:
```
> pip3 install -r requirements.txt
```

6. It's time to fetch some literature! Run the ```literature_fetch_recommendation_api.py``` script to grab the recommended articles from Semantic Scholar:
```
> cd app/code
> python3 literature_fetch_recommendation_api.py
```

7. Now, fire up MkDocs to see how your survey is shaping up locally:
```
> mkdocs serve
```

Head over to the localhost link that pops up in your terminal. Once you're satisfied, commit your code and open up a PR. If you have any questions or need assistance, please contact Gurdeep.

### Bugs? Feature Requests? I've Got You Covered
If you encounter any bugs or have brilliant ideas for new features, don't hesitate to head over to the "Issues" tab and let me know.

### Happy surveying! 📖🔍
