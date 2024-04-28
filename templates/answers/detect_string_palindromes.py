def is_palindrome(chars: str) -> bool:
    """Accepts sanitized string (no punctuation, capitals, or white spaces) and returns True if it is a palindrome"""
    if len(chars) == 1 or len(chars) == 0:
        return True
    
    head, mid, last = chars[0], chars[1:-1], chars[-1]

    return head == last and is_palindrome(mid)



def detect_string_palindrome(chars: str) -> str:
    """
    Accepts a string and returns True if string is a palindrome
    Valid palindromes are spelt the same forwards and backwards, for example:
        - "racecar" reversed racecar so racecar should return:
            "racecar is a valid palindrome"
        - "corgis" is "sigroc" reversed so "corgis" should return:
            "corgis is not a valid palindrome"
    Case, punctuation, and whitespaces should be ignored
    """

    
    new_chars = ''.join([char.lower() for char in chars if char.isalpha()])
    truth = is_palindrome(new_chars)
    if truth == True:
        return f"{chars} is a valid palindrome"
    else:
        return f"{chars} is not a valid palindrome"
    
