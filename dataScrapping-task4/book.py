import requests as rq
from bs4 import BeautifulSoup
import pandas as pd

burl='https://books.toscrape.com/'

bHeader = {
     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36'
}

bresp=rq.get(url=burl,headers=bHeader)

bsoup=BeautifulSoup(bresp.content,'html.parser')

books=bsoup.find_all('article', attrs={'class':'product_pod'})

bookData=[]

for bookTitle in books:
  title=bookTitle.find('h3').a['title']
  price=bookTitle.find('p', attrs={'class':'price_color'}).text
  rating=bookTitle.find('p', attrs={'class':'star-rating'})['class'][1]

  book={
       'title': title,
        'price': price,
        'rating': rating
        }

  bookData.append(book)

  print('title =', title)
  print('price =', price)
  print('rating =', rating)

bookdf=pd.DataFrame(bookData)
bookdf.to_csv('books.csv')


