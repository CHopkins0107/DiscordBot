import discord
import config
from collections import namedtuple
from serverinfo import ServerInfo # server, role_id, channels


client = discord.Client()
server_db = {}

@client.event
async def on_ready():
    for guild in client.guilds:
        # channels = [channel.name for channel in guild.text_channels]
        channel_dict = {i.id:i.name for i in guild.channels if (i.name != 'Voice Channels' and i.name != 'Text Channels')}
        server_obj = ServerInfo(server=guild.name, channels=guild.channels)
        server_db[guild.id] = server_obj
    print("Bot successfully initiated")
    print()
    print(guild.channels)
    print(channel_dict)


@client.event
async def on_raw_reaction_add(payload):
    if payload.message_id == server_db[payload.guild_id].getID():
        server_id = payload.guild_id
        server = discord.utils.find(lambda s : s.id == server_id, client.guilds)
        role = discord.utils.find(lambda r : r.name == payload.emoji.name, server.roles)
        print(payload.emoji.name, server.roles)

        if role is not None:
            print("Valid Role -- adding user to role")
            print(role.id)

            user = discord.utils.find(lambda u : u.id == payload.user_id, server.members)
            await user.add_roles(role)
            print(f"Operation successful: {user} added to {role}!")

        else:
            print(role)


@client.event
async def on_raw_reaction_remove(payload):
    if payload.message_id == server_db[payload.guild_id].getID():
        server_id = payload.guild_id
        server = discord.utils.find(lambda s: s.id == server_id, client.guilds)
        role = discord.utils.find(lambda r: r.name == payload.emoji.name, server.roles)

        if role is not None:
            print("Valid Role -- removing user from role")
            print(role.id)
            user = discord.utils.find(lambda u : u.id == payload.user_id, server.members)
            await user.remove_roles(role)
            print(f"Operation successful: {user} removed from {role}!")


@client.event
async def on_message(message):
    message.content = message.content.lower()

    if message.content.startswith('.setup'):
        message_list = message.content.split()
        temp = message_list[1]
        try:
            temp = int(temp)
        except TypeError:
            await message.channel.send("Error: Invalid Message ID")
        except:
            await message.channel.send("Unknown error has occured")
        server_db[message.guild.id].setID(temp)
        await message.channel.send("Successfully set reaction message!")

    if message.content.startswith('.queue'):
        message_list = message.content.split()
        game = message_list[1]
        if message_list.length() == 3:
            party_size = message_list[2]
        else:
            party_size = 5





client.run(config.secret)