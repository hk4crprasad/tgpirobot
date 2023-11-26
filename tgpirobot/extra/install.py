import subprocess
from time import sleep

def instally(console, required_packages):
    def is_package_installed(package):
        try:
            subprocess.check_output(["pip", "show", package])
            return True
        except subprocess.CalledProcessError:
            return False

    with console.status("[bold green]Checking and installing packages...") as status:
        for package in required_packages:
            sleep(1)
            if not is_package_installed(package):
                try:
                    subprocess.run(["pip", "install", package, "--quiet"])
                    console.log(f"{package} installed")
                except Exception as e:
                    console.log(f"[bold red]Failed to install module {package}: {e}")
            else:
                console.log(f"{package} is already installed")

    console.log("[bold green]All packages checked and installed successfully!")
