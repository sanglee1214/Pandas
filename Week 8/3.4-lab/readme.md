---
title: LDA with Foursquare API Lab
type: lab 3.4
duration: "1:25"
creator:
    name: Chris Esposo
    city: Atlanta, GA
---

# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) LDA with Foursquare API
Week 8 | 3.4


## Introduction

First things first, we want to develop a classifier that can detect if a user comment is misapplied to the venue. Think of all the times you've gone to an Amazon item and saw reviews that looked like the image below, "Used but in very good condition", "fast shipping" are these relevant to a product review? Or are they more appropriate for seller reviews?

We're going to see if we can develop a comment classifier to detect which kinds of comments may be more appropriate for which venue type, and thus provide some indication on the "appropriateness" of the comment that can be used for further review, thus (we hope), improving the overall quality of Foursquare as a reviews platform

How do we plan on doing this? First, this lab will finally utilize a multi-class target. In this case, our goal will be to link comments we've extracted from Foursquare to store category type.

As an example: "This place got me drunk" would be a comment you'd expect to see for a store category "bar"
Yet, "I want to have my wedding here" is definitely not a comment you'd expect to see at a "bar" category (lest you live in Boston), more likely you'd see such a category associated with a park, or other such venue.

The motivation for this exercise came from Amazon. Notice in the picture below, you see some comments that are speaking about the "condition" of the DVD and not the quality of the movie. These are an example of misapplied comments. I'm not promising our classifier will be this exact, but what we'll be doing is a big step in that direction. Excited? Good! Let's go!


## Exercise

Like the previous foursquare exercise, start with loading up your API key and find an appropriate location to mine data from via Foursquare. After, load up your crawler/scraper code and pull in the data in a properly formatted pandas table. After merging (if pulling multiple data), formatting, and removing duplicates, we'll move onto the second part of the lab, which will include some light text analysis/NLP.


```python
import foursquare
import json
import pandas as pd
import unicodedata


#ACCESS_TOKEN = ""
#client = foursquare.Foursquare(access_token=ACCESS_TOKEN)

CLIENT_ID = 'YOUR ID'
CLIENT_SECRET = 'YOUR SECRET'
client = foursquare.Foursquare(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)

starting_list = client.venues.search(params={'near': 'Suwanee, GA', 'radius':'3000', 'categoryId':'4d4b7105d754a06376d81259'})
#print(json.dumps(starting_list, indent = 4))

venue_table = pd.DataFrame(); venue_table_2 = pd.DataFrame();
```

#### Requirements

- Functional experience with RegEx
- Writing simple python methods to clean/merge/sort data
- Knowledge of NLTK text methods, especially the text vectorizer methods


#### Starter code

Please use [the following starter code](./code/w8-3.4-starter.ipynb)

> [Solution Code](/code/w8-3.4-solution.ipynb)

#### Deliverable

Submit a notebook with the code written to complete the exercises!

#### Additional Resources

For those of you who want to read further:

- [Developer Notes from Foursquare](https://developer.foursquare.com/)
- [Foursquare Developer Resources](https://developer.foursquare.com/resources/libraries)
