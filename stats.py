def get_num_words(book_text):
    try:
        words = book_text.split()
    except Exception as e:
        print(e)
    return(len(words))

def get_char_count(book_text):
    char_count = {}
    try:
        words = book_text.lower().split()
        for word in words:
            for letter in word:
                if letter not in char_count:
                    char_count[letter] = 1
                else:
                    char_count[letter] += 1
    except Exception as e:
        print(e)
    
    return char_count

def get_sorted_count(char_count):
    output_dict = {}
    sorted_dict = dict(sorted(char_count.items(), key = lambda item: item[1], reverse = True))
    for key in sorted_dict:
        if key.isalpha() == True:
            print(f'{key}: {sorted_dict[key]}')