from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/")
soup = BeautifulSoup(response.text, 'html.parser')
herf = soup.find(name ="a", class_ ="timeline")





#with open("day-41/website.html", "r",encoding='utf-8') as web_file :
    #html_content = web_file.read()

#soup = BeautifulSoup(html_content,"html.parser")
##print(soup.prettify())

#all_anchor_tags = soup.find_all(name = "a")
##print(all_anchor_tags)

#for tag in all_anchor_tags :
    #print(tag.get("href"))
#
