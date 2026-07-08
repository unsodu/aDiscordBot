    Copyright (C) 2026 unsodu

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.

# bot

made by "cedarist." on discord.
sharing is caring as they say. This is my bot and its source code. itd be helpful to share with you my helpful tools and moderation bot.
so yeah and stuff dont breach license agreement ig.
id appreciate any forks and bug reports ))

# installation

## requirements

python 3.11 or more

git

a discord bot(ofc)

### to install both

windows:

    winget install --id Git.Git --source winget
    winget install --id Python.Python.3.14 --source winget

linux(debian):

    sudo apt update
    sudo apt install git python3 python3-pip

linux(arch):

    sudo pacman -S git python3 python3-pip

Termux:

    pkg update
    pkg upgrade
    pkg install git python

## dependancies and repo

first, in any platform do

```bash
git clone https://github.com/unsodu/aDiscordBot.git
cd aDiscordBot
```
then:

    pip install -r requirements.txt

or just copy the contents of the text and install.

### external dependencies

these are required for external proccessing i.e in your host server, such as your pc.

cmd/powershell:
```cmd/PowerShell
winget install --id ImageMagick.ImageMagick --source winget
```

Debian:
```debian
sudo apt install imagemagick
```
arch:
```arch
sudo pacman -S imagemagick
```
termux:
```Termux
pkg install imagemagick
```

## configure

if youre on windows:

    notepad .env
 
or linux:

    nano .env

paste:

    TOKEN=YOURBOT_TOKEN

(replace YOURBOT_TOKEN with your bot token; you can find it in discord developer portal on your web browser)

congrats, now you have the bot.

###### to run it:

    python bot.py

(or whatever you renamed the file to)

now you have that bot running, it should say:

logged in as {bot_name#0000}

# commands

its still under construction, and the current existing commands and be found in ?cmds file, which you can update if you make your own ones