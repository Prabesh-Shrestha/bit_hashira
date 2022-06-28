import os
from hikari.presences import Activity, Status
import hashira
import sys
import hikari
import lightbulb
import hashira.tokens as tokens
try:
    if sys.argv[1] == 'launch':
        TOKEN = tokens.bot_token_real
    else:
        TOKEN = tokens.bot_token_test
except:
    print("using the test bot")
    TOKEN = tokens.bot_token_test


bot = lightbulb.BotApp(
    token=TOKEN,
    prefix=hashira.prefix,
    # default_enabled_guilds = hashira.guild_id
)


@bot.listen(hikari.StartedEvent)
async def on_started(event: hikari.StartingEvent) -> None:
    await bot.update_presence(status=Status.ONLINE, activity=Activity(name='Hello World!'))
    await (await bot.rest.fetch_channel(hashira.log_id)).send(
        f"{hashira.bot_name} is now online!"
    )
bot.load_extensions_from('./hashira/commands')



if __name__ == '__main__':
    if os.name != 'nt':
        import uvloop
        uvloop.install()
    bot.run()    



