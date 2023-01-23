import string

words_list = list(string.ascii_uppercase)
words_list.extend(list(string.ascii_uppercase))


def encode(word, shift):
    encode_word = ""
    for i in word:
        position = words_list.index(i)
        new_position = position + shift
        new_letter = words_list[new_position]
        encode_word += new_letter
    print(encode_word)


def decode(word, shift):
    decode_word = ""
    for i in word:
        position = words_list.index(i)
        new_position = position - shift
        new_letter = words_list[new_position]
        decode_word += new_letter
    print(decode_word)


while True:
    code = input("enter if you need encode or decode:").upper()
    if code == "ENCODE":
        encode(word=input("enter a word you need to Encode:").upper(), shift=int(input("enter a number to shift:")))
    elif code == "DECODE":
        decode(word=input("enter a word you need to Decode:").upper(), shift=int(input("enter a number to shift:")))
    end = input("if you want to continue type yes or press no")
    if end == "yes":
        continue
    else:
        break
