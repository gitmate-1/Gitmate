from setuptools import setup, find_packages

setup(
    name="gitmate",
    version="1.0.0",
    author="Your Name",
    description="🤖 Smart Git Automation CLI Tool — Auto commit, push, and manage repos with style!",
    packages=find_packages(),
    install_requires=["typer", "rich"],
    entry_points={
        "console_scripts": [
            "gitmate=gitmate.cli:app",
        ],
    },
    python_requires=">=3.8",
)
