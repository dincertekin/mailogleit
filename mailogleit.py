from rich import print as rprint
from rich.prompt import Confirm
from rich.prompt import Prompt
from tabulate import tabulate
import sys
import time
from pyfiglet import Figlet

# ./modules/*
from modules.instagram import Instagram
from modules.snapchat import Snapchat
from modules.spotify import Spotify

def main():
    f = Figlet(font='slant')
    print(f.renderText('mailogleit'))

    while True:
        email = Prompt.ask("[blue][*][/blue] [white]Enter an e-mail address to scan[/white]")
        email_confirm = Prompt.ask(f"[green]{email}[/green] is that correct? (y/n)", default="y")

        if email_confirm.lower() in ["y", "yes"]:
            break
        else:
            rprint("[red][!][/red] [white]Please enter the email again.[/white]")

    rprint("[bold green]Scanning the e-mail...[/bold green]")

    # Scan the email with Instagram
    instagram_result = Instagram.run_scan(email)
    rprint(f"[bold blue]Instagram:[/bold blue] {instagram_result}")

    # Scan the email with Snapchat
    snapchat_result = Snapchat.run_scan(email)
    rprint(f"[bold blue]Snapchat:[/bold blue] {snapchat_result}")

    # Scan the email with Spotify
    spotify_result = Spotify.run_scan(email)
    rprint(f"[bold blue]Spotify:[/bold blue] {spotify_result}")

if __name__ == "__main__":
    main()