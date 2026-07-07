import discord
from datetime import timedelta
from utils.logger import log_action

async def handle_message(client, message):

    if not message.content.startswith("?mute"):
        return

    if not message.guild:
        return

    if not message.author.guild_permissions.moderate_members:
        return await message.channel.send("Need elevated permissions")

    parts = message.content.split(" ", 3)

    if len(parts) < 3 or not message.mentions:
        return await message.channel.send(
            "Proper usage: ?mute <minutes> <@member> [reason]"
        )

    try:
        minutes = int(parts[1])
    except ValueError:
        return await message.channel.send(
            "Proper usage: ?mute <minutes> <@member> [reason]"
        )

    if minutes <= 0 or minutes > 40320:
        return await message.channel.send(
            "Mute time must be between 1 and 40320 minutes"
        )

    member = message.mentions[0]

    if member.top_role >= message.author.top_role:
        return await message.channel.send("Cannot moderate this user")

    if member.top_role >= message.guild.me.top_role:
        return await message.channel.send("Cannot moderate this user")

    reason = parts[3] if len(parts) > 3 else "No reason"

    try:
        until = discord.utils.utcnow() + timedelta(minutes=minutes)

        await member.timeout(until, reason=reason)

        await message.channel.send(f"Muted {member}")

        await log_action(
            client,
            message.guild,
            "**__MUTE__**",
            f"**user:** {member.mention}\n"
            f"**moderator:** {message.author.mention}\n"
            f"**reason:** {reason}",
            discord.Color.yellow()
        )

    except Exception as e:
        print("MUTE ERROR:", e)
        await message.channel.send("Mute failed")