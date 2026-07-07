import os
import discord
import asyncio
from discord import app_commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("TOKEN")


class MyClient(discord.Client):
    def __init__(self):
        intents = discord.Intents.default()
        intents.message_content = True
        super().__init__(intents=intents)

        self.tree = app_commands.CommandTree(self)
        self.handlers = []

    async def setup_hook(self):
        commands = [ 
            ("commands.setmodchannel", "setmodchannel"),
            ("commands.enc", "enc"),
            ("commands.dec", "dec"),
            ("commands.report", "report"),
            ("commands.speechbubble", "speechbubble"),
            ("commands.setreportchannel", "set_reportchannel"),
        ]

        for module_path, obj_name in commands:
            module = __import__(module_path, fromlist=[obj_name])
            command = getattr(module, obj_name)
            self.tree.add_command(command)

        from commands.ban import handle_message as ban
        from commands.kick import handle_message as kick
        from commands.mute import handle_message as mute
        from commands.delete import handle_message as delete
        from commands.cmds import handle_message as cmds
        from commands.unban import handle_message as unban
        from commands.unmute import handle_message as unmute

        self.handlers = [ban, kick, mute, delete, cmds, unban, unmute]

        guild_id = os.getenv("GUILD_ID")
        if guild_id:
            guild = discord.Object(id=int(guild_id))
            await self.tree.sync(guild=guild)
        else:
            await self.tree.sync()

        asyncio.create_task(self.status_loop())

    async def on_ready(self):
        print(f"Logged in as {self.user}")

    async def status_loop(self):
        await self.wait_until_ready()

        while not self.is_closed():
            await self.change_presence(
                activity=discord.Streaming(
                    name="?cmds for help",
                    url="https://twitch.tv/a"
                )
            )
            await asyncio.sleep(60)

    async def on_message(self, message):
        if message.author.bot:
            return

        for handler in self.handlers:
            try:
                result = handler(self, message)
                if asyncio.iscoroutine(result):
                    await result
            except Exception as e:
                print(f"[HANDLER ERROR] {handler.__name__}: {e}")


client = MyClient()
client.run(TOKEN)
