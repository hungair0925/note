import re
import csv
import requests
from bs4 import BeautifulSoup

URL = "https://honto.jp/ranking/gr/bestseller_1101_1201_011.html"
response = requests.get(URL)
response.encoding = response.apparent_encoding
soup = BeautifulSoup(response.text, "html.parser")
product_list_html = soup.find_all("div", class_="stContents")

with open("book_rank.csv", "w", encoding="utf-8") as f:
    field_name = ["ランク", "タイトル", "著者", "値段(円)"]
    writer = csv.DictWriter(f, fieldnames=field_name)
    writer.writeheader()
    for i, tag in enumerate(product_list_html):
        author_tag = tag.find("ul", class_="stData")
        title_tag = tag.find("h2", class_="stHeading")
        price_tag = tag.find("li", class_="stPrice")
        author = author_tag.li.a.get_text()

        #正規表現を使わなかったとき
        """
        replace_target = ["（著）", "（編著）", "（監修）"]
        for rep in replace_target:
            if rep in author:
                author = author.replace(rep, "")
        """

        author = re.sub("（.*?）", "", author).rstrip()
        title = title_tag.get_text()
        title = re.sub("（.*?）", "", title).rstrip()
        price = price_tag.span.get_text().replace("円", "")
        context = {"ランク": i + 1, "タイトル": title, "著者": author, "値段(円)": price}
        writer.writerow(context)
