#!/usr/bin/python3
from rich import print as rprint
import random
import requests

class Spotify:
    @staticmethod
    def run_scan(email):
        url = f"https://spclient.wg.spotify.com/signup/public/v1/account?validate=1&email={email}"

        headers = {
            "User-Agent": "Mozilla/5.0 (Linux; Android 10; SM-G960F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.120 Mobile Safari/537.36"
        }

        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()

            data = response.json()

            if data.get("status") == 20:
                rprint("[green][+][/green] [white]Spotify[/white]")
            else:
                rprint("[red][-][/red] [white]Spotify[/white]")

        except requests.RequestException as e:
            rprint(f"[red][!] Error occurred on Spotify module: [white]{str(e)}[/white][/red]")