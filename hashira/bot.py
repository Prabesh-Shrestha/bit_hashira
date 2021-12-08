import hikari
import lightbulb
import hashira.tokens as tokens
import hashira


bot = lightbulb.BotApp(
    token=tokens.bot_token,
    prefix=hashira.prefix,
    default_enabled_guilds = hashira.guild_id
)


@bot.listen(hikari.StartedEvent)
async def on_started(event: hikari.StartingEvent) -> None:
    await (await bot.rest.fetch_channel(hashira.log_id)).send(
        f"{hashira.bot_name} is now online!"
    )



bot.load_extensions_from('./hashira/commands')

