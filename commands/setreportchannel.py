import discord
from discord import app_commands
from utils.reportconfig import save_channel


@app_commands.command(
    name="set-reportchannel",
    description="Set the channel where reports are sent"
)
@app_commands.checks.has_permissions(administrator=True)
async def set_reportchannel(
    interaction: discord.Interaction,
    channel: discord.TextChannel
):

    save_channel(channel.id)

    await interaction.response.send_message(
        f"Report channel set to {channel.mention}",
        ephemeral=True
    )