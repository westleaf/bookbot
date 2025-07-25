from stats import *

def get_book_text(path_to_file):
  with open(path_to_file) as f:
    return f.read()

def main():
  num_words = len(get_num_words(get_book_text("books/frankenstein.txt")))
  num_char = get_num_char(get_book_text("books/frankenstein.txt"))
  print(f"{num_words} words found in the document")
  print(f"{num_char}")

main()
