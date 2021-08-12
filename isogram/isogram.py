def is_isogram(string):
    if "-" or " " in string:
        string = string.replace("-", "")
        string = string.replace(" ", "")

    if len(set(string.lower())) == len(string):
        return True
    return False
