import requests
import lightbulb
import hashira
waifu_plug= lightbulb.Plugin("waifus")
waifu_plug.description= f'''
SFW:
waifu, neko, shinobu, megumin, bully, cuddle, cry, hug, awoo, kiss, lick, pat, smug, bonk, yeet, blush, smile, wave, highfive, handhold, nom, bite, glomp, slap, kill, kick, happy, wink, poke, dance, cringe
NSFW:
waifu, neko, trap, blowjob
example: 
`{hashira.prefix}waifu shinobu`
'''


def getwaifu(type, catagory):
    try:
        response = requests.get(f"https://api.waifu.pics/{type}/{catagory}")
        waifupic = response.json()["url"]
        return waifupic
    except:
        response = requests.get(f"https://api.waifu.pics/{type}/{catagory}")
        waifupic = response.json()["url"]
        return waifupic


@waifu_plug.command()
@lightbulb.option("catagory",'catagory', str)
@lightbulb.command("waifu", "shows waifu")
@lightbulb.implements(lightbulb.PrefixCommand,lightbulb.SlashCommand)
async def ping(ctx: lightbulb.Context) -> None:
    try:
        if ctx.get_channel().is_nsfw():
            await ctx.respond(getwaifu('nsfw', str(ctx.options.catagory)))
    except:
            await ctx.respond(getwaifu('sfw', str(ctx.options.catagory)))



def load(bot):
    bot.add_plugin(waifu_plug)

def unload(bot):
    bot.remove_plugin(waifu_plug)

