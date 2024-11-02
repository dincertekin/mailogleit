#!/usr/bin/python3
from rich import print as rprint
import re
import requests

class Github:
    @staticmethod
    def run_scan(email):
        session = requests.Session()
        
        url_login = "https://github.com/join"
        url_check = "https://github.com/signup_check/email"

        token_regex = re.compile(
            r'<input[^>]+name="authenticity_token"[^>]+value="([^"]+)"'
        )
        
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36',
            'Accept': 'application/json, text/plain, */*',
            'Accept-Language': 'en-US,en;q=0.5',
            'Origin': 'https://github.com',
            'DNT': '1',
            'Connection': 'keep-alive',
        }

        response = session.get(url_login, headers=headers)
        if response.status_code != 200:
            return rprint(f"[red]GitHub:[/red] Failed to retrieve join page!")

        match = token_regex.search(response.text)
        if not match:
            return rprint(f"[red]GitHub:[/red] CSRF token not found!")

        email_token = match.group(1)

        data = {
            "value": email,
            "authenticity_token": email_token,
        }
        check_response = session.post(url_check, data=data)

        if check_response.status_code == 422:
            return rprint(f"[green][+][/green] [white]GitHub[/white]")
        elif check_response.status_code == 200:
            return rprint(f"[red][-][/red] [white]GitHub[/white]")
        elif check_response.status_code == 429:
            return rprint(f"[red]GitHub:[/red] Too many requests.")
        else:
            return rprint(f"[red]GitHub:[/red] Request failed with status code {check_response.status_code}.")
