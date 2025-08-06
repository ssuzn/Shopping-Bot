# 봇 명령어 핸들러
from discord.ext import commands
from crawler.musinsa import select_items_by_category, select_items_by_color
from utils.embed import create_item_embed

def setup_commands(bot):
    @bot.command(name="쇼핑")
    async def 쇼핑(ctx, category=None):
        if not category:
            await ctx.send("카테고리를 입력해주세요. 예) `!쇼핑 스니커즈`")
            return
        try:
            items = select_items_by_category(category)
            if not items:
                await ctx.send("해당 카테고리에서 상품을 찾을 수 없습니다.")
                return
            for item in items:
                embed = create_item_embed(item)
                await ctx.send(embed=embed)
        except Exception as e:
            await ctx.send(f"오류 발생: {e}")

    @bot.command(name="색상")
    async def 색상(ctx, category=None, color=None):
        if not category or not color:
            await ctx.send("카테고리와 색상을 입력해주세요. 예) `!색상 상의 green`")
            return
        try:
            items = select_items_by_color(category, color)
            if not items:
                await ctx.send("해당 조건의 상품을 찾을 수 없습니다.")
                return
            for item in items:
                embed = create_item_embed(item)
                await ctx.send(embed=embed)
        except Exception as e:
            await ctx.send(f"오류 발생: {e}")