import discord
from utils.logger import log_action

async def handle_message(client, message):

    if not message.content.startswith("?ban"):
        return

    if not message.guild:
        return

    if not message.author.guild_permissions.ban_members:
        return await message.channel.send("Need elevated permissions")

    parts = message.content.split(" ", 2)

    if len(parts) < 2 or not message.mentions:
        return await message.channel.send(
            "Proper usage: ?ban <@member> [reason]"
        )

    member = message.mentions[0]

    if member.top_role >= message.author.top_role:
        return await message.channel.send("Cannot moderate this user")

    if member.top_role >= message.guild.me.top_role:
        return await message.channel.send("Cannot moderate this user")

    reason = parts[2] if len(parts) > 2 else "No reason"

    try:
        await member.ban(reason=reason)

        await message.channel.send(f"Banned {member}")

        await log_action(
            client,
            message.guild,
            "**__BAN__**",
            f"**user:** {member.mention}\n"
            f"**moderator:** {message.author.mention}\n"
            f"**reason:** {reason}",
            discord.Color.dark_red()
        )

    except Exception as e:
        print("BAN ERROR:", e)
        await message.channel.send("Ban failed")