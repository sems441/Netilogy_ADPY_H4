import hashlib


def my_generator(file_name):
    with open(file_name, "rb") as file_read:
        for number, line in enumerate(file_read):
            line = hashlib.md5(line)
            yield f"Строка № {number} - хэш: {line.hexdigest()}"


line_read_generator = my_generator("text.txt")
print(line_read_generator)
for result in line_read_generator:
    print(result)
