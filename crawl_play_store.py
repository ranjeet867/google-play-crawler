import requests
from bs4 import BeautifulSoup
import sys,io


# @author Ranjeet Singh <ranjeetsingh867@gmail.com>
# Moodify it according to your requirements

non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)


#Append your app store urls here
urls = ["https://play.google.com/store/apps/details?id=com.flipkart.android&hl=en", 
		"https://play.google.com/store/apps/details?id=com.amazon.mShop.android.shopping"]

for url in urls:

	page  = requests.get(url).text
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
	
	rating_bars = soup_histogram.find_all('div', class_ = "rating-bar-container")
	
	for rating_bar in rating_bars:
		print("Rating: ", rating_bar.find("span").text)
		print("Rating count: ", rating_bar.find("span", class_="bar-number").string)
		
	reviews_div = soup_expatistan.find(attrs={"data-load-more-section-id": "reviews"})
	expand_pages = reviews_div.find_all("div", class_="single-review")
	
	for expand_page in expand_pages:
		print("Author Name: ", str(expand_page.find("span", class_="author-name").a.string).translate(non_bmp_map))
		print("Review Date: ", expand_page.find("span", class_="review-date").string)
		print("Reviewer Link: ", expand_page.find("a", class_="reviews-permalink")['href'])
		reviewer_ratings = expand_page.find("div", class_="review-info-star-rating").find_next()['aria-label'];
		reviewer_ratings = ''.join(x for x in reviewer_ratings if x.isdigit())
		print("Reviewer Ratings: ", reviewer_ratings)
		print("Review Title: ", str(expand_page.find("span", class_="review-title").string).translate(non_bmp_map))
		print("Review Body: ", str(expand_page.find("div", class_="review-body").text).translate(non_bmp_map))
		developer_reply = expand_page.find_parent().find("div", class_="developer-reply")
		if hasattr(developer_reply, "text"):
			print("Developer Reply: ", str(developer_reply.text).translate(non_bmp_map))
		else:
			print("Developer Reply: ", "")
			
		
			
			
		
		
	
