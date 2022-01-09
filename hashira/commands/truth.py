import lightbulb
import hikari
from lightbulb.commands.base import Command
import hashira
import random 
truth_plug = lightbulb.Plugin("truth_and_dare")
truth_plug.description = f'''
Wanna play truth and dare ? 
start your session by registering
`{hashira.prefix}register`

start the game by typing
`{hashira.prefix}start`

select truth or dare by typing
`{hashira.prefix}truth` or `{hashira.prefix}dare`

to end the session typing
`{hashira.prefix}end`

if you want to send some question that can be added here just type 
`{hashira.prefix}tadsuggest <question>`

'''


turth_question = [
    'would you date ur bff? (male/female)',
    'would you like to slap someone who you dont know for absolute no reason :joy: ?',
    'would you kill someone that u love the most to protect someone u love more',
    'would you have a one night stand with a hiv infected person even if they are hot',
    'have you ever masterbated sniffing someone\'s underwear?',
    'how many males or females teacher have you had crush on ? *uwu*',
    'what is 3+3',
    'Why did your last relationship break down?',
    'Have you ever peed in the shower?',
    'What\'s your worst habit?',
    'how many children have you washed down the drain?',
]

dare_question = [
    'try to eat a banana with your foot', 
    'ask your crush out', 
    'chew a chewing gum and put it inside ur nose'
    'suck your toes',
    'go to `https://www.twitch.tv/shishir3d` and `https://www.twitch.tv/idi0city` and sub to them',
    'give your bff, a spoiler to of a movie they havnt watched, but are planing to',
    'let your friend use a social media account to post something embrassing that you are famous on (>50 followers)',
    'watch sasbahu series(indian) on loop on 10x speed'
]
session = []

@truth_plug.command()
@lightbulb.command("register", "register's the user")
@lightbulb.implements(lightbulb.PrefixCommand,lightbulb.SlashCommand)
async def lists(ctx: lightbulb.Context):
    global session
    user = ctx.author.id
    session.append(user)
    await ctx.respond('sure buddy')



@truth_plug.command()
@lightbulb.command("start", "starts the game")
@lightbulb.implements(lightbulb.PrefixCommand,lightbulb.SlashCommand)
async def lists(ctx: lightbulb.Context):
    usr = random.choice(session)
    await ctx.respond(f'its your turn <@{usr}> \n choose truth or dare :smirk:')


@truth_plug.command()
@lightbulb.command("truth", "should be done when the user wants to say truth")
@lightbulb.implements(lightbulb.PrefixCommand,lightbulb.SlashCommand)
async def lists(ctx: lightbulb.Context):
    question = random.choice(turth_question)
    await ctx.respond(question)


@truth_plug.command()
@lightbulb.command("dare", "should be done when the user wants a dare")
@lightbulb.implements(lightbulb.PrefixCommand,lightbulb.SlashCommand)
async def lists(ctx: lightbulb.Context):
    question = random.choice(dare_question)
    await ctx.respond(question)


@truth_plug.command()
@lightbulb.command("end", "end the game")
@lightbulb.implements(lightbulb.PrefixCommand,lightbulb.SlashCommand)
async def lists(ctx: lightbulb.Context):
    global session
    session = []
    await ctx.respond('sure buddy')


@truth_plug.command()
@lightbulb.option("question",'question', modifier = lightbulb.commands.OptionModifier.GREEDY)
@lightbulb.command("tadsuggest", "send some random questions to be added in the list")
@lightbulb.implements(lightbulb.PrefixCommand,lightbulb.SlashCommand)
async def lists(ctx: lightbulb.Context):
    if ctx.interaction is None: 
        question = " ".join(ctx.options.question)
    else: 
        question  = ctx.options.question

    await truth_plug.app.rest.create_message(hashira.truth_channel, question)

def load(bot):
    bot.add_plugin(truth_plug)

def unload(bot):
    bot.remove_plugin(truth_plug)

