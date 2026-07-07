import discord
from utils.logger import log_action

async def handle_message(client, message):

    if not message.content.startswith("?unban"):
        return

    if not message.guild:
        return

    if not message.author.guild_permissions.ban_members:
        return await message.channel.send("Need elevated permissions")

    parts = message.content.split(" ", 2)

    if len(parts) < 2:
        return await message.channel.send(
            "Proper usage: ?unban <user_id> [reason]"
        )

    try:
        user_id = int(parts[1])
    except ValueError:
        return await message.channel.send(
            "Proper usage: ?unban <user_id> [reason]"
        )

    reason = parts[2] if len(parts) > 2 else "No reason"

    try:
        user = await client.fetch_user(user_id)

        await message.guild.unban(user, reason=reason)

        await message.channel.send(f"Unbanned {user}")

        await log_action(
            client,
            message.guild,
            "**__UNBAN__**",
            f"**user:** {user.mention}\n"
            f"**moderator:** {message.author.mention}\n"
            f"**reason:** {reason}",
            discord.Color.og_blurple()
        )

    except Exception as e:
        print("UNBAN ERROR:", e)
        await message.channel.send("Unban failed")