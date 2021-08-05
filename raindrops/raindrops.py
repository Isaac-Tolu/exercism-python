def convert(number):

    convert_str = ''
    
    if number % 3 == 0:
        convert_str += 'Pling'
    if number % 5 == 0:
        convert_str += 'Plang'
    if number % 7 == 0:
        convert_str += 'Plong'
    if (number % 3 != 0) and (number % 5 != 0) and \
        (number % 7 != 0):
        convert_str = str(number)

    return convert_str