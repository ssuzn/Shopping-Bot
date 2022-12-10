import discord
from bs4 import BeautifulSoup
import requests
import random
from data import *


# def cody(cod):
#     url = f'https://www.musinsa.com/app/styles/lists?use_yn_360=&style_type={style[cod]}&brand=&model=&tag_no=&max_rt=&min_rt=&display_cnt=60&list_kind=big&sort=date&page=1'
#
#     res = requests.get(url).text
#     soup = BeautifulSoup(res, "html.parser")
#
#     data = soup.select('div.wrap > div.right_area > form > div.right_contents.hover_box > div > ul')
#
#     b = data.select_one('li > div.style-list-item__thumbnail > a > div > img')['src']
#     c = data.select_one('li:nth-child(1) > img.style-list-thumbnail__img').get('src')
#
#     embed = discord.Embed(title='코디 추천', description='ㅤ', color=0x3399FF)
#     embed.set_image(url='http:'+ )
#
#     return (embed)
#

def find_channel(channels):
    position_array = [i.position for i in channels]

    for i in channels:
        if i.position == min(position_array):
            return i

def help(message): # 도움말
    embed = discord.Embed(title="저는 이런 기능들을 해요!", description="  ", color=0x3399FF)
    embed.set_thumbnail(url='https://imgur.com/fIJcRzc.jpg')
    embed.add_field(name='ㅤ', value='ㅤ', inline=True)
    embed.add_field(name='카테고리에서 찾길 원하시나요?',
                    value='`!쇼핑을 입력해보세요.\n`'
                          '선택하신 카테고리에서 가장 인기 있는 제품을 추천해드려요!\n\n',
                    inline=False)
    # embed.add_field(name='ㅤ', value='ㅤ', inline=True)
    embed.add_field(name='찾으시는 색상이 있으신가요?',
                    value='`!색상을 입력해보세요.`\n'
                          '선택하신 카테고리에서 원하시는 색상의 가장 인기 있는 제품을 추천해드려요!\n',
                    inline=False)
    # embed.add_field(name='ㅤ', value='ㅤ', inline=True)
    embed.add_field(name='제품 구매에 고민되시나요?',
                    value='`!추천 받기를 입력해보세요.`\n'
                          '다른 사람들의 투표를 받을 수 있어요!\n',
                    inline=False)
    embed.add_field(name='ㅤ', value='ㅤ', inline=True)
    embed.set_footer(text=f'즐거운 쇼핑 되세요 {message.author.name}님!', icon_url='https://imgur.com/zEgfFkI.jpg')
    return (embed)


def desc_cloth(message): # !쇼핑 에 대한 설명
    embed = discord.Embed(title='!쇼핑 에 대한 도움말이에요', description='ㅤ', color=0x3399FF)
    embed.add_field(name='1. 아래 목록에서 원하는 카테고리를 선택해주세요.', value='`상의` `아우터` `바지` `원피스` `스커트` `스니커즈` `신발`', inline=False)
    embed.add_field(name='2. `!쇼핑 (선택한 카테고리)` 를 입력해주세요.\n'
                         '해당 카테고리에서 가장 인기있는 제품을 추천해드려요.', value='ex. !쇼핑 상의', inline=False)
    return (embed)

def desc_color(message): # !색상 에 대한 설명
    embed = discord.Embed(title='!색상 에 대한 도움말이에요', description='ㅤ', color=0x3399FF)
    embed.add_field(name='1. 아래 목록에서 원하는 카테고리를 선택해주세요.', value='`상의` `아우터` `바지` `원피스` `스커트` `스니커즈` `신발`', inline=False)
    embed.add_field(name='2. 아래 목록에서 원하는 색상을 선택해주세요.', value='`black` `white` `green` `red` `yellow` `denim` `gray` `blue` `brown` `pink` `purple`', inline=False)
    embed.add_field(name='3. `!색상 (선택한 카테고리) (선택한 색상)` 을 입력해주세요.\n'
                         '선택하신 카테고리에서 찾으시는 색상 중 가장 인기있는 제품을 추천해드려요.', value='ex. !색상 상의 black', inline=False)
    return (embed)

def select_cloth(cate): # 카테고리에서 추천
    url = baseurl + list[cate]
    res = requests.get(url).text
    soup = BeautifulSoup(res, "html.parser")

    data = soup.select_one("#searchList > li:nth-child(1) > div.li_inner")  # 가장 첫번째 제품에서 찾기

    image = data.select_one("div.list_img > a > img")["data-original"]
    link = data.select_one("div.article_info > p.list_info > a")["href"]
    brand = data.select_one('p.item_title').text
    title = data.select_one('a').get('title')
    price = data.select_one('p.price').text.replace('\n', '').split()
    if len(price) > 1:  # 원가 할인가 존재
        prime = price[0]
        discount = price[1]
    else:  # 할인가 존재하지 않음
        prime = price[0]
        discount = "이 제품은 할인중이 아니에요!"

    if data.select_one('p.point'):  # 리뷰수가 존재하면
        review = data.select_one('p.point > span.count').text
    else:  # 리뷰수가 존재하지 않으면
        review = 0

    embed = discord.Embed(title=title, description=brand, color=0x00FF00)
    embed.set_thumbnail(url="http:" + image)
    embed.add_field(name='원가', value=prime)
    embed.add_field(name='할인가', value=discount)
    embed.add_field(name='리뷰수', value=review)
    embed.add_field(name='구매 링크', value='https:' + link, inline=False)

    return(embed)

def select_color(cate, col): # 카테고리 + 색상에서 추천
    url = baseurl + list[cate] + colorurl[0] + list[cate] + colorurl[1] + color[col] + colorurl[2]

    res = requests.get(url).text
    soup = BeautifulSoup(res, "html.parser")
    data = soup.select_one("#searchList > li:nth-child(1) > div.li_inner")  # 가장 첫번째 제품에서 찾기

    image = data.select_one("div.list_img > a > img")["data-original"]
    link = data.select_one(".article_info > p.list_info > a")["href"]
    brand = data.select_one('p.item_title').text
    title = data.select_one('a').get('title')
    price = data.select_one('p.price').text.replace('\n', '').split()
    if len(price) > 1: # 원가 할인가 존재
        prime = price[0]
        discount = price[1]
    else: # 할인가 존재하지 않음
        prime = price[0]
        discount = "이 제품은 할인하지 않아요!"

    if data.select_one('p.point'):  # 리뷰수가 존재하면
        review = data.select_one('p.point > span.count').text
    else:  # 리뷰수가 존재하지 않으면
        review = 0

    embed = discord.Embed(title=title, description=brand, color=0x00FF00)
    embed.set_thumbnail(url="https:" + image)
    embed.add_field(name='원가', value=prime)
    embed.add_field(name='할인가', value=discount)
    embed.add_field(name='리뷰수', value=review)
    embed.add_field(name='구매 링크', value='https:' + link, inline=False)

    return (embed)

def hello(message):
    txt = ['안녕하세요', '또 와주셨군요', '반가워요']
    ans = random.randint(0, len(txt)-1)
    return txt[ans]