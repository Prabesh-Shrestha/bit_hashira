import lightbulb
import hikari
class YourHelpCommand(lightbulb.BaseHelpCommand):
    async def send_bot_help(self, ctx: lightbulb.CommandContext):
        embed = hikari.Embed(title='Need help ??')
        embed.add_field(name='prefix', value='`>`')
        embed.add_field(name='commands: ', value=ctx.bot)
        embed.add_field(name='report: ', value='Prabesh#1395')
        embed.set_footer(icon=ctx.member.avatar_url, text=str(ctx.member))
        await ctx.respond(embed=embed)
        
    async def send_plugin_help(self, ctx, plugin):
        embed = hikari.Embed(title=f'Need help with {plugin.name}??')
        embed.add_field(name='description', value=plugin.description)
        embed.set_footer(icon=ctx.member.avatar_url, text=str(ctx.member))
        await ctx.respond(embed=embed)
 
    async def send_command_help(self, ctx, command):
        pass
    async def send_group_help(self, ctx, group):
        pass
    async def object_not_found(self, ctx, obj):
        pass
def load(bot):
    bot.d.old_help_command = bot.help_command
    bot.help_command = YourHelpCommand(bot)

def unload(bot):
    bot.help_command = bot.d.old_help_command
    del bot.d.old_help_command