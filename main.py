# function which takes a string and returns a list of corresponding numbers rep as an ascii code
def word_as_ascii(text):
  list_char = [(n,ord(n)) for n in text]
  pprint(list_char)

# word_as_ascii("fuofs abfdsb")

def map_harden(func, input_list):
  output_list =[]
  for n in input_list:
    output_list.append(func(n))
  return output_list

def encode(text):
  list_of_char = list(text)
  list_of_ascii = map_harden(ord,list_of_char)
  encoded_list_of_ascii = map_harden(lambda n:n + 13 if n + 13 < 123 else 97 + 13 - (123 - n), list_of_ascii)
  encoded_list_of_char = map_harden(chr,encoded_list_of_ascii)
  encoded_text = "".join(encoded_list_of_char)
  return encoded_text

map

print(encode("uryyb jbeyq"))
print(encode(encode("top secret!123")))
print(encode("lmnop"))
print(encode(encode("lmnop")))
