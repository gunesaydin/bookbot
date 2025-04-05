from stats import count_words, count_letters, sort_dict
import sys

def get_book_text(filepath):
    content = ""

    with open(filepath) as file:
        content = file.read()

    return content

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    print("============ BOOKBOT ============")
    content = get_book_text(book_path)
    print(f"Analyzing book found at {book_path}")
    num_words = count_words(content)
    letter_dict = sort_dict(count_letters(content))
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for key in letter_dict:
        if key.isalpha() == False:
            continue
        else:
            print(f"{key}: {letter_dict[key]}")

main()