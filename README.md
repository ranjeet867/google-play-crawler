
# Welcome to the google-play-crawler!
Python based Google Play Crawler 

##Example of crawled data:

App name:  Amazon Shopping <br>
Installs Range:   50,000,000 - 100,000,000
Rating Value:  4.268221378326416<br>
Rating Count:  449554<br>
Reviews Count:  449,554<br>
Rating:   5 <br>
Rating count:  281,323<br>
Rating:   4 <br>
Rating count:  86,924<br>
Rating:   3 <br>
Rating count:  34,203<br>
Rating:   2 <br>
Rating count:  14,772<br>
Rating:   1 <br>
Rating count:  32,332<br>
Author Name:  michelle slaughter<br>
Review Date:  2 June 2016<br>
Reviewer Link:  /store/apps/details?id=com.amazon.mShop.android.shopping&reviewId=Z3A6QU9xcFRPSEdKRjFBeEJjVFNZMHdfLUptRnprTkhnOGpacWhaSzhUb1NOa29Ca3lYeEtxZi1PeXZZUXVtdVlieExuaG1wbmtSRF83emZLeE1iRXg3dVE<br>
Reviewer Ratings:  3<br>
Review Title:  Alright<br>
Review Body:   Alright The app itself is great. This is my first user on Amazon after being a longtime user of Ebay. Just not too happy with delivery as promised. I ordered 2 instock items directly from Amazon on may 30th, says will ship today (june 2) and have it by the 6th..has yet to be shipped. Funny thing is the next day the 31st I ordered 2 items from a 3rd party on Amazon and they shipped yesterday. Sneaky part tho offering 30 days free of Prime, have to give credit card. I did, mine is expired so they cancelled free trial  Full Review <br> 
Developer Reply:  <br>

##Requirements

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



