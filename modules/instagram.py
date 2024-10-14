#!/usr/bin/python3
from bs4 import BeautifulSoup
from rich import print as rprint
import random
import requests
import string

class Instagram:
    @staticmethod
    def run_scan(email):
        session = requests.Session()
        url_login = "https://www.instagram.com/accounts/login/"
        url_check = "https://www.instagram.com/api/v1/web/accounts/web_create_ajax/attempt/"

        user_agents = [
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36',
        ]
        headers = {
            'User-Agent': random.choice(user_agents),
            'Accept': 'application/json, text/plain, */*',
            'Accept-Language': 'en-US,en;q=0.5',
            'Origin': 'https://www.instagram.com',
            'DNT': '1',
            'Connection': 'keep-alive',
        }

        try:
            response = session.get(url_login, headers=headers)
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')
                scripts = soup.find_all('script')
                token = None
                for script in scripts:
                    if 'csrf_token' in script.text:
                        token = script.text.split('csrf_token":"')[1].split('"')[0]
                        break

                if not token:
                    rprint("[red]Error:[/red] CSRF token not found in Instagram login page.")
                    return
                
                headers["x-csrftoken"] = token
            else:
                rprint(f"[red][-][/red] Failed to retrieve Instagram login page.")
                return

            data = {
                'email': email,
                'username': ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(8)),
                'first_name': '',
                'opt_into_one_tap': 'false'
            }

            check_response = session.post(url_check, headers=headers, data=data)

            if check_response.status_code == 200:
                check_data = check_response.json()
                print(check_data)
                if 'errors' in check_data:
                    if 'email' in check_data['errors']:
                        if check_data['errors']['email'][0]['code'] == 'email_is_taken':
                            rprint(f"[green][+][/green] [white]Instagram[/white]")
                        elif "email_sharing_limit" in str(check_data["errors"]):
                            rprint(f"[green][+][/green] [white]Instagram[/white]")
                        else:
                             rprint(f"[red][-][/red] [white]Instagram[/white]")
                else:
                     rprint(f"[red][-][/red] [white]Instagram[/white]")
            else:
                rprint(f"[red][-][/red] [white]Instagram: Request failed with status code {check_response.status_code}.[/white]")
        except Exception as e:
            rprint(f"[red][!] Error occurred on Instagram module: [white]{str(e)}[/white][/red]")
