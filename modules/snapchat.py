#!/usr/bin/python3
from rich import print as rprint
import random
import requests

class Snapchat:
    @staticmethod
    def run_scan(email):
        rprint("[red][!][/red] Snapchat: [white]Work in progress...[/white]")
        """
        session = requests.Session()
        url = "https://bitmoji.api.snapchat.com/api/user/find"

        user_agents = [
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36',
        ]
        headers = {
            'User-Agent': random.choice(user_agents)
        }

        data = {
            'email': email
        }

        try:
            response = session.post(url, headers=headers, json=data)

            if '{"account_type":"snapchat"}' in response.text:
                rprint(f"[green][+][/green] [white]Snapchat[/white]")

            else:
                rprint(f"[red][-][/red] [white]Snapchat[/white]")

        except Exception as e:
            rprint(f"[red][!] Error occurred on Snapchat module: [white]{str(e)}[/white][/red]")
        """