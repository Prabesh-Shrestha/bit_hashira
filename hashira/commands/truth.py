import lightbulb
import hikari 
import hashira
import random 
truth_plug = lightbulb.Plugin("truth_and_dare")
truth_plug.description = f'''
pp: 
shows that member's pp size
>pp @user
'''


session = []



@truth_plug.command()
@lightbulb.command("register", "register's the user")
@lightbulb.implements(lightbulb.PrefixCommand,lightbulb.SlashCommand)
async def lists(ctx: lightbulb.Context):
    global session
    user = ctx.author.id
    session.append(user)
    await ctx.respond()



@truth_plug.command()
@lightbulb.command("start", "starts the game")
@lightbulb.implements(lightbulb.PrefixCommand,lightbulb.SlashCommand)
async def lists(ctx: lightbulb.Context):
    usr1 = random.choice(session)
    usr2 = random.choice(session)
    while usr1 == usr2:
        usr2 = random.choice(session)  
    await ctx.respond(f'{usr1} ask {usr2}')


def load(bot):
    bot.add_plugin(truth_plug)

def unload(bot):
    bot.remove_plugin(truth_plug)

