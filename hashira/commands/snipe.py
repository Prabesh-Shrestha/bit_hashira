import lightbulb
import hikari
import hashira

snipe_plug = lightbulb.Plugin("snipes")
snipe_plug.description = f'''
snipe:
snipes the last deleted message
{hashira.prefix}snipe
snipelist: 
lists all the snipes
{hashira.prefix}snipelist
edit: 
snipes the last edited message
{hashira.prefix}edit
'''
deleted_message = [] 
edited_message = []


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
    if len(deleted_message) > 10:
        deleted_message.pop(0)


@snipe_plug.listener(hikari.MessageUpdateEvent)
async def on_message_delete(message: hikari.MessageUpdateEvent):
    if message.is_bot:
        return

    global edited_message 

    edited_message_dict = {
        'id': message.channel_id,
        'author': message.author,
        'mes_old': message.old_message.content,
        'mes_new': message.content,
    }

    edited_message.append(edited_message_dict)
    if len(edited_message) > 10:
        edited_message.pop(0)


@snipe_plug.command()
@lightbulb.command('snipe', 'shows the latest deleted message')
@lightbulb.implements(lightbulb.PrefixCommand, lightbulb.SlashCommand)
async def snipe(ctx: lightbulb.Context):
    for i in deleted_message:
        if i['id'] == ctx.channel_id:
            embed = hikari.Embed()
            embed.add_field(name = 'lol remember this ? \n', value=f'{i["author"]}: {i["message"]}')
            embed.set_footer(icon=ctx.member.avatar_url, text=str(ctx.member))
            await ctx.respond(embed=embed)     
            break


@snipe_plug.command()
@lightbulb.command('snipelist', 'shows the latest deleted message')
@lightbulb.implements(lightbulb.PrefixCommand, lightbulb.SlashCommand)
async def snipe(ctx: lightbulb.Context):
    mes = ''
    for i in deleted_message:
        if i['id'] == ctx.channel_id:
            mes += f'{i["author"]}: {i["message"]}\n'
    
        embed = hikari.Embed()
        embed.add_field(name = 'lol remember this ? \n', value=mes)
        embed.set_footer(icon=ctx.member.avatar_url, text=str(ctx.member))
        await ctx.respond(embed=embed)     



@snipe_plug.command()
@lightbulb.command('edit', 'shows the latest edited message')
@lightbulb.implements(lightbulb.PrefixCommand, lightbulb.SlashCommand)
async def edit(ctx: lightbulb.Context):
    for i in edited_message:
        if i['id'] == ctx.channel_id:
            embed = hikari.Embed(title='Edit')
            embed.add_field(name = 'before', value=f'{i["author"]}: {i["mes_old"]}')
            embed.add_field(name = 'after', value=f'{i["author"]}: {i["mes_new"]}')
            embed.set_footer(icon=ctx.member.avatar_url, text=str(ctx.member))
            await ctx.respond(embed=embed)     



def load(bot):
    bot.add_plugin(snipe_plug)

def unload(bot):
    bot.remove_plugin(snipe_plug)