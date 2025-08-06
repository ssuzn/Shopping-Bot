import discord
from discord.ext import commands
from dotenv import load_dotenv
import os

from bot.commands import setup_commands
from bot.events import setup_events

# .env 파일에서 DISCORD_TOKEN 불러오기
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

# 디스코드 봇 기본 설정
intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)

# 명령어 및 이벤트 핸들러 등록
setup_commands(bot)
setup_events(bot)

# 봇 실행
if __name__ == "__main__":
    bot.run(TOKEN)