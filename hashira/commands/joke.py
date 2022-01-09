import requests
import lightbulb
import hashira
joke_plug= lightbulb.Plugin("jokes")
joke_plug.description= f'''
for random jokes type: 
{hashira.prefix}random_joke
'''

random_joke = 'https://v2.jokeapi.dev/joke/Any?safe-mode'
def getreq(url):
    response = requests.get(url)
    waifupic = response.json()
    return waifupic

@joke_plug.command()
@lightbulb.command("random_joke", "presents random jokes")
@lightbulb.implements(lightbulb.PrefixCommand,lightbulb.SlashCommand)
async def randjoke(ctx: lightbulb.Context) -> None:
    try:
        res = getreq(random_joke)
        ans = f'''
        {res['setup']}
        {res['delivery']}
    '''
        await ctx.respond(ans)
    except:
        await ctx.respond("I can't find any jokes")
        # await ctx.respond("yug ko black hole maybe? :thinking:")


# never 
# gonna 
# give 
# you 
# up

def load(bot):
    bot.add_plugin(joke_plug)

def unload(bot):
    bot.remove_plugin(joke_plug)


