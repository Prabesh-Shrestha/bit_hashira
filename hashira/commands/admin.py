from hikari.permissions import Permissions
import lightbulb
from lightbulb import checks
import hikari 
import hashira
import datetime
admin_plug = lightbulb.Plugin("admin")
admin_plug.description = f'''
purge:
deletes all the message up to a limit
{hashira.prefix}purge <number>
ban: 
bans the user from the server
{hashira.prefix}ban @user reason
kick:
kicks the user from the server
{hashira.prefix}kick @user reason
unban:
unbans the user from the server
{hashira.prefix}unban @user reason

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
async def purge_channel(ctx: lightbulb.Context) -> None:
    num_msgs = ctx.options.messages
    channel = ctx.get_channel()
    messages = list(await channel.fetch_history().limit(num_msgs+ 1))
    await ctx.app.rest.delete_messages(channel, messages)


@checks.bot_has_guild_permissions(Permissions.BAN_MEMBERS)
@admin_plug.command
@lightbulb.option("member", "member", type=hikari.Member, required=True)
@lightbulb.option("reason", "reason", type=str, required=True)
@lightbulb.command("ban", "bans the member")
@lightbulb.implements(lightbulb.PrefixCommand, lightbulb.SlashCommand)
async def ban_usr(ctx: lightbulb.Context) -> None:
    await ctx.options.member.ban(reason=ctx.options.reason)
    await ctx.respond(f"{ctx.options.member.mention} has been banned")

@checks.bot_has_guild_permissions(Permissions.BAN_MEMBERS)
@admin_plug.command
@lightbulb.option("member", "member", type=hikari.Member, required=True)
@lightbulb.option("reason", "reason", type=str, required=True)
@lightbulb.command("unban", "unbans the member")
@lightbulb.implements(lightbulb.PrefixCommand, lightbulb.SlashCommand)
async def unban_usr(ctx: lightbulb.Context) -> None:
    await ctx.get_guild().unban(user=ctx.options.member, reason=ctx.options.reason)
    await ctx.respond(f"{ctx.options.member.mention} has been unbanned")



@checks.bot_has_guild_permissions(Permissions.KICK_MEMBERS)
@admin_plug.command
@lightbulb.option("member", "member", type=hikari.Member, required=True)
@lightbulb.option("reason", "reason", type=str, required=True)
@lightbulb.command("kick", "kicks the member")
@lightbulb.implements(lightbulb.PrefixCommand, lightbulb.SlashCommand)
async def kick_usr(ctx: lightbulb.Context) -> None:
    await ctx.options.member.kick(reason=ctx.options.reason)
    await ctx.respond(f"{ctx.options.member.mention} has been kicked")


def load(bot):
    bot.add_plugin(admin_plug)

def unload(bot):
    bot.remove_plugin(admin_plug)

