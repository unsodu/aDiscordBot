import discord
from discord import app_commands
from utils.modconfig import set_modchannel

@app_commands.command(
    name="set-modchannel",
    description="Set moderation log channel"
)
@app_commands.describe(channel="Channel to send logs to")
async def setmodchannel(interaction: discord.Interaction, channel: discord.TextChannel):

    if not interaction.guild:
        return await interaction.response.send_message(
            "This command can only be used in a server",
            ephemeral=True
        )

    if not interaction.user.guild_permissions.administrator:
        return await interaction.response.send_message(
            "Need elevated permissions",
            ephemeral=True
        )

    set_modchannel(interaction.guild.id, channel.id)

    await interaction.response.send_message(
        f"Mod channel set to {channel.mention}",
        ephemeral=True
    )