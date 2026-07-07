import discord
from discord import app_commands
from utils.experiments import EXPERIMENTS
from utils.reportconfig import get_channel


class ReportModal(discord.ui.Modal, title="Report Issue"):

    q1 = discord.ui.TextInput(
        label="What is your Discord ID",
        required=True
    )

    q2 = discord.ui.TextInput(
        label="Main subject of the issue",
        style=discord.TextStyle.paragraph,
        required=True
    )

    q3 = discord.ui.TextInput(
        label="Describe details",
        required=True
    )

    q4 = discord.ui.TextInput(
        label="Extra info? (You can skip)",
        style=discord.TextStyle.paragraph,
        required=False
    )

    q5 = discord.ui.TextInput(
        label="**DISCLAIMER:** TROLLING = BLACKLIST",
        required=False
    )

    async def on_submit(self, interaction: discord.Interaction):

        report_channel_id = get_channel()

        if not report_channel_id:
            await interaction.response.send_message(
                "Report channel has not been configured.",
                ephemeral=True
            )
            return

        channel = interaction.client.get_channel(report_channel_id)

        if channel is None:
            await interaction.response.send_message(
                "Configured report channel could not be found.",
                ephemeral=True
            )
            return

        embed = discord.Embed(
            title="Report",
            color=discord.Color.red()
        )

        embed.add_field(
            name="User ID",
            value=self.q1.value,
            inline=False
        )

        embed.add_field(
            name="Main subject",
            value=self.q2.value,
            inline=False
        )

        embed.add_field(
            name="Details",
            value=self.q3.value,
            inline=False
        )

        embed.add_field(
            name="Extra info",
            value=self.q4.value or "None",
            inline=False
        )

        embed.add_field(
            name="Disclaimer was seen",
            value=self.q5.value or "None",
            inline=False
        )

        embed.set_footer(text=f"Reporter: {interaction.user}")

        await channel.send(embed=embed)

        await interaction.response.send_message(
            "Report submitted.",
            ephemeral=True
        )


@app_commands.command(
    name="report",
    description="Report an issue for mods"
)
async def report(interaction: discord.Interaction):

    if not EXPERIMENTS.get("report", False):
        await interaction.response.send_message(
            "Report system is disabled.",
            ephemeral=True
        )
        return

    await interaction.response.send_modal(ReportModal())
