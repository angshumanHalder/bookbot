import sys
from stats import get_num_words
from stats import get_num_characters

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    file_contents = get_book_text(sys.argv[1])
    word_count = get_num_words(file_contents)
    charcter_count = get_num_characters(file_contents)

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {len(word_count)} total words")
    print("--------- Character Count -------")
    for k, v in charcter_count.items():
        print(f"{k}: {v}")


main()

