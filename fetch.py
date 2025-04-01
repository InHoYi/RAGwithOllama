import requests
from bs4 import BeautifulSoup
from datetime import datetime

raw = requests.get('https://www.busan.com/') # 원하는 채널로 변경
soup = BeautifulSoup(raw.content, "html.parser")

search = soup.find_all('div', class_ = "arl_001")

content = search[0].text
content.replace('\t', '')
print(content)
article = open(f"article/article{datetime.today().strftime("%Y%m%d")}.txt", "w", encoding = "UTF-8")
article.write(content)
article.close()