import discord
from dotenv import load_dotenv
import os
from discord.ext import commands
from zip import *
from data import *

load_dotenv()
prefix = '!'
intents = discord.Intents.all() # 봇이 서버 멤버의 정보나 서버 멤버 리스트를 불러올 수 있도록 허용

client = commands.Bot(command_prefix=prefix, intents = intents)

@client.event
async def on_ready():
    print(f'안녕하세요 {client.user.name}이에요!')


@client.event # 봇이 서버에 초대되었을때
async def on_guild_join(guild):
    for channel in guild.text_channels:
        if channel.permissions_for(guild.me).send_messages:
            await channel.send("새로운 서버 " + str(guild) + " 에 접속하였어요!")
            await channel.send('!도움말을 입력하여 저를 이용해보세요.')


@client.event # 멤버 서버에 들어왔을때
async def on_member_join(member):
    message = '반가워요 {}님\n !명령어 를 통해 서비스를 제공받을 수 있어요.\n !도움말 을 입력해보세요.'.format(str(member.name))
    await find_channel(member.guild.text_channels).send(message)
    return None

@client.event # 멤버 서버에서 나갔을때
async def on_member_remove(member):
    message = "{}님이 서버를 떠나셨어요.".format(str(member.name))
    await find_channel(member.guild.text_channels).send(message)
    return None



@client.event
async def on_message(message):
    if message.author.bot: # 봇이 보낸 메세지는 무시
        return None

    if message.content.startswith("!도움말"):
        await message.channel.send(embed=help(message))

    if message.content.startswith("!쇼핑"): #실행
        val = message.content.split(' ') # [!쇼핑, 상의, green]

        if len(val) == 1: # !쇼핑만 입력했을 경우
            await message.channel.send(embed=desc_cloth(message)) # !쇼핑 설명 출력


        else: # !쇼핑 상의 입력했을 경우
            cate = val[1] # 상의, 아우터

            if cate not in list: # list에 없는 단어 입력
                embed = discord.Embed(title='잘못된 입력이에요.',
                                    description='다음 중 하나를 입력해주세요. \n `상의` `아우터` `바지` `원피스` `스커트` `스니커즈` `신발`',
                                      color=0xFF0000)
                embed.set_thumbnail(url='https://imgur.com/mABzlJu.jpg')
                await message.channel.send(embed=embed)
            else: # 잘 입력했으면 추천 결과
                await message.channel.send('옷장 뒤적이는중...')
                res = await message.channel.send(embed=select_cloth(cate))

    if message.content.startswith("!색상"): # !색상 상의 green
        val = message.content.split(' ')

        if len(val) == 1:
            await message.channel.send(embed=desc_color(message))


        elif len(val) == 2: # val[2]가 없을때
            embed = discord.Embed(title='잘못된 입력이에요.',
                                    description='카테고리와 색상을 형식에 맞게 입력해주세요!\n',
                                    color=0xFF0000)
            embed.set_thumbnail(url='https://imgur.com/HPTF4I7.jpg')
            await message.channel.send(embed=embed)
        else:
            cate = val[1] # 상의
            col = val[2] # green

            if cate not in list and col in color: # 카테고리 잘못 입력
                embed = discord.Embed(title='카테고리를 잘못 입력하셨어요.',
                                        description='다음 중 하나를 입력해주세요. \n'
                                                    ' `상의` `아우터` `바지` `원피스` `스커트` `스니커즈` `신발`',
                                         color=0xFF0000)
                embed.set_thumbnail(url='https://imgur.com/mABzlJu.jpg')
                await message.channel.send(embed=embed)

            elif col not in color and cate in list: # 색상 잘못 입력
                embed = discord.Embed(title='색상을 잘못 입력하셨어요.',
                                         description='다음 중 하나를 입력해주세요.\n'
                                                  '`black` `white` `green` `red` `yellow` `denim` `gray` `blue` `brown` `pink` `purple`',
                                        color=0xFF0000)
                embed.set_thumbnail(url='https://imgur.com/aYYSs1w.jpg')
                await message.channel.send(embed=embed)

            elif cate not in list and col not in color: # 카테고리, 색상 잘못 입력
                embed = discord.Embed(title='잘못된 입력이에요.',
                                        description='카테고리와 색상을 형식에 맞게 입력해주세요!\n',
                                        color=0xFF0000)
                embed.set_thumbnail(url='https://imgur.com/HPTF4I7.jpg')
                await message.channel.send(embed=embed)


            else: # 오류 없음
                await message.channel.send('옷장 뒤적이는중...')
                await message.channel.send(embed=select_color(cate, col))

    if message.content == "!추천받기":
        embed = discord.Embed(title='위 제품이 어떤지 추천해 주세요!', description='이모티콘을 눌러 투표해주세요.')
        res = await message.channel.send(embed=embed)
        await res.add_reaction('👍')
        await res.add_reaction('👎')


# with open('token.txt', 'r') as f:
#     token = f.read()

client.run(os.environ['token'])

