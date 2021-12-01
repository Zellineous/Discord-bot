# bot.py
# This file is intended to be a "getting started" code example for students.
# The code in this file is fully functional.
# Students are free to edit the code in the milestone 3 folder.
# Students are NOT allowed to distribute this code without the express permission of the class instructor
# IMPORTANT: How to set your secret environment variables? read README guidelines.

# imports
import os
import discord
import database as db

# environment variables
token = os.environ['DISCORD_TOKEN']
server = os.environ['DISCORD_GUILD']
#server_id = os.environ['SERVER_ID']  # optional
#channel_id = os.environ['CHANNEL_ID']  # optional

# database connection
# secret keys related to your database must be updated. Otherwise, it won't work
db_conn = db.connect()
# bot events
client = discord.Client()


@client.event
async def on_ready():
    """
    This method triggers with the bot connects to the server
    Note that the sample implementation here only prints the
    welcome message on the IDE console, not on Discord
    :return: VOID
    """
    print("{} has joined the server".format(client.user.name))


@client.event
async def on_message(message):
    """
    This method triggers when a user sends a message in any of your Discord server channels
    :param message: the message from the user. Note that this message is passed automatically by the Discord API
    :return: VOID
    """
    response = None # will save the response from the bot
    if message.author == client.user:
        return # the message was sent by the bot
    if message.type is discord.MessageType.new_member:
        response = "Welcome {}".format(message.author) # a new member joined the server. Welcome him.
    else:
        # A message was send by the user.
        msg = message.content.lower()
        if "milestone3" in msg:
            response = "I am alive. Signed: 'your bot'"
        if "/station" in msg:
            s = msg
            m = s[9:13]
            response = db.q1(m)
        if "/salary employee" in msg:
            w = msg
            o = w[17:21]
            p = w[22:27]
            response = db.q2(o,p)
        if "/trips-routes" in msg:
            s = msg
            y = s[14:17]
            response = db.q3(y)
        if "/passenger" in msg:
            s = msg
            r = s[11:19]
            response = db.q4(r)
        if "/avg-trips" in msg:
            s = msg
            l = s[11:15]
            k = s[16:20]
            response = db.q5(l,k)
        if "/route-less-more" in msg:
            s = msg
            f = s[17:19]
            g = s[20:22]
            response = db.q6(f,g)
        if "/trips-station" in msg:
            s = msg
            d = s[15:16]
            response = db.q7(d)
    if response:
        # bot sends response to the Discord API and the response is show
        # on the channel from your Discord server that triggered this method.
        embed = discord.Embed(description=response)
        await message.channel.send(embed=embed)
        embed = None
        
        
        


try:
    # start the bot and keep the above methods listening for new events
    client.run(token)
except:
    print("Bot is offline because your secret environment variables are not set. Head to the left panel, " +
          "find the lock icon, and set your environment variables. For more details, read the README file in your " +
          "milestone 3 repository")
