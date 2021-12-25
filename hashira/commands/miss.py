import lightbulb
import hikari
mis = lightbulb.Plugin("mis")

mis.description = f'''

'''

@mis.command()
@lightbulb.command("ping", "shows the latency")
@lightbulb.implements(lightbulb.PrefixCommand,lightbulb.SlashCommand)
async def ping(ctx: lightbulb.Context):
    embed = hikari.Embed(title='ping :ping_pong:')
    embed.add_field(name='rn : ', value=f'{ctx.bot.heartbeat_latency * 1_000:,.0f}ms')
    embed.set_footer(icon=ctx.member.avatar_url, text=str(ctx.member))
    print(ctx.bot.plugins)
    await ctx.respond(embed=embed)



def load(bot):
    bot.add_plugin(mis)

def unload(bot):
    bot.remove_plugin(mis)

