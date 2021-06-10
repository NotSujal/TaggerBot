import discord
from discord.ext import commands
import json,asyncio
from assist import *

class TagManager(commands.Cog):
    """
    The following commands are only for Tagmanagers
    """
    def __inti__(self,client):
        self.client = client

        
    @commands.command(aliases=['req'])
    async def requestedtags (self,ctx):
        """
        Know which all tags are requested by users
        """
        with open(requested_tags+".json") as f:
            data = json.load(f)
            response = ''
        for keys in data:
            response += keys + " \r\n"
        if response == "":
            response = "All the requests are satisfied!"
        await ctx.send(response)


    @commands.command(aliases=['delreq'])
    async def delrequests (self,ctx,req):
        """
        Delete the satisfied/useless requests of users
        """
        user = ctx.message.author.id
        if not isTagmanager(user):
            await ctx.send("Yon are not a TagManager to delete a request")
            return
        with open(requested_tags+".json") as f:
            data = json.load(f)
            del data[req]
        with open(requested_tags+".json","w") as f:
            json.dump(data,f,indent=4,sort_keys=True)
        await ctx.send("Done!")





    @commands.command(aliases = ["allgood"])
    async def verify(self,ctx,*,query):
        """
        Verify the unverified tags
        """
        user = ctx.message.author.id
        try:
            all_tagmanagers = getdata(tagmanagers,"list")
            
        except:
            all_tagmanagers = [781767296121176074]
            createdata(tagmanagers,"list")
            await asyncio.sleep(1)
            savedata(tagmanagers,"list",all_tagmanagers)

    

        if not isTagmanager(user):
            await ctx.send("You need to be a TagManager to verify the query ")
            return
        
        response = getdata(unverified_tags,query)

        savedata(verified_tags,query,response)
        await asyncio.sleep(1)
        deletedata(unverified_tags,query)
        await ctx.send(f"The query *{query}* is verified by {ctx.message.author.mention} and is added to verified list")


    @commands.command(aliases = ["atm",'addmanager'])
    async def addtagmanager(self,ctx,newmember: discord.User = None):
        """
        Add tag managers to manipulate tags
        """
        user = ctx.message.author.id
        
        if not isTagmanager(user):
            await ctx.send("You need to be a TagManager to recruit a TagManager")
            return


        newmember = newmember.id
        try:
            current_tagmanagers = getdata(tagmanagers,"list")
        except:
            current_tagmanagers = [781767296121176074]

        if newmember in current_tagmanagers:
            await ctx.send(f"They are already registered as tag managers")
            return
        
        current_tagmanagers.append(newmember)
        await asyncio.sleep(1)
        savedata(tagmanagers,"list",current_tagmanagers)

        await ctx.send(f"Successfully added {newmember} as a TagManager")

    @commands.command(aliases = ["ev"])
    async def editverified(self,ctx,query,edited_answer):
        """
        edit verified tags
        """
        user = ctx.message.author.id
        if not isTagmanager(user):
            await ctx.send("This command can be only used by tagmanagers")
            return

        try:
            current_answer = getdata(verified_tags,query)
        except:
            await ctx.send("This Tag doesn't exist")
            return
        if current_answer != edited_answer:
            current_answer = edited_answer
            await asyncio.sleep(1)
            savedata(verified_tags,query,current_answer)
            await ctx.send("Done!")


def setup(client):
    client.add_cog(TagManager(client))