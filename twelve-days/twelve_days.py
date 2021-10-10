structure = [
    ('first', 'a Partridge in a Pear Tree.'),
    ('second', 'two Turtle Doves, '),
    ('third', 'three French Hens, '),
    ('fourth', 'four Calling Birds, '),
    ('fifth', 'five Gold Rings, '),
    ('sixth', 'six Geese-a-Laying, '),
    ('seventh', 'seven Swans-a-Swimming, '),
    ('eighth', 'eight Maids-a-Milking, '),
    ('ninth', 'nine Ladies Dancing, '),
    ('tenth', 'ten Lords-a-Leaping, '),
    ('eleventh', 'eleven Pipers Piping, '),
    ('twelfth', 'twelve Drummers Drumming, '),
]

def recite(start_verse, end_verse):
    song_list = []

    for verse in range(start_verse, end_verse + 1):
        each_verse = first_part(verse) + second_part(verse)
        song_list.append(each_verse)

    return song_list

def first_part(verse):

    verse_segment = f'On the {structure[verse-1][0]} day of Christmas ' \
            f'my true love gave to me: '

    return verse_segment

def second_part(verse):
    verse_segment = ''

    for i in range(verse, 0, -1):
        verse_segment += structure[i-1][1]
        if i == 2: verse_segment += 'and '

    return verse_segment