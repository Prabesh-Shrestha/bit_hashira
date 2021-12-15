import lightbulb

text_plug= lightbulb.Plugin("texts")



@text_plug.command()
@lightbulb.command("ping", "Checks that the bot is alive")
@lightbulb.implements(lightbulb.SlashCommand)
async def ping(ctx: lightbulb.Context) -> None:
    await ctx.respond("Pong!")



def load(bot):
    bot.add_plugin(text_plug)

def unload(bot):
    bot.remove_plugin(text_plug)
