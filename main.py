import json


class Iterator_dict:

    def __init__(self, data):
        self.data = data
        self.step = 0
        self.current = None
        self.stop = len(data) - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.step > self.stop:
            raise StopIteration
        name = self.data[self.step]["name"]["common"]
        name_for_url = name.split()
        url = "https://en.wikipedia.org/wiki/"
        if len(name_for_url) >1:
            for part_name in name_for_url:
                url = url + part_name + "_"
            url = url [:-1]
        else:
            url = url + name_for_url[0]
        self.step += 1

        return name, url


with open("countries.json", "r") as file:
    data_file = json.load(file)

my_iter = Iterator_dict(data_file)
with open("result.txt", "w", encoding="utf-8") as file_write:
    for i in my_iter:
        file_write.write(f"Название страны: {i[0]}  - Ссылка: {i[1]}\n")
        print(i)