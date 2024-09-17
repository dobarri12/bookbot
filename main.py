def main ():
    book_path = "books/frankenstein.txt"
    with open(book_path) as f:
        file_contents = f.read()

    char_counts = count_chars(file_contents)
    chars_list = [{'char': char, 'num': count} for char, count in char_counts.items()]
    chars_list.sort(reverse=True, key=sort_on)
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words(file_contents)} words found in the document")
    for char_dict in chars_list:
        if char_dict['char'].isalpha():
            print(f"The '{char_dict['char']}' character was found {char_dict['num']} times")
    print("--- End report ---")



def num_words (book_text):
   return len(book_text.split())
    
def count_chars (book_text):
    chars = {}
    for c in book_text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

def sort_on(dict):
    return dict["num"]

main()
