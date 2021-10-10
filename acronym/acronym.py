def abbreviate(words):

    for letter in words:
        if letter == "'": words = words.replace(letter, '')
        elif not(letter.isalpha()): words = words.replace(letter, ' ')

    return ''.join([word[0].upper() for word in words.split()])