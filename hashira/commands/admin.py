from hikari.permissions import Permissions
import lightbulb
from lightbulb import checks
import hashira
import datetime
admin_plug = lightbulb.Plugin("admin")
admin_plug.description = f'''


'''


@admin_plug.command()
@lightbulb.command("shutdown", "turns off the bot")
@lightbulb.implements(lightbulb.PrefixCommand,lightbulb.SlashCommand)
async def shut(ctx: lightbulb.Context):
    if str(ctx.author.id) == hashira.creator_id:
        await ctx.respond('done!!')
        await ctx.bot.close()
    else:
        await ctx.respond('u are not my boss lmao xD')

@checks.bot_has_guild_permissions(Permissions.MANAGE_MESSAGES)
@admin_plug.command
@lightbulb.option("messages", "The number of messages to purge.", type=int, required=True)
@lightbulb.command("purge", "Purge messages within the last hour.")
@lightbulb.implements(lightbulb.PrefixCommand, lightbulb.SlashCommand)
async def userinfo(ctx: lightbulb.Context) -> None:
    num_msgs = ctx.options.messages
    channel = ctx.get_channel()
    messages = list(await channel.fetch_history().limit(num_msgs+ 1))
    await ctx.app.rest.delete_messages(channel, messages)
# ban 
# kick


def load(bot):
    bot.add_plugin(admin_plug)

def unload(bot):
    bot.remove_plugin(admin_plug)

