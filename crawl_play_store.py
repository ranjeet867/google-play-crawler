import time
from bs4 import BeautifulSoup
import sys, io
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.proxy import *

# @author Ranjeet Singh <ranjeetsingh867@gmail.com>
# Modify it according to your requirements

no_of_reviews = 1000

non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)
driver = webdriver.Firefox(executable_path='/usr/local/bin/geckodriver')

wait = WebDriverWait( driver, 10 )


# Append your app store urls here
urls = ["https://play.google.com/store/apps/details?id=com.flipkart.android&hl=en",
        "https://play.google.com/store/apps/details?id=com.amazon.mShop.android.shopping"]

        for url in urls:

            driver.get(url)

            page = driver.page_source

            soup_expatistan = BeautifulSoup(page, "html.parser")

            expatistan_table = soup_expatistan.find("h1", class_="AHFaub")

            print("App name: ", expatistan_table.string)

            expatistan_table = soup_expatistan.findAll("span", class_="htlgb")[4]

            print("Installs Range: ", expatistan_table.string)

            expatistan_table = soup_expatistan.find("meta", itemprop="ratingValue")

            print("Rating Value: ", expatistan_table['content'])

            expatistan_table = soup_expatistan.find("meta", itemprop="reviewCount")

            print("Reviews Count: ", expatistan_table['content'])

            soup_histogram = soup_expatistan.find("div", class_="VEF2C")

            rating_bars = soup_histogram.find_all('div', class_="mMF0fd")

            for rating_bar in rating_bars:
                print("Rating: ", rating_bar.find("span").text)
                print("Rating count: ", rating_bar.find("span", class_="L2o20d").get('title'))

            # open all reviews
            url = url+'&showAllReviews=true'
            driver.get(url)
            time.sleep(5) # wait dom ready
            for i in range(1,10):
                driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')#scroll to load other reviews
                time.sleep(1)
            page = driver.page_source
            
            soup_expatistan = BeautifulSoup(page, "html.parser")
            expand_pages = soup_expatistan.findAll("div", class_="d15Mdf")
            counter = 1
            for expand_page in expand_pages:
                try:
                    print("\n===========\n")
                    print("review："+str(counter))
                    print("Author Name: ", str(expand_page.find("span", class_="X43Kjb").text))
                    print("Review Date: ", expand_page.find("span", class_="p2TkOb").text)
                    '''
                    //didn't find reviewer link
                    print("Reviewer Link: ", expand_page.find("a", class_="reviews-permalink")['href'])
                    '''
                    reviewer_ratings = expand_page.find("div", class_="pf5lIe").find_next()['aria-label'];
                    reviewer_ratings = reviewer_ratings.split('(')[0]
                    reviewer_ratings = ''.join(x for x in reviewer_ratings if x.isdigit())
                    print("Reviewer Ratings: ", reviewer_ratings)
                    '''
                    //didn't find review title
                    print("Review Title: ", str(expand_page.find("span", class_="review-title").string))
                    '''
                    print("Review Body: ", str(expand_page.find("div", class_="UD7Dzf").text))
                    developer_reply = expand_page.find_parent().find("div", class_="LVQB0b")
                    if hasattr(developer_reply, "text"):
                        print("Developer Reply: "+"\n", str(developer_reply.text))
                    else:
                        print("Developer Reply: ", "")
                    counter+=1
                except:
                    pass
driver.quit()

