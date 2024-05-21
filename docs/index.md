<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body>
    <h1>Introduction</h1>
    <p>Welcome to <a href="https://github.com/VirtualPatientEngine" target="_blank">Team VPE</a>'s Literature Survey System! This project leverages the powerful <a href='https://api.semanticscholar.org/api-docs/recommendations' target="_blank">Semantic Scholar's Recommendation API</a> to provide you with highly relevant research article recommendations based on your curated lists of articles.</p>

    <p>Moreover, this website contains curated collection of references on differentiable and learned simulator algorithms for developing digital twins with applications in drug discovery and development.</p>
    
    <h2>Features</h2>
    <ul>
        <li><strong>List-based recommendations:</strong> For each topic, we use a manually curated list of positive articles. We then select an equal number of negative articles from other topics. Semantics Scholar's recommendation system uses the set of positive and negative to provide up to 300 recommendations per topic.</li>
        <li><strong>Single-paper recommendations:</strong> For each article in our curated lists, Semantics Scholar's recommendation system returns up to 10 related articles.</li>
    </ul>

    <h2>How it works?</h2>
    <ul>
        <li>Scroll to the top of this page and click one of the tabs to open the relevant section.</li>
        <li>Each topic contains two tables. The first table lists the manually curated articles, and the second table lists the articles recommended for that topic by the recommendation system. The last column of the first table contains a hyperlink that opens a new tab with articles recommended for that specific article.</li>
        <li>Click on the <i class="material-icons">help</i> icon at the top of the page to learn more about that section.</li>
    </ul>

    <div style="display: inline-block; vertical-align: middle;">
       Check out our <a href="https://github.com/VirtualPatientEngine/literatureSurvey"  target="_blank">GitHub <i class="material-icons">open_in_new</i></a> repository to learn how to build one for yourself.
    </div>
</body>
</html>