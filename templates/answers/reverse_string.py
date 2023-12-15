# recursively prints a string backwards

def reverse_string(chars: str) -> str:
    if len(chars) == 1:
        return chars
    
    return chars[-1] + reverse_string(chars[0:-1])