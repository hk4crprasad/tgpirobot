from rich.progress import track, Progress
import subprocess
import os
import time
import requests
from rich.console import Console
console = Console()
def delete_file(file_path):
    if os.path.exists(file_path):
        os.remove(file_path)
        console.log(f"[bold yellow]Deleted File:[/bold yellow] {file_path}")
    else:
        console.log(f"[bold yellow]File not found:[/bold yellow] {file_path}")

def download_file(url, save_path):
    response = requests.get(url, stream=True)
    total_size = int(response.headers.get('content-length', 0))
    
    with Progress() as progress:
        task = progress.add_task("[cyan]Downloading...", total=total_size)
        
        with open(save_path, 'wb') as file:
            for chunk in response.iter_content(chunk_size=1024):
                file.write(chunk)
                progress.update(task, completed=len(chunk))
    
    print(f"\n")
    console.log(f"[bold yellow]Debug:[/bold yellow] Download complete")
