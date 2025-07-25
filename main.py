from stats import *

def get_book_text(path_to_file):
  with open(path_to_file) as f:
    return f.read()

def main():
  num_words = len(get_num_words(get_book_text("books/frankenstein.txt")))
  num_char = get_num_char(get_book_text("books/frankenstein.txt"))
  sorted_list = get_sorted_list(num_char)
  print(f"{num_words} words found in the document")
  print(f"{num_char}")
  print(f"{sorted_list}")
  for i in range(0, len(sorted_list)):
    print(sorted_list[i])

main()
