#from tgpirobot.tgpirobot import TgPiRobot, print_help
from tgpirobot import TgPiRobot, print_help, instally
import sys
import os
from rich.console import Console
from rich.progress import track, Progress
import subprocess
from pyrogram.errors.exceptions.unauthorized_401 import AuthKeyUnregistered
try:
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
                try:
                    bot.run()
                except ImportError as e:
                    print("")
                    console.log(f"\n[bold red]Error:[/bold red] {e}")
                    console.log("[bold red]Run[/bold red] [bold green]tgpirobot -d[/bold green][bold red] and then[/bold red] [bold green]tgpirobot -r[/bold green]")
                except Exception as e:
                    print("")
                    console.log(f"\n[bold red]Error:[/bold red] {e}")
                    console.log("[bold red]Run[/bold red] [bold green]tgpirobot -d[/bold green][bold red] and then[/bold red] [bold green]tgpirobot -r[/bold green]")
                except AuthKeyUnregistered as e:
                    print("")
                    console.log(f"\n[bold red]Error:[/bold red] {e}")
                    console.log("[bold red]Run[/bold red] [bold green]tgpirobot -d[/bold green][bold red] and then[/bold red] [bold green]tgpirobot -r[/bold green]")
                except OperationalError as e:
                    pirint("")
                    console.log(f"\n[bold red]Error:[/bold red] {e}")
                    console.log("[bold red]Run[/bold red] [bold green]tgpirobot -d[/bold green][bold red] and then[/bold red] [bold green]tgpirobot -r[/bold green]")

                console.theme = None
            elif arg in ["--update", "-u", "update"]:
                update()
                console.theme = None
            elif arg in ["--install", "-i", "install"]:
                instally()
            elif arg in ["--del", "-d", "del"]:
                console.log(f"[bold yellow]Debug:[/bold yellow] Removing old session file")
                os.system("rm $PREFIX/bin/tgpirobot.session")               
                time.sleep(1)
                console.log(f"[bold yellow]Done:[/bold yellow] Removed old session file, now run by tgpirobot -r")
            else:
                print("Invalid option : tgpirobot -h for help (If still error then try tgpirobot -d)")
        else:
            print("No option provided : tgpirobot -h for help (If still error then try tgpirobot -d)")
    
    if __name__ == "__main__":
        main()
except ImportError as e:
    console.log(f"[bold red]Error:[/bold red] {e}")
    console.log("[bold red]Run[/bold red] [bold green]tgpirobot -d[/bold green][bold red] and then[/bold red] [bold green]tgpirobot -r[/bold green]")
except Exception as e:
    console.log(f"[bold red]Error:[/bold red] {e}")
    console.log("[bold red]Run[/bold red] [bold green]tgpirobot -d[/bold green][bold red] and then[/bold red] [bold green]tgpirobot -r[/bold green]")
except AuthKeyUnregistered as e:
    console.log(f"[bold red]Error:[/bold red] {e}")
    console.log("[bold red]Run[/bold red] [bold green]tgpirobot -d[/bold green][bold red] and then[/bold red] [bold green]tgpirobot -r[/bold green]")
except OperationalError as e:
    console.log(f"[bold red]Error:[/bold red] {e}")
    console.log("[bold red]Run[/bold red] [bold green]tgpirobot -d[/bold green][bold red] and then[/bold red] [bold green]tgpirobot -r[/bold green]")
