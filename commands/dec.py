from discord import app_commands
from utils.crypto import decrypt_message

@app_commands.command(name="dec", description="Decrypt a base64 string")
@app_commands.describe(
    password="Password",
    salt="Salt",
    ciphertext="Encrypted message"
)
async def dec(interaction, password: str, salt: str, ciphertext: str):

    await interaction.response.defer(ephemeral=True)

    try:
        result = decrypt_message(password, salt, ciphertext)

        await interaction.followup.send(
            f"Decrypted:\n{result}",
            ephemeral=True
        )

    except Exception:
        await interaction.followup.send(
            "Decryption failed",
            ephemeral=True
        )