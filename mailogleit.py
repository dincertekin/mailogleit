from rich import print as rprint
from rich.prompt import Prompt
from rich.prompt import Confirm
from pyfiglet import Figlet

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

    rprint("[bold green]Scanning the email...[/bold green]")

main()