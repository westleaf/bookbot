def get_num_words(text_to_read):
  return text_to_read.split()

def get_num_char(text_to_read):
  word_dict={}
  for char in text_to_read:
    if char.lower() not in word_dict:
      word_dict[char.lower()] = 1
    else:
      word_dict[char.lower()] += 1

  return word_dict
