#from tgpirobot.tgpirobot import TgPiRobot, print_help
from tgpirobot.tgpirobot import TgPiRobot, print_help, instally
import sys
import os
from rich.console import Console
from rich.progress import track, Progress
import subprocess

def update():
    print("Updating tgpirobot...")

    with Progress() as progress:
        task = progress.add_task("[cyan]Progress...", total=100)

        pip_process = subprocess.Popen(["pip", "install", "--upgrade", "tgpirobot"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        for i in range(1, 101):
            progress.update(task, completed=i)
            time.sleep(0.3)

        pip_process.communicate()

    print("Update complete.")
    
console = Console()

def main():
    bot = TgPiRobot()
    if len(sys.argv) > 1:
        arg = sys.argv[1]
        if arg in ["--help", "-h", "help"]:
            print_help()
            console.theme = None
        elif arg in ["--run", "-r", "run"]:
            bot.run()
            console.theme = None
        elif arg in ["--update", "-u", "update"]:
            update()
            console.theme = None
        elif arg in ["--install", "-i", "install"]:
            instally()
        else:
            print("Invalid option : tgpirobot -h for help")
    else:
        print("No option provided : tgpirobot -h for help")

if __name__ == "__main__":
    main()
