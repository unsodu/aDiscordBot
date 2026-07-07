import random
import string
from discord import app_commands
from utils.crypto import encrypt_message

def generate_password(length=10):
    chars = string.ascii_letters + string.digits
    return "".join(random.choice(chars) for _ in range(length))


@app_commands.command(name="enc", description="Encrypts a string w/ base 64")
@app_commands.describe(message="Message to encrypt")
async def enc(interaction, message: str):

    await interaction.response.defer(ephemeral=True)

    try:
        password = generate_password()

        salt, token = encrypt_message(message, password)

        await interaction.followup.send(
            f"Encrypted:\n{token}\n\nSalt:\n{salt}\n\nPassword:\n{password}",
            ephemeral=True
        )

    except Exception:
        await interaction.followup.send("Encryption failed", ephemeral=True)