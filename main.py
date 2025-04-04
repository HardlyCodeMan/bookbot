#!/bin/python3
import sys
from stats import get_num_words, get_char_count, get_sorted_count

def get_book_text(filepath):
    try:
        with open(filepath) as f:
            file_contents = f.read()
    except Exception as e:
        print(e)
    return file_contents

if len(sys.argv) != 2:
    print(f'Usage: python3 main.py <path_to_book>')
    sys.exit(1)
else:
    book = sys.argv[1]

#print(get_book_text(book))
print(f'============ BOOKBOT ============')
print(f'Analyzing book found at {book}')
print(f'----------- Word Count ----------')
print(f'Found {get_num_words(get_book_text(book))} total words')
print(f'--------- Character Count -------')
get_sorted_count(get_char_count(get_book_text(book)))
print(f'============= END ===============')