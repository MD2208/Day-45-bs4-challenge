from bs4 import BeautifulSoup
import requests 
## GET TOP VOTED ENTRY FROM THE FOLLOWING WEBSITE BY SCRAPING
response = requests.get('https://news.ycombinator.com/')
web_page = response.text

soup = BeautifulSoup(web_page, 'html.parser')
articles = soup.select('.titleline > a:nth-of-type(1)')
texts = [article.getText() for article in articles]
links = [article.get("href") for article in articles]


upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_='score') ]

max = 0
index = 0

for i in range(len(upvotes)):
    if max < upvotes[i]:
        max=upvotes[i]
        index = i 

print(upvotes[index], texts[index], links[index])
# with open(file="website.html", encoding="utf-8") as file:
#     contents = file.read()

# soup = BeautifulSoup(contents, 'html.parser')
# print(soup.title.string)