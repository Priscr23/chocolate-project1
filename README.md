chocolate-project1
==============================

Analysis of diferent chocolate bars made of distinct cocoa beans
Overview
Chocolate is undeniably one of the most beloved and popular candies worldwide. 
In the United States alone, residents consume an astounding amount of chocolate, surpassing 2.8 billion pounds annually.
However, not all chocolate bars are created equal. This dataset provides valuable insights into the world of chocolate, offering expert ratings of over 1,700 individual chocolate bars.

Contents
Expert ratings of chocolate bars
Information on regional origin
Percentage of cocoa
Variety of chocolate bean used
Bean origin
Data Sources
The dataset is sourced from reputable sources and compiled to offer a comprehensive view of chocolate attributes and characteristics.

Purpose
The purpose of this dataset is to provide researchers, chocolate enthusiasts, and industry professionals with detailed information about chocolate bars, also details about how it has expanded worldwide since it reached the Spanish colonizers. 
By analyzing factors such as regional origin, cocoa percentage, and bean variety, users can gain insights into the factors that contribute to the quality and taste of chocolate.

Potential Applications
Analyzing the correlation between cocoa percentage and taste ratings
Exploring the impact of regional origin on chocolate flavor profiles
Studying trends in chocolate preferences over time
Identifying factors that contribute to the success of premium chocolate brands
Acknowledgments
This dataset would not be possible without the expertise and dedication of chocolate experts and enthusiasts who have meticulously evaluated and documented chocolate bars.

Project Organization
------------

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io


--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
