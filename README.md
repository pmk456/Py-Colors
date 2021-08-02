# Py-Colors
## Installation
```shell
pip install py-colors
```
## Note
```text
If Your Using Windows This package will add all available colors
to windows registry so you can easily add colors to your code.
```
# Usage
```python
from colors import *
# First Method
print(fg_color + bg_color + style + "Hello, World")
# Second Method
print(color(string="Hello, World", fg="blue", bg="black", style="bold"))
```
# Available Colors
### Colors
```
RED
BLUE
CYAN
YELLOW
GREEN
MAGENTA
WHITE
BLACK
```
### Backgrounds
```
BG_BLACK
BG_RED
BG_GREEN
BG_YELLOW
BG_BLUE
BG_MAGENTA
BG_CYAN
BG_WHITE
```
### Styles
```
RESET
BOLD
REVERSE
UNDERLINE
ITALIC
BLINK
INVISIBLE
RED_UNDERLINE
GREEN_UNDERLINE
STRIKE
CURLY_UNDERLINE
```