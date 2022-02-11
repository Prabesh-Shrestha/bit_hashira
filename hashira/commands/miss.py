import lightbulb
import hikari
import hashira 
mis = lightbulb.Plugin("mis")

mis.description = f'''
invite: 
invite link of the bot

{hashira.prefix}invite 

ping: 
shows the latency of the bot 

{hashira.prefix}ping

'''

@mis.command()
@lightbulb.command("ping", "shows the latency")
@lightbulb.implements(lightbulb.PrefixCommand,lightbulb.SlashCommand)
async def ping(ctx: lightbulb.Context):
    embed = hikari.Embed(title='ping :ping_pong:')
    embed.add_field(name='rn : ', value=f'{ctx.bot.heartbeat_latency * 1_000:,.0f}ms')
    embed.set_footer(icon=ctx.member.avatar_url, text=str(ctx.member))
    await ctx.respond(embed=embed)

@mis.command()
@lightbulb.command("invite", "invite link")
@lightbulb.implements(lightbulb.PrefixCommand,lightbulb.SlashCommand)
async def inv(ctx: lightbulb.Context):
    embed = hikari.Embed()
    embed.add_field(name='Link: ', value=hashira.INV_LINK)
    await ctx.respond(embed=embed)




def load(bot):
    bot.add_plugin(mis)

def unload(bot):
    bot.remove_plugin(mis)

