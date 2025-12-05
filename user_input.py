from rich.panel import Panel
from rich.text import Text
from rich.style import Style
from rich.color import Color

from console import console

def introduction():
    """
    Displays the introduction.
    """
    green = Color.from_rgb(25, 200, 40)
    border_style = Style(color=green)

    heading
    console.print(Panel("[white]Welcome to the Hour Sheet Generator Script!", style=border_style, padding=1), justify="center")

    