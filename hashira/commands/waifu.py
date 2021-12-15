import requests
import lightbulb

waifu= lightbulb.Plugin("waifu")



def getwaifu(type, catagory):
    try:
        response = requests.get(f"https://api.waifu.pics/{type}/{catagory}")
        waifupic = response.json()["url"]
        return waifupic
    except:
        response = requests.get(f"https://api.waifu.pics/{type}/{catagory}")
        waifupic = response.json()["url"]
        return waifupic


@waifu.command()
@lightbulb.option("catagory",'catagory', str)
@lightbulb.command("waifu", "shows waifu")
@lightbulb.implements(lightbulb.SlashCommand)
async def ping(ctx: lightbulb.Context) -> None:
    if ctx.get_channel().is_nsfw():
        await ctx.respond(getwaifu('nsfw', str(ctx.options.catagory)))
    else:
        await ctx.respond(getwaifu('sfw', str(ctx.options.catagory)))



def load(bot):
    bot.add_plugin(waifu)

def unload(bot):
    bot.remove_plugin(waifu)

