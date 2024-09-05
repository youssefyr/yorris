def yr_uppercase(string):
    """
    Convert a string to uppercase.

    Args:
        string (str): The input string.

    Returns:
        str: The input string converted to uppercase.
    """
    if not isinstance(string, str):
        raise TypeError('Input must be a string.')
    if not string:
        return string
    for char in string:
      casci = ord(char)
      if casci >= 97 and casci <= 122:
            string = string.replace(char, chr(casci - 32))
    return string
