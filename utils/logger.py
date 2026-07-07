import discord
from utils.modconfig import get_modchannel

async def log_action(client, guild, title, description, color=discord.Color.red()):

    channel_id = get_modchannel(guild.id)
    if not channel_id:
        return

    channel = guild.get_channel(int(channel_id))
    if not channel:
        return

    embed = discord.Embed(
        title=title,
        description=description,
        color=color
    )

    embed.set_footer(text=f"Guild: {guild.name}")

    await channel.send(embed=embed)