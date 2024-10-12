#!/usr/bin/python3
import sys
import time
from rich import print as rprint
from rich.prompt import Prompt
from rich.prompt import Confirm
from pyfiglet import Figlet
from tabulate import tabulate

# ./modules/*
from modules.instagram import Instagram

def main():
    f = Figlet(font='slant')
    print(f.renderText('mailogleit'))

    while True:
        email = Prompt.ask("[blue][*][/blue] [white]Enter an e-mail address to scan[/white]")
        email_confirm = Confirm.ask(f"[green]{email}[/green] is that correct?", default=True, case_sensitive=False)

        if email_confirm:
            break
        else:
            rprint("[red][!][/red] [white]Please enter the email again.[/white]")

    rprint("[bold green]Scanning the e-mail...[/bold green]")

    animation = "|/-\\"
    start_time = time.time()
    while True:
        for i in range(4):
            time.sleep(0.2)
            sys.stdout.write("\r" + animation[i % len(animation)])
            sys.stdout.flush()
        if time.time() - start_time > 10:
            break
    sys.stdout.write("\r")

    print(tabulate([[email]], headers=["E-mail"], tablefmt="grid"))

    Instagram.run_scan(email)

main()