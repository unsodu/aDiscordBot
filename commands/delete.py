import discord
from utils.logger import log_action

async def handle_message(client, message):

    if not message.content.startswith("?del"):
        return

    if not message.guild:
        return

    if not message.author.guild_permissions.manage_messages:
        return await message.channel.send("Need elevated permissions")

    parts = message.content.split(" ", 1)

    if len(parts) < 2:
        return await message.channel.send(
            "Proper usage: ?del <amount>"
        )

    try:
        amount = int(parts[1])
    except ValueError:
        return await message.channel.send(
            "Proper usage: ?del <amount>"
        )

    if amount <= 0 or amount > 100:
        return await message.channel.send(
            "Amount must be between 1 and 100"
        )

    try:
        deleted = await message.channel.purge(limit=amount + 1)

        await message.channel.send(
            f"Deleted {len(deleted) - 1} messages",
            delete_after=3
        )

        await log_action(
            client,
            message.guild,
            "**__MESSAGES DELETED__**",
            f"**moderator:** {message.author.mention}\n"
            f"**amount:** {amount}",
            discord.Color.brand_red()
        )

    except Exception as e:
        print("DELETE ERROR:", e)
        await message.channel.send("Delete failed")