import sys

COLORS = {
    'red': '\033[91m',
    'green': '\033[92m',
    'yellow': '\033[93m',
    'blue': '\033[94m',
    'magenta': '\033[95m',
    'cyan': '\033[96m',
    'white': '\033[97m',
    'reset': '\033[0m',
    'bold': '\033[1m',
    'underline': '\033[4m'
}

def pprint(data, color='cyan', bold=False, box=False):
    """
    Custom print function that beautifies output.
    
    Arguments:
        data: Any object to print (list, dict, tuple, str, etc.).
        color: Text color (red, green, yellow, etc.).
        bold: Whether to print the text in bold.
        box: Whether to print the data in a box.
    """
    
    formatted_data = format_data(data)
    
    if color in COLORS:
        formatted_data = COLORS[color] + formatted_data + COLORS['reset']
    
    if bold:
        formatted_data = COLORS['bold'] + formatted_data + COLORS['reset']
    
    if box:
        formatted_data = wrap_in_box(formatted_data)
    
    sys.stdout.write(formatted_data + '\n')

def format_data(data):
    """
    Convert any data structure into a readable string.
    """
    if isinstance(data, list):
        return format_list(data)
    elif isinstance(data, dict):
        return format_dict(data)
    elif isinstance(data, tuple):
        return format_tuple(data)
    else:
        return str(data)

def format_list(lst):
    return "[ " + ", ".join(str(item) for item in lst) + " ]"


def format_dict(d):
    return "{\n" + "\n".join(f"  {k}: {v}" for k, v in d.items()) + "\n}"


def format_tuple(tpl):
    return "( " + ", ".join(str(item) for item in tpl) + " )"


def wrap_in_box(text):
    """
    Wrap the text inside a box made of '-'.
    """
    lines = text.splitlines()
    width = max(len(line) for line in lines)
    box_top = '+' + '-' * (width + 2) + '+'
    box_bottom = box_top
    wrapped_lines = '\n'.join(f'| {line.ljust(width)} |' for line in lines)
    return f"{box_top}\n{wrapped_lines}\n{box_bottom}"
