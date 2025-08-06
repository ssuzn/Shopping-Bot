def setup_events(bot):
    @bot.event
    async def on_ready():
        print(f"{bot.user} 봇 준비 완료!")

    @bot.event
    async def on_member_join(member):
        await member.send("서버에 오신 것을 환영합니다!")

    @bot.event
    async def on_member_remove(member):
        print(f"{member.name}님이 서버를 떠났습니다.")