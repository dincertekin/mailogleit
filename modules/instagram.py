#!/usr/bin/python3
from rich import print as rprint
import requests

class Instagram:
    @staticmethod
    def run_scan(email):
        url = f"https://instagram.com/accounts/password_reset/?email={email}"        
        try:
            response = requests.get(url)
            if response.status_code == 200:
                rprint(f"[green][+][/green] [white]Instagram[/white]")
            else:
                rprint(f"[red][-][/red] [white]Instagram[/white]")
        except Exception as e:
            rprint(f"[red]Error occured on Instagram module: [white]{str(e)}[/white][/red]")