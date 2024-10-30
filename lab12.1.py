def format_string(s):
    while len(s) % 4 != 0:
        s += " "
    
    for i in range(0, len(s), 4):
        print(s[i:i+4])

def first_and_last_word(s):
    words = s.split()
    first_word = words[0] 
    last_word = words[-1]
    print(first_word)
    print(last_word)

input_string = input("Введіть рядок: ")
format_string(input_string)
first_and_last_word(input_string)
