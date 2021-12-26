# math
# rate
# run


import json
import lightbulb
import hikari
import requests
core = lightbulb.Plugin("core")

core.description = f'''



'''
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
@lightbulb.implements(lightbulb.PrefixCommand, lightbulb.SlashCommand)
async def say(ctx: lightbulb.Context):
    await ctx.respond(ctx.options.message)



@core.command()
@lightbulb.option("word",'word', str)
@lightbulb.command('meaning', 'searchs the meaning of a word')
@lightbulb.implements(lightbulb.PrefixCommand, lightbulb.SlashCommand)
async def meaning(ctx: lightbulb.Context):
    word = ctx.options.word
    response = requests.get(f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}")
    res = response.json()
    try:
        origin = res[0]["origin"]
    except:
        origin = "no origin found"
    try:
        example = res[0]["meanings"][0]["definitions"][0]["example"]
    except:
        example = "no examples"
    try:
        speech = res[0]["meanings"][0]["partOfSpeech"]
    except:
        speech = "no speech"
    des = f"""
    Word: {res[0]["word"]}
    Phonetic: {res[0]["phonetic"]}
    Origin: {origin}
    Part of speach: {speech}
    Definition:{res[0]["meanings"][0]["definitions"][0]["definition"]}
    Example: {example}"""
    embed = hikari.Embed(title=f"Meaning of {word}")
    embed.add_field(name = 'Description: \n', value=des)
    embed.set_footer(icon=ctx.member.avatar_url, text=str(ctx.member))
    await ctx.respond(embed=embed)



@core.command()
@lightbulb.option("expression",'expression', str)
@lightbulb.command('eval', 'solves simple math expression')
@lightbulb.implements(lightbulb.PrefixCommand, lightbulb.SlashCommand)
async def solve(ctx: lightbulb.Context):
    await ctx.respond(eval(ctx.options.expression))
    # fix 



# @core.command()
# @lightbulb.option("code",'code', modifier=lightbulb.OptionModifier.GREEDY)
# @lightbulb.command('run', 'runs a code')
# @lightbulb.implements(lightbulb.PrefixCommand, lightbulb.SlashCommand)
# async def solve(ctx: lightbulb.Context):
#     if ctx.interaction is None: 
#         expression = '\n'.join(ctx.options.code)
#         lang = expression.split("\n")[0][3:]
#         code = expression.split("\n", 1)[-1][:-3]
#         print(lang)
#         print(code)
#         client = PystonClient()
#         output = await client.execute(lang, code)
#         embed = hikari.Embed()
#         embed.add_field(name="Result", value=output)
#         embed.set_footer(icon_url=ctx.author.avatar_url, text=f"Requested by {ctx.author.name}")
#         await ctx.respond(embed=embed)


#     else: 
#         pass
    # lang = code.split("\n")[0][3:]
    # code = code.split("\n", 1)[-1][:-3]
    # client = PystonClient()
    # output = await client.execute(lang, code)
    # embed = hikari.Embed()
    # embed.add_field(name="Result", value=output)
    # embed.set_footer(icon_url=ctx.author.avatar_url, text=f"Requested by {ctx.author.name}")
    # await ctx.respond(embed=embed)

 











def load(bot):
    bot.add_plugin(core)

def unload(bot):
    bot.remove_plugin(core)