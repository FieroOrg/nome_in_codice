import discord
from util.exception import NotAllowedCommand
from game.match import Match, Status
from discord.ext import commands



class Game(commands.Cog):
    """The commands for handle the game

            !captain - Set the user as captain of a team

       """
    def __init__(self, bot, starterHelper):
        self.bot = bot
        self.starterHelper = starterHelper

    def join_as_master(self, guild, channel, member):
        if (guild.id,channel.id) in self.starterHelper.matches.keys():
            return self.starterHelper.matches[(guild.id, channel.id)].join_as_master(member)
        else:
            raise NotAllowedCommand('Match not started')

    def show_word(self, guild, channel, member, word):
        if (guild.id, channel.id) in self.starterHelper.matches.keys():
            return self.starterHelper.matches[(guild.id, channel.id)].show(member, word)
        else:
            raise NotAllowedCommand('Match not started')


    @commands.command()
    async def master(self, ctx, *, member: discord.Member = None):
        """Set the user as captain of a team"""
        try:
            member = member or ctx.author
            res = self.join_as_master(ctx.message.author.guild, ctx.message.channel, member)
            await ctx.send('{0.name} joined in {1} team~'.format(member, res))
            await ctx.send(self.starterHelper.print_status())
        except NotAllowedCommand as err:
            await ctx.send(err.message)

    # @commands.command()
    # async def show(self, ctx, *, member: discord.Member = None):
    #     """Set the user as captain of a team"""
    #     if (ctx.message.author.guild.id, ctx.message.channel.id) not in self.starterHelper.matches.keys() or\
    #             ((ctx.message.author.guild.id, ctx.message.channel.id) in self.starterHelper.matches.keys() and \
    #          self.starterHelper.matches[(ctx.message.author.guild.id, ctx.message.channel.id)].status == Status.PLAY):
    #         await ctx.send('It miss the word. Write !show [word]')
    #     else:
    #         await ctx.send('You can use this command only when a game is started. And it miss the word. Write !show [word]')


    @commands.command()
    async def show(self, ctx, word, *, member: discord.Member = None):
        """Set the user as captain of a team"""
        try:
            member = member or ctx.author
            res = self.show_word(ctx.message.author.guild, ctx.message.channel, member, word)
            await ctx.send('{0.name} show {1}~'.format(member, res))
            await ctx.send(self.starterHelper.print_status())
        except NotAllowedCommand as err:
            await ctx.send(err.message)
