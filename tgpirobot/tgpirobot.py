import subprocess
from time import sleep
from rich.console import Console

console = Console()

install_requires = [
    'python-dotenv',
    'pyrogram-repl',
    'python-telegram-bot',
    'requests',
    'pyfiglet',
    'tqdm',
    'setuptools',
    'inquirer',
    'rich',
    'aiohttp'
]

def is_package_installed(package):
    try:
        subprocess.check_output(["pip", "show", package])
        return True
    except subprocess.CalledProcessError:
        return False

with console.status("[bold green]Checking and installing packages...") as status:
    for package in install_requires:
        sleep(1)
        if not is_package_installed(package):
            subprocess.run(["pip", "install", package, "--quiet"])
            console.log(f"{package} installed")

console.log("[bold green]All packages checked and installed successfully!")

import sys
import os
import time
import asyncio
import random
import subprocess
from datetime import datetime
import json
import aiohttp
from pyrogram import Client, filters
from pyfiglet import figlet_format
from rich.progress import track, Progress
from pkgutil import get_data
from pathlib import Path
from rich.table import Table
from rich.syntax import Syntax
from rich.theme import Theme
from rich import pretty
from rich.traceback import install
from rich.markdown import Markdown

install(show_locals=True)

pretty.install()
def read_resource(path):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, path)
    try:
        with open(file_path, 'rb') as file:
            data = file.read()
            return data.decode() if data else ""
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return ""
        
def quizzes():
    quiz = read_resource("quizzes.json")
    return json.loads(quiz)
    
def markd():
    markdown = read_resource("README.md")
    return Markdown(markdown)
    
def read_version():
    return read_resource(".version").strip()

# Example usage
VERSION = read_version()
MARKDOWNS = markd()
CONFIG_FILE = "config.json"
FLOOD_LIMIT = 10  
FLOOD_DURATION = 60

table = Table(show_header=False)
xterm_theme = Theme({
    "background": "#1c1c1c",  # Replace with your desired background color
    "text": "#dcdccc",        # Replace with your desired text color
    # Add more styles as needed
})
console.theme = xterm_theme

class TgPiRobot:

    def __init__(self):
        self.api_id = None
        self.api_hash = None
        self.token = None
        self.debug = False
        self.sender_list = {}
        self.blocked_users = set()
        self.load_config()
        self.app = Client("tgpirobot", api_id=self.api_id, api_hash=self.api_hash)

    def load_config(self):
        if not os.path.exists(CONFIG_FILE):
            self.create_config()
        else:
            with open(CONFIG_FILE) as f:
                config = json.load(f)
            self.api_id = config["api_id"]
            self.api_hash = config["api_hash"]
            self.token = config["token"]
            self.debug = config["debug"]

    def create_config(self):
        console.print("Welcome to tgpirobot configuration", style="bold red")
        
        self.api_id = console.input("Enter API ID :- ")
        self.api_hash = console.input("Enter API Hash :- ")
        self.token = console.input("Enter Bot Token :- ") 
        self.debug = console.input("Debug (y/n) :- ") == "y"

        config = {
            "api_id": self.api_id,
            "api_hash": self.api_hash,
            "token": self.token,
            "debug": self.debug
        }

        with open(CONFIG_FILE, "w") as f:
            json.dump(config, f, indent=4)

        console.print("Config saved to config.json", style="bold green")

    async def handle_new_message(self, client, message):
        try:
            me = await self.app.get_me()
        except Exception:
            console.print_exception(show_locals=True)
            return

        if message.from_user.is_bot or message.from_user.id == me.id:
            return

        user_id = message.from_user.id
        username = message.from_user.username

        if user_id in self.blocked_users:
            await message.reply("You are blocked for flood")
            return

        self.sender_list.setdefault(user_id, 0) 
        self.sender_list[user_id] += 1

        flood_left = FLOOD_LIMIT - self.sender_list[user_id]

        if flood_left <= 0:
            self.blocked_users.add(user_id)
            self.sender_list.pop(user_id)
            await message.reply("You are blocked for flood")
            await client.block_user(user_id)
            await asyncio.sleep(FLOOD_DURATION)
            await client.unblock_user(user_id) 
            self.blocked_users.remove(user_id)

        auto_reply = ""
        if self.sender_list[user_id] == 1:
            auto_reply = self._get_offline_reply(username)
        elif 1 < self.sender_list[user_id] < 4:
            auto_reply = self._get_wait_reply(username)
        else:
            auto_reply = self._get_quiz(username)

        if auto_reply:
            auto_reply += f"\nFlood attempts left: {flood_left}"
            await message.reply(auto_reply, quote=True)

        date = message.date.strftime("%a %b %d %H:%M:%S %Y")
        text = (
                f"User%20name%20%3A-%20@{username if username else 'None'}%0AUser%20id%20%3A-%20{user_id}%0ADate%20%3A-%20{date}%0AMessage%20%3A-%20{message.text.replace(' ', '%20') if message.text else ''}"
            )
        table = Table(show_header=False)
        await self._send_log(text, me)
        table.add_column("Attribute", style="bold red", no_wrap=True)
        table.add_column("Value", style="green")
        
        table.add_row("User name", f"@{username}")
        table.add_row("User ID", f"{user_id}")
        table.add_row("Date", message.date.strftime("%a %b %d %H:%M:%S %Y"))
        table.add_row("Message", f"{message.text if message.text else ''}")
        
        console.print(table)

    
    def _get_offline_reply(self, username):
        return (
            f"Hi @{username},\nI'm offline right now. "
            "Please check back later!\nFeel free to browse https://github.com/hk4crprasad"
        )

    def _get_wait_reply(self, username):
        replies = [
            f"Please be patient @{username}, I'm still offline!",
            f"Please bear with me @{username}!",
        ]
        return random.choice(replies)

    def _get_quiz(self, username):
        quizzes_data = quizzes()
        q = random.choice(quizzes_data)
        return (
            f"How about a quiz @{username}?\n\n"
            f"{q['question']}\n{q['answer']}"
        )
   
    async def _send_log(self, text, me):
        url = f"https://api.telegram.org/bot{self.token}/sendMessage?chat_id={me.id}&text={text}"
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as resp:
                return await resp.text()

    def run(self):
        @self.app.on_message(filters.private & ~filters.bot)
        async def _(client, message):
            await self.handle_new_message(client, message)
            
        self.app.run()
       
    def update(self):
        print("Updating tgpirobot...")
    
        with Progress() as progress:
            task = progress.add_task("[cyan]Progress...", total=100)
    
            pip_process = subprocess.Popen(["pip", "install", "--upgrade", "tgpirobot"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    
            for i in range(1, 101):
                progress.update(task, completed=i)
                time.sleep(0.3)  
                
            pip_process.communicate()
    
        print("Update complete.")
        
def print_logo():
    piroh = figlet_format("TgPiRobot")
    raam = f"Version: {VERSION}\n"
    piroo = Syntax(piroh, "python", theme="monokai")
    radhe = Syntax(raam, "python", theme="monokai")
    console.print(piroo)
    console.print(radhe)

def print_help():
    print_logo()
    console.print(MARKDOWNS)