import lightbulb
import hikari
snipe_plug = lightbulb.Plugin("snipe")

deleted_message = [] 


@snipe_plug.listener(hikari.MessageDeleteEvent)
async def on_message_delete(message: hikari.MessageDeleteEvent):
    if message.old_message.author.is_bot:
        return
    global deleted_message
    message_deleted = {
        'id': message.channel_id,
        'author': message.old_message.author,
        'message': message.old_message.content,
    }
    deleted_message.append(message_deleted)


@snipe_plug.command()
@lightbulb.command('snipe', 'shows the latest deleted message')
@lightbulb.implements(lightbulb.PrefixCommand, lightbulb.SlashCommand)
async def snipe(ctx: lightbulb.Context):
    for i in deleted_message:
        if i['id'] == ctx.channel_id:
            await ctx.respond(f"{i['author']}:{i['message']}")


def load(bot):
    bot.add_plugin(snipe_plug)

def unload(bot):
    bot.remove_plugin(snipe_plug)