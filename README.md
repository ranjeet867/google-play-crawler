
# Welcome to the google-play-crawler!
Python based Google Play Crawler 

## Example of crawled data:

App name:  Flipkart Online Shopping App<br>
Installs Range:  100,000,000+<br>
Rating Value:  4.455704689025879<br>
Reviews Count:  7689096<br>
Rating:  5<br>
Rating count:  5,003,740<br>
Rating:  4<br>
Rating count:  1,836,612<br>
Rating:  3<br>
Rating count:  465,871<br>
Rating:  2<br>
Rating count:  114,706<br>
Rating:  1<br>
Rating count:  268,167<br>
<br>
review：1<br>
Author Name: <br>
Review Date:<br>
Reviewer Ratings:<br>
Review Body: <br>
Developer Reply: <br> 


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



