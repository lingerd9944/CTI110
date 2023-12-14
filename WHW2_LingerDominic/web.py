from googlesearch import search
import requests
from bs4 import BeautifulSoup
import re

searchRequest = input('What would you like to search?')
i = 10
k = 0
mylines = []

for j in search(searchRequest, tld="co.in", num = i, stop = i, pause = 2):
    print(j)
    url = j 
    page = requests.get(url)
    if page.status_code == 200:
        soup = BeautifulSoup(page.content, "html.parser")
        text = soup.find_all(['p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6'])
        scrapedText = ' '.join(element.get_text() for element in text)
        with open('urls2.txt', 'a') as f:
            f.write('\n')
            f.write('\n')
            f.write(url)
            f.write('\n')
            f.write('\n')
        for line in scrapedText[:500]:            
            with open('urls2.txt', 'a') as f:
                f.write(line)


