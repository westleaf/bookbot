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

def sort_on(items):
  return items["num"]

def get_sorted_list(dict_to_sort):
    sorted_dict_list=[]
    for key, value in dict_to_sort.items():
      sorted_dict_list.append({"char":key, "num":int(value)})

    sorted_dict_list.sort(key=sort_on)
    return sorted_dict_list
