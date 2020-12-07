import discord
from util.exception import NotAllowedCommand
from game.match import Match, Status
from discord.ext import commands
from game.database import Database

class Adder(commands.Cog):
    """The commands for handle the adding of words

       """
    def __init__(self,bot):
        self.bot = bot
        self.user_tag = dict()
        self.db = Database() # it's the right place? 

    @commands.command()
    async def addtag(self, ctx, tag, lang, *, member: discord.Member = None):
        if not isinstance(ctx.message.channel, discord.DMChannel):
            await ctx.send('You should send !addtag [tag] [lang] in a private message')
        else:
            try:
                member = member or ctx.author
                self.db.add_tag(tag, lang)
                await ctx.send('{0.name} added {1} tag'.format(member, tag))
                await ctx.send(self.starterHelper.print_status())
            except NotAllowedCommand as err:
                await ctx.send(err.message)

    @commands.command()
    async def addword(self, ctx, tag, *, member: discord.Member = None):

        if not isinstance(ctx.message.channel, discord.DMChannel):
            await ctx.send('You should send !addword [tag] in a private message')
        else:
            try:
                member = member or ctx.author
                if self.db.get_tag_id(tag) is not None:
                    self.user_tag[member.id] = tag
                    await ctx.send('write the words. One word/term in each line')
                else:
                    raise NotAllowedCommand("the tag does not exists")
            except NotAllowedCommand as err:
                await ctx.send(err.message)

    @commands.Cog.listener('on_message')
    async def word_listener(self, ctx, *, member: discord.Member = None):

        if ctx.author == self.bot.user:
            return
        member = member or ctx.author
        if isinstance(ctx.message.channel, discord.DMChannel) and member.id in self.user_tag.keys():
            words = ctx.message.text.strip('\n')
            self.db.add_words(words, self.user_tag[member.id])

    @commands.command()
    async def stopword(self, ctx, *, member: discord.Member = None):

        if not isinstance(ctx.message.channel, discord.DMChannel):
            await ctx.send('You should send !addword [tag] in a private message')
        else:
            try:
                member = member or ctx.author
                self.user_tag.pop(member.id, None)
                await ctx.send('Stop insering words')
            except NotAllowedCommand as err:
                await ctx.send(err.message)
