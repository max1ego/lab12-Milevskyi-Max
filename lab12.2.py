import random

names = ["Олександр", "Марія", "Іван", "Ольга", "Андрій", "Світлана", 
         "Юрій", "Ірина", "Дмитро", "Наталя", "Сергій", "Анна"]

def generate_line():
    line = ""
    while len(line) + len(random.choice(names)) + 1 <= 100:
        line += random.choice(names) + " "
    return line.strip()

def write_lines_to_file(n, filename="output.txt"):
    f = open(filename, "w", encoding="utf-8")
    for i in range(n):
        f.write(generate_line() + "\n")
    f.close()

N = int(input("Введіть кількість рядків: "))
write_lines_to_file(N)
print("Done")
