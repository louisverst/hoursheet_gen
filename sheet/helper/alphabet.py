def prev_letter(c: str) -> str:
    """
    Returns the next letter in the alphabet. Returns a capital if the input is capital, lowercase otherwise.
    
    :param str c:
    :return str:
    """
    if len(c) != 1:
        raise ValueError("Letter should be provided as strings of length 1.")

    if c.isupper():
        if c == "A":
            return "Z"
        else:
            return chr(ord(c) - 1)
        
    if c.islower():
        if c == "a":
            return "z"
        else:
            return chr(ord(c) - 1)


    raise ValueError("Invalid input for prev_letter()")

def next_letter(c: str) -> str:
    """
    Returns the previous letter from the alphabet relative to the input. Returns a capital if the input is capital, lowercase otherwise.

    :param str c:
    :return str:
    """

    if len(c) != 1:
        raise ValueError("Letter should be provided as strings of length 1.")

    if c.isupper():
        if c == "Z":
            return "A"
        else:
            return chr(ord(c) + 1)
        
    if c.islower():
        if c == "z":
            return "a"
        else:
            return chr(ord(c) + 1)


    raise ValueError("Invalid input for next_letter()")