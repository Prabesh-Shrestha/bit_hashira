from hikari.permissions import Permissions
import lightbulb
from lightbulb import checks
import hashira
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

# @checks.bot_has_guild_permissions(Permissions.MANAGE_MESSAGES)
# @admin_plug.command()
# @lightbulb.command("clear", "deletes the chat")
# @lightbulb.option("limit",'limit', int)
# @lightbulb.implements(lightbulb.PrefixCommand,lightbulb.SlashCommand)
# async def shut(ctx: lightbulb.Context):
#     pass
# purge 
# ban 
# kick


def load(bot):
    bot.add_plugin(admin_plug)

def unload(bot):
    bot.remove_plugin(admin_plug)

