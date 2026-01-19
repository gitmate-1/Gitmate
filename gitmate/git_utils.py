import subprocess
from rich.console import Console

console = Console()

def run_command(cmd: list, show_output: bool = True):
    """Safely run shell commands"""
    try:
        result = subprocess.run(cmd, check=True, capture_output=True, text=True)
        if show_output and result.stdout.strip():
            console.print(result.stdout.strip(), style="green")
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        console.print(f"[red]Error:[/red] {e.stderr.strip() if e.stderr else e}")
        return None

def get_status():
    console.print("[bold cyan]Checking repository status...[/bold cyan]")
    run_command(["git", "status"])

def get_branch():
    return run_command(["git", "rev-parse", "--abbrev-ref", "HEAD"], show_output=False)

def get_remote():
    return run_command(["git", "config", "--get", "remote.origin.url"], show_output=False)

def auto_commit(message: str):
    console.print("[yellow]Staging changes...[/yellow]")
    run_command(["git", "add", "."])

    console.print(f"[cyan]Committing: {message}[/cyan]")
    run_command(["git", "commit", "-m", message])

    console.print("[blue]Pushing to remote...[/blue]")
    run_command(["git", "push"])
    console.print("[green bold]✅ All changes committed and pushed successfully![/green bold]")

def get_last_commit():
    return run_command(["git", "log", "-1", "--pretty=%B"], show_output=False)
