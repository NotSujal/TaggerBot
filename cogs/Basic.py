from discord.ext import commands
import asyncio
from googlesearch import search
from assist import *


class Basic(commands.Cog):
    """
    This catagory holds the commands which are used by a normal user
    """
    def __init__(self,client):
        self.client = client

    @commands.command(aliases = ['t'])
    async def tag(self, ctx,*,query):
        """
        search for a answer for a provided query.
        """

        try:
            response = getdata(verified_tags,query)
            response += "  ⚡`(is verified)`"
        except:
            try:
                response = getdata(unverified_tags,query)
                response += "  ⛔`(unverified)`"
                

            except:
                for i in search(query,safe="on",num = 1,start = 0,stop = 1,pause= 2):
                    response = i
                    await ctx.send(response)
                    createdata(requested_tags,query)
        await ctx.send(f"There was no tag named {query}, \r\nAdded request to add this tag.")
        
        
    @commands.command(aliases =["add"])
    async def addtag(self, ctx,query,answer):
        """
        Add a tag to the data.
        """
        answer += " \r\n Source: " + ctx.message.author.name
        createdata(unverified_tags,query)
        await asyncio.sleep(1)
        savedata(unverified_tags,query,answer)
        await ctx.send(f"Thanks for adding tag,{ctx.message.author.mention}! \r\nThe given data is Successfully added to unverified list of tags and will be soon checked and verified!")


    @commands.command(aliases = ["eu"])
    async def editunverified(self,ctx,query,edited_answer):
        """
        edit your unverified tags
        """

        try:
            current_answer = getdata(unverified_tags,query)
        except:
            await ctx.send("This Tag doesn't exist")
            return
        if current_answer != edited_answer:
            current_answer = edited_answer
            await asyncio.sleep(1)
            savedata(unverified_tags,query,current_answer)
            await ctx.send("Done!")

   

    @commands.Cog.listener()
    async def on_command_error(self, ctx: commands.Context, error: commands.CommandError):
        """A global error handler cog."""

        if isinstance(error, commands.CommandNotFound):
            return  # Return because we don't want to show an error for every command not found
        elif isinstance(error, commands.CommandOnCooldown):
            message = f"This command is on cooldown. Please try again after {round(error.retry_after, 1)} seconds."
        elif isinstance(error, commands.MissingPermissions):
            message = "You are missing the required permissions to run this command!"
        elif isinstance(error, commands.UserInputError):
            message = "Something about your input was wrong, please check your input and try again!"
        else:
            message = "Oh no! Something went wrong while running the command!"

        await ctx.send(message, delete_after=5)
        await ctx.message.delete(delay=5)

    
    @commands.Cog.listener()
    async def on_command_error(self, ctx: commands.Context, error: commands.CommandError):
        """A global error handler cog."""

        if isinstance(error, commands.CommandNotFound):
            return  # Return because we don't want to show an error for every command not found
        elif isinstance(error, commands.CommandOnCooldown):
            message = f"This command is on cooldown. Please try again after {round(error.retry_after, 1)} seconds."
        elif isinstance(error, commands.MissingPermissions):
            message = "You are missing the required permissions to run this command!"
        elif isinstance(error, commands.UserInputError):
            message = "Something about your input was wrong, please check your input and try again!"
        else:
            message = "Oh no! Something went wrong while running the command!"

        await ctx.send(message, delete_after=5)
        await ctx.message.delete(delay=5)



def setup(client):
    client.add_cog(Basic(client))
