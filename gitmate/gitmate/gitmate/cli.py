import typer
from rich.console import Console
from gitmate.git_utils import get_status, auto_commit, get_branch, get_remote, get_last_commit
from gitmate.message_generator import generate_smart_message

app = typer.Typer(help="🤖 GitMate — Your Smart Git Automation CLI Tool")
console = Console()

@app.command()
def status():
    """Show current Git repository status"""
    get_status()

@app.command()
def info():
    """Show repository info"""
    branch = get_branch()
    remote = get_remote()
    last_commit = get_last_commit()

    console.print("[bold cyan]Repository Info:[/bold cyan]")
    console.print(f"📦 Branch: [green]{branch}[/green]")
    console.print(f"🌐 Remote: [yellow]{remote}[/yellow]")
    console.print(f"🧾 Last Commit: [magenta]{last_commit}[/magenta]")

@app.command()
def auto(message: str = typer.Argument(..., help="Commit message")):
    """Add, commit, and push all changes"""
    auto_commit(message)

@app.command()
def smart():
    """Auto generate commit message and push"""
    msg = generate_smart_message()
    if msg == "No changes detected":
        console.print("[yellow]⚠️ No changes to commit[/yellow]")
    else:
        console.print(f"[cyan]🤖 Generated message:[/cyan] [bold green]{msg}[/bold green]")
        auto_commit(msg)

if __name__ == "__main__":
    app()
