# 무신사에서 실제로 상품을 크롤링하는 함수
import requests
from bs4 import BeautifulSoup
from crawler.data import list, color, url

def select_items_by_category(category):
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url[category], headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    items = soup.select(".li_inner")

    for item in items[:1]:  # 첫 번째 아이템만 보여줌
        title = item.select_one(".list_info > a").text.strip()
        link = "https:" + item.select_one(".list_info > a")["href"]
        price = item.select_one(".price").text.strip()
        img_url = "https:" + item.select_one("img")["data-original"]

        return {
            "title": title,
            "price": price,
            "img_url": img_url,
            "link": link
        }

def select_items_by_color(category, color):
    search_url = f"https://www.musinsa.com/search/musinsa/goods?q={category}+{color}"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(search_url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    items = soup.select(".li_inner")

    for item in items[:1]:
        title = item.select_one(".list_info > a").text.strip()
        link = "https:" + item.select_one(".list_info > a")["href"]
        price = item.select_one(".price").text.strip()
        img_url = "https:" + item.select_one("img")["data-original"]

        return {
            "title": title,
            "price": price,
            "img_url": img_url,
            "link": link
        }