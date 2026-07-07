import io
from pathlib import Path

import discord
from discord import app_commands
from PIL import Image

BUBBLE_PATH = Path(__file__).resolve().parent.parent / "utils" / "speechbubble.webp"


@app_commands.command(
    name="speechbubble",
    description="Add a speech bubble to an image"
)
@app_commands.describe(
    image="Image to edit",
    togif="Output as GIF instead of PNG"
)
async def speechbubble(
    interaction: discord.Interaction,
    image: discord.Attachment,
    togif: bool = False
):
    await interaction.response.defer()

    data = await image.read()

    img = Image.open(io.BytesIO(data)).convert("RGBA")
    bubble = Image.open(BUBBLE_PATH).convert("RGBA")

    bubble = bubble.resize(
        (
            int(img.width * 1.3),
            int(img.height * 0.55)
        ),
        Image.Resampling.LANCZOS
    )

    x = -(bubble.width - img.width) // 2
    y = 0

    img.alpha_composite(bubble, (x, y))

    output = io.BytesIO()

    if togif:
        img.convert("RGB").save(output, format="GIF")
        filename = "speechbubble.gif"
    else:
        img.save(output, format="PNG")
        filename = "speechbubble.png"

    output.seek(0)

    await interaction.followup.send(
        file=discord.File(output, filename)
    )