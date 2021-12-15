# meaning 
# av [done]
# math
# rate
# run
# quote [done]
# say 


import json
import lightbulb
import hikari
import requests
core = lightbulb.Plugin("core")

def GetQuote():
    response = requests.get("https://zenquotes.io/api/random")
    jsondata = json.loads(response.text)
    quote = jsondata[0]["q"] + " by " + jsondata[0]["a"]
    return quote


@core.command()
@lightbulb.option("member",'member', hikari.Member)
@lightbulb.command('av', 'shows the av of a user')
@lightbulb.implements(lightbulb.PrefixCommand, lightbulb.SlashCommand)
async def av(ctx: lightbulb.Context):
    embed = hikari.Embed(title=f"Avatar: {ctx.options.member}")
    embed.set_image(ctx.options.member.avatar_url)
    print(ctx.member.avatar_url)
    embed.set_footer(icon=ctx.member.avatar_url, text=str(ctx.member))
    await ctx.respond(embed=embed)


@core.command()
@lightbulb.command('quote', 'generates random quotes')
@lightbulb.implements(lightbulb.PrefixCommand, lightbulb.SlashCommand)
async def quote(ctx: lightbulb.Context):
    _quote = GetQuote()
    embed = hikari.Embed()
    embed.add_field(name = 'Quote: \n', value=_quote)
    embed.set_footer(icon=ctx.member.avatar_url, text=str(ctx.member))
    await ctx.respond(embed=embed)

@core.command()
@lightbulb.option("message",'message', str)
@lightbulb.command('say', 'order the bot to say something')
@lightbulb.implements(lightbulb.PrefixCommand)
async def say(ctx: lightbulb.Context):
    await ctx.respond(ctx.options.message)
    # await ctx.respond()





def load(bot):
    bot.add_plugin(core)

def unload(bot):
    bot.remove_plugin(core)