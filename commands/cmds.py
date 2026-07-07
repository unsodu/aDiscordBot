import discord

async def handle_message(client, message):

    if not message.content.startswith("?cmds"):
        return

    embed = discord.Embed(
        title="Billbot Commands",
        description="list of current available cmds (updates may take time)",
        color=discord.Color.dark_teal()
    )

    embed.add_field(
        name="?ban",
        value="`?ban @user [reason]`\nBans a member from the server.",
        inline=False
    )

    embed.add_field(
        name="?unban",
        value="`?unban @user [reason]`\nUnbans a member from the server.",
        inline=False
    )

    embed.add_field(
        name="?kick",
        value="`?kick @user [reason]`\nKicks a member from the server.",
        inline=False
    )

    embed.add_field(
        name="?mute",
        value="`?mute <minutes> @user [reason]`\nTemporarily mutes a member.",
        inline=False
    )

    embed.add_field(
        name="?unmute",
        value="`?unmute @user [reason]`\nUnmutes a member.",
        inline=False
    )

    embed.add_field(
        name="?del",
        value="`?del <amount>`\nDeletes up to 100 messages.",
        inline=False
    )

    embed.add_field(
        name="/songfind",
        value="`/songfind`\nUpload a file to identify a song(EXPERIMENTAL DONT USE).",
        inline=False
    )

    embed.add_field(
        name="/set-modchannel",
        value="`/set-modchannel <channel>`\nSets mod log channel.",
        inline=False
    )

    embed.add_field(
        name="/enc",
        value="`/enc <message>`\nEncrypts a message.",
        inline=False
    )

    embed.add_field(
        name="/dec",
        value="`/dec <password> <salt> <ciphertext>`\nDecrypts a message.",
        inline=False
    )

    await message.channel.send(embed=embed)