#from tgpirobot.tgpirobot import TgPiRobot, print_help
from tgpirobot import TgPiRobot, print_help
import sys
import os
from rich.console import Console

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
            bot.update()
            console.theme = None
        else:
            print("Invalid option")
    else:
        print("No option provided")

if __name__ == "__main__":
    main()
