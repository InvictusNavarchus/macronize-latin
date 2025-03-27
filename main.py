#!/usr/bin/env python3

import argparse
import pyperclip
from submit_form import submit_form
from parse_html import parse_html
from rich.console import Console
from rich.panel import Panel

def main():
    # Create a parser object
    parser = argparse.ArgumentParser(description="Macronize any Latin text you send")

    # Add positional argument
    parser.add_argument("-t", '--text', help="The text you want to be macronized")
    parser.add_argument("-c", '--copy', action='store_true', help="Copy text from clipboard")

    # Parse the arguments
    args = parser.parse_args()

    if (args.copy):
        text = pyperclip.paste()
    if (args.text):
        text = args.text

    console = Console()
    print("Input:")
    console.print(Panel(text, expand=False, border_style="cyan"))
    response = submit_form(text)
    macronized_text = parse_html(response)
    print("Output:")
    console.print(Panel(macronized_text, expand=False, border_style="green"))
    pyperclip.copy(macronized_text)
    print("Output copied to clipboard!")

if __name__ == "__main__":
    main()