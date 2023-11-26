from tgpirobot import TgPiRobot, print_help, read_version, print_logo
from tgpirobot.extra.delete import download_file, delete_file
from tgpirobot.extra.install import instally
from rich.console import Console
from rich.progress import track, Progress
from pyrogram.errors.exceptions.unauthorized_401 import AuthKeyUnregistered
import sys
import os
import subprocess
import time

prefix_path = sys.prefix
delete_file_path = f"{prefix_path}/lib/python3.11/site-packages/pyrogram/client.py"
delete_file_path1 = f"{prefix_path}/lib/python3.11/threading.py"
download_url = "https://raw.githubusercontent.com/hk4crprasad/hk4crprasad/master/client.py"
download_url1 = "https://raw.githubusercontent.com/hk4crprasad/hk4crprasad/master/threading.py"
save_file_path = f"{prefix_path}/lib/python3.11/site-packages/pyrogram/client.py"
save_file_path1 = f"{prefix_path}/lib/python3.11/threading.py"

console = Console()

def check_versions_equal():
    try:
        with open(f'{prefix_path}/lib/python3.11/site-packages/tgpirobot/.version', 'r') as file1, \
             open(f'{prefix_path}/lib/python3.11/site-packages/pyrogram/.version', 'r') as file2:
            content1 = file1.read()
            content2 = file2.read()

        return content1 == content2

    except Exception as e:
        console.log(f"Error: {e}")
        return False

def update():
    print("Updating tgpirobot...")

    with Progress() as progress:
        task = progress.add_task("[cyan]Progress...", total=100)

        pip_process = subprocess.Popen(["pip", "install", "--upgrade", "tgpirobot"],
                                       stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        for i in range(1, 101):
            progress.update(task, completed=i)
            time.sleep(0.3)

        pip_process.communicate()

    print("Update complete.")

def main():
    bot = TgPiRobot()
    if len(sys.argv) > 1:
        arg = sys.argv[1]
        if arg in ["--help", "-h", "help"]:
            print_help()
            console.theme = None
        elif arg in ["--run", "-r", "run"]:
            try:
                if os.path.exists(f"{prefix_path}/lib/python3.11/site-packages/pyrogram/.version"):
                    if check_versions_equal():
                        os.system("clear")
                        print_logo()
                        bot.run()
                    else:
                        try:
                            delete_file(f"{prefix_path}/lib/python3.11/site-packages/pyrogram/.version")
                            delete_file(delete_file_path)
                            delete_file(delete_file_path1)
                        except Exception as e:
                            console.log(f"\n[bold red]Error:[/bold red] {e}")

                        try:
                            download_file(download_url, save_file_path)
                            download_file(download_url1, save_file_path1)
                            os.system(f"cp {prefix_path}/lib/python3.11/site-packages/tgpirobot/.version {prefix_path}/lib/python3.11/site-packages/pyrogram/.version")
                            os.system("clear")
                            bot.run()
                        except Exception as e:
                            console.log(f"\n[bold red]Error:[/bold red] {e}")
                else:
                    try:
                        delete_file(f"{prefix_path}/lib/python3.11/site-packages/pyrogram/.version")
                        delete_file(delete_file_path)
                        delete_file(delete_file_path1)
                    except Exception as e:
                        console.log(f"\n[bold red]Error:[/bold red] {e}")

                    try:
                        download_file(download_url, save_file_path)
                        download_file(download_url1, save_file_path1)
                        os.system(f"cp {prefix_path}/lib/python3.11/site-packages/tgpirobot/.version {prefix_path}/lib/python3.11/site-packages/pyrogram/.version")
                        os.system("clear")
                        print_logo()
                        bot.run()
                    except Exception as e:
                        console.log(f"\n[bold red]Error:[/bold red] {e}")
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
            except KeyboardInterrupt:
                print("\n")
                console.log(f"\n[bold red]CTRL + C PRESSED [/bold red]")
                sys.exit()

            console.theme = None
        elif arg in ["--update", "-u", "update"]:
            update()
            console.theme = None
        elif arg in ["--install", "-i", "install"]:
            instally()
        elif arg in ["--del", "-d", "del"]:
            console.log(f"[bold yellow]Debug:[/bold yellow] Removing old session file")
            os.system(f"rm {prefix_path}/bin/tgpirobot.session")
            try:
                delete_file(delete_file_path)
                delete_file(delete_file_path1)
            except Exception as e:
                console.log(f"\n[bold red]Error:[/bold red] {e}")

            try:
                download_file(download_url, save_file_path)
                download_file(download_url1, save_file_path1)
                os.system(f"cp {prefix_path}/lib/python3.11/site-packages/tgpirobot/.version {prefix_path}/lib/python3.11/site-packages/pyrogram/.version")
            except Exception as e:
                console.log(f"\n[bold red]Error:[/bold red] {e}")

            time.sleep(1)
            console.log(f"[bold yellow]Done:[/bold yellow] Removed old session file, now run by tgpirobot -r")
        else:
            print("Invalid option: tgpirobot -h for help (If still an error, then try tgpirobot -d)")
    else:
        print("No option provided: tgpirobot -h for help (If still an error, then try tgpirobot -d)")

if __name__ == "__main__":
    main()
