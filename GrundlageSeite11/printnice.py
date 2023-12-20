# prints frames around output
# can be ignored
def print_nice(message, is_input=False):
    if is_input:
        border = "╔" + "═" * (len(message) + 2) + "╗"
    else:
        border = "╠" + "═" * (len(message) + 2) + "╣"

    content = f"║ {message} ║"

    if is_input:
        bottom_border = "╚" + "═" * (len(message) + 2) + "╝"
    else:
        bottom_border = "╚" + "═" * (len(message) + 2) + "╝"

    print(border)
    print(content)
    print(bottom_border)