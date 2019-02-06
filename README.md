
# Welcome to the google-play-crawler!
Python based Google Play Crawler 

## Example of crawled data:

App name:  Flipkart Online Shopping App
Installs Range:  100,000,000+
Rating Value:  4.455704689025879
Reviews Count:  7689096
Rating:  5
Rating count:  5,003,740
Rating:  4
Rating count:  1,836,612
Rating:  3
Rating count:  465,871
Rating:  2
Rating count:  114,706
Rating:  1
Rating count:  268,167

review：1
Author Name: 
Review Date:
Reviewer Ratings:
Review Body: 
Developer Reply:  


## Requirements

1. Python 3.4.4
2. beautifulsoup4
3. Selenium
4. geckodriver
5. Firefox
## Installation beautifulsoup4

If you're using a recent version of Debian or Ubuntu Linux, you can install Beautiful Soup with the system package manager:

Try anyone of these methods. I personally prefer pip. 

    $ apt-get install python-bs4.
    $ easy_install beautifulsoup4.
    $ pip install beautifulsoup4.

To Install Selenium 

    pip install selenium
    
To install geckodriver in Mac

    brew install geckodriver
    

## Usage:
Directly run the script crawl_play_store.py to print app data. By default it will crawl Flipkart and Amazon upto 1000 reviews.

     python crawl_play_store.py
     
To scrap data just add app url in this array in python file:
urls = ["https://play.google.com/store/apps/details?id=com.flipkart.android&hl=en", 
		"https://play.google.com/store/apps/details?id=com.amazon.mShop.android.shopping"]

Or customize your code according to your need. 



