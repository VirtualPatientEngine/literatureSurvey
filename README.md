[![TESTS](https://github.com/VirtualPatientEngine/literatureSurvey/actions/workflows/tests.yml/badge.svg)](https://github.com/VirtualPatientEngine/literatureSurvey/actions/workflows/tests.yml)
[![RELEASE](https://github.com/VirtualPatientEngine/literatureSurvey/actions/workflows/release.yml/badge.svg)](https://github.com/VirtualPatientEngine/literatureSurvey/actions/workflows/release.yml)
[![mkdocs-deploy](https://github.com/VirtualPatientEngine/literatureSurvey/actions/workflows/mkdocs-deploy.yml/badge.svg)](https://github.com/VirtualPatientEngine/literatureSurvey/actions/workflows/mkdocs-deploy.yml)
[![pages-build-deployment](https://github.com/VirtualPatientEngine/literatureSurvey/actions/workflows/pages/pages-build-deployment/badge.svg)](https://github.com/VirtualPatientEngine/literatureSurvey/actions/workflows/pages/pages-build-deployment)

<h1 align="center" style="border-bottom: none;">🚀 Literature Survey</h1>

Welcome to the Literature Survey Template Repository! 📚✨ This repository provides you with a nifty setup to create your very own automated literature survey repository. Say goodbye to manual searching and hello to automated updates every Monday morning at 6 am UTC!

### But Wait, There's More!
Not only does this repo automatically fetch the most cited and latest articles in your field, but it also presents them to you in pretty web pages with interactive tables and plots!

### Example Usage
For demonstration purposes, this template repository uses the keywords related to the simulator module of Team VPE as an example. You can easily customize it to your own fields of interest by following the steps outlined below. To see how the automated literature survey repo looks like, visit this [link](https://virtualpatientengine.github.io/literatureSurvey).

Let's dive in and set up your own literature survey adventure!

### Getting Started
Follow these simple steps to set up your literature survey repository:

1. Click on the ```Use this template``` button to create your own repository based on this template.

2. Open up the ```app/data/query.tsv``` file in your favorite code editor or Excel.

3. Get creative! Under the title columns, give catchy titles to your sections and under the Query column, define their correspondng queries. Need help? Check out Semantic Scholar's query [parameter definition](https://api.semanticscholar.org/api-docs/#tag/Paper-Data/operation/get_graph_paper_bulk_search).

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

6. It's time to fetch some literature! Run the ```literature_fetch.py``` script to grab those juicy papers from Semantic Scholar:
```
> cd app/code
> python3 literature_fetch.py
```

7. Now, fire up MkDocs to see how your survey is shaping up locally:
```
> mkdocs serve
```

Head over to the localhost link that pops up in your terminal. Marvel at the beauty of your survey pages. Once you're satisfied, commit your code and open up a PR. If you have any questions or need assistance, feel free to reach out to the Team VPE Code/DevOps guides or contact Gurdeep.

### Bugs? Feature Requests? I've Got You Covered
If you encounter any bugs or have brilliant ideas for new features, don't hesitate to head over to the "Issues" tab and let me know.

### Happy surveying! 📖🔍
