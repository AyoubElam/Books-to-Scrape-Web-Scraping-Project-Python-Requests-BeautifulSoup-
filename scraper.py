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

soup = BeautifulStoneSoup(response.text,"html.parser") # pyright: ignore[reportUndefinedVariable]


#You ask BeautifulSoup:

#“Find all the HTML elements where
#tag = <article>
#and class = product_pod.”

#Why?
#Because each book on the page is inside a block like this:

#<article class="product_pod">
#    ...
#</article>

books = soup.find_all("article" , class_="product_pod") 