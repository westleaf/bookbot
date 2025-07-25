from stats import *
import sys

path_to_book=""

def get_book_text(path_to_file):
  with open(path_to_file) as f:
    return f.read()

def main():
  if len(sys.argv)!=2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
  else:
    path_to_book=sys.argv[1]


  num_words = len(get_num_words(get_book_text(path_to_book)))
  num_char = get_num_char(get_book_text(path_to_book))
  sorted_list = get_sorted_list(num_char)
  print(f"============ BOOKBOT ============")
  print(f"Analyzing book found at {path_to_book}...")
  print(f"----------- Word Count ----------")
  print(f"Found {num_words} total words")
  print(f"--------- Character Count -------")
  for item in sorted_list:
    if item["char"].isalpha():
      print(f"{item["char"]}: {item["num"]}")

main()
