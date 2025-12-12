#used to send HTTP requests to websites & It allows you to download the HTML of a webpage
#Basically: “Hey website, give me the page content.”
import requests     


#BeautifulSoup, a tool that makes it easy to read and search HTML. BeautifulSoup converts HTML code into an object you can navigate like:
#soup.find()

#soup.find_all()

#soup.select()

#from bs4 import BeautifulStoneSoup




url = "https://books.toscrape.com/catalogue/page-1.html"

response = requests.get(url)

soup = BeautifulStoneSoup(response.text,"html.parser")


books = soup.find_all("article" , class_="product_pod") 