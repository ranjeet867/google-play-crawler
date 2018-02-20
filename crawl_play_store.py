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

    expatistan_table = soup_expatistan.find("div", class_="id-app-title")

    print("App name: ", expatistan_table.string)

    expatistan_table = soup_expatistan.find("div", itemprop="numDownloads")

    print("Installs Range: ", expatistan_table.string)

    expatistan_table = soup_expatistan.find("meta", itemprop="ratingValue")

    print("Rating Value: ", expatistan_table['content'])

    expatistan_table = soup_expatistan.find("meta", itemprop="ratingCount")

    print("Rating Count: ", expatistan_table['content'])

    expatistan_table = soup_expatistan.find("span", class_="reviews-num")

    print("Reviews Count: ", expatistan_table.string)

    soup_histogram = soup_expatistan.find("div", class_="rating-histogram")

    rating_bars = soup_histogram.find_all('div', class_="rating-bar-container")

    for rating_bar in rating_bars:
        print("Rating: ", rating_bar.find("span").text)
        print("Rating count: ", rating_bar.find("span", class_="bar-number").string)

    next_button = driver.find_element_by_xpath('//*[@id="body-content"]/div/div/div[1]/div[2]/div[2]/div[1]/div[4]/button[2]')

    for i in range(0,no_of_reviews):
        try:
            next_button.click()
        except Exception:
         time.sleep(5)

    reviews_div = driver.find_element_by_xpath('//div[@data-load-more-section-id="reviews"]').get_attribute("innerHTML")
    soup_expatistan = BeautifulSoup(reviews_div, "html.parser")

    expand_pages = soup_expatistan.find_all("div", class_="single-review")

    for expand_page in expand_pages:
        print("Author Name: ", str(expand_page.find("span", class_="author-name").string.encode("utf-8")))
        print("Review Date: ", expand_page.find("span", class_="review-date").string.encode("utf-8"))
        print("Reviewer Link: ", expand_page.find("a", class_="reviews-permalink")['href'])
        reviewer_ratings = expand_page.find("div", class_="review-info-star-rating").find_next()['aria-label'];
        reviewer_ratings = ''.join(x for x in reviewer_ratings if x.isdigit())
        print("Reviewer Ratings: ", reviewer_ratings)
        print("Review Title: ", str(expand_page.find("span", class_="review-title").string))
        print("Review Body: ", str(expand_page.find("div", class_="review-body").text.encode("utf-8")))
        developer_reply = expand_page.find_parent().find("div", class_="developer-reply")
        if hasattr(developer_reply, "text"):
            print("Developer Reply: ", str(developer_reply.text.encode("utf-8")))
        else:
            print("Developer Reply: ", "")


driver.quit()

