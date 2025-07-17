#main
from stats import count_words
from stats import letter_count
from stats import sort
import sys

def get_book_text(filepath):
    with open(filepath) as f:
           text = f.read()
    return text

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_text = get_book_text(sys.argv[1])
    total_words = count_words(book_text)
    char_counts = letter_count(book_text)
    sorted_list = sort(char_counts)

    print("============ BOOKBOT ============")
    print("Analyzing book found in books...")
    print("----------- Word Count ----------")
    print(f"Found {total_words} total words")
    print("--------- Character Count -------")

    for item in sorted_list:
        character = item["char"]
        count = item["num"]
        if character.isalpha():
            print(f"{character}: {count}")

    print("============= END ===============")

    
if __name__ == "__main__":
    main()
