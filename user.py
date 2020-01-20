import json
class User:

    def __init__(self, name, l_name, age):
        self.name = name
        self.l_name = l_name
        self.age = age
        with open('data.json', 'w') as outfile:
            json.dump(self.__dict__, outfile, ensure_ascii=False)
        return print("File created!")