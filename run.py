# run.py
import os
import sys
from rich import print
from prompt_toolkit import prompt
from pyfiglet import figlet_format

def main():
    banner = figlet_format("HyexzFrameWork", font="slant")
    print(f"[bold green]{banner}[/bold green]")
    print("[cyan]Welcome to HyexzFrameWork by Hyezzcraxksz[/cyan]")

    try:
        while True:
            cmd = prompt("hyexz > ")
            if cmd in ["exit", "quit"]:
                print("[red]Exiting...[/red]")
                break
            elif cmd.startswith("use "):
                print(f"[yellow]Module selected: {cmd[4:]}[/yellow]")
            elif cmd == "help":
                print("[blue]Available commands: use, help, exit[/blue]")
            else:
                print(f"[red]Unknown command:[/red] {cmd}")
    except KeyboardInterrupt:
        print("\n[red]Interrupted by user.[/red]")

if __name__ == "__main__":
    main()
