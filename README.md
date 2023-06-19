# sqlalchemy-challenge
Module 10 Challenge

The first part of this challenge is in climate5.ipynb.

The Flask API runs from app.py.

All files relevant to the challenge can be found in the SurfsUp folder of the sqlalchemy-challenge directory


I needed to access a number of resources for assistance with this challenge. Although not the complete resource list, most are provided below.


I found some aspects of the challenge very difficult, including which data set to use for which parts of the challenge, eg whether the single station most recent 12 months dataset was the one to use for all future analysis or not. 

Also although I 'cleaned' the dataset in Jupyter notebook with respect to removing rows with missing data, (dropna), I did not do this with the session queries I used in Flask, which I imagine I should have.

I also didnt have time to get DRY going properly, by having set functions and calling them to avoid re-writing code.

Thanks for looking through my challenge and assessing it.

With the Flask analysis, I have actually separated the different analyses into different routes, more for my own clarity and not to ruin previous working code as I approached the next problem.



# ordering sqlalchemy by DESC
https://stackoverflow.com/questions/35132463/sqlalchemy-core-order-by-desc
https://stackoverflow.com/questions/4186062/sqlalchemy-order-by-descending

# changing formatting of pandas plots
https://stackoverflow.com/questions/66277501/pandas-subplot-title-size
https://stackoverflow.com/questions/21487329/add-x-and-y-labels-to-a-pandas-plot

# pandas binning
https://pbpython.com/pandas-qcut-cut.html
https://mode.com/example-gallery/python_histogram/

# using args and kwargs to DRY instead of repeating code
https://realpython.com/python-kwargs-and-args/

# pass tuples in to Flask
https://stackoverflow.com/questions/39772670/flask-return-multiple-variables
https://stackoverflow.com/questions/31669864/date-in-flask-url