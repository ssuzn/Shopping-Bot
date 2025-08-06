# 크롤링 결과를 Discord Embed 형태로 만들어주는 함수
import discord

def create_item_embed(item):
    embed = discord.Embed(
        title=item["title"],
        url=item["link"],
        description=item["price"],
        color=0x00BFFF  # 디스코드 블루 컬러
    )
    embed.set_image(url=item["img_url"])
    return embed