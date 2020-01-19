import requests
import json
import datetime
from user import User
import webbrowser

app_id = "b80beaf6f51d41a78c7e7e5b95703a41"
secret = "3c991ff268ab4b9b9eb7d687341e9361"
callback_url = "https://oauth.yandex.ru/verification_code"

code_url = f"https://oauth.yandex.ru/authorize?response_type=code&client_id={app_id}"
code = ""

# name = input("Hi! What is your first name?\n")
# l_name = input("Nice to meet you! And the last name?\n")
# age = input("The last question here, how old is " + name + " " + l_name + "?\n")
# You = User(name, l_name, age)
#
# # проверка
# print(json.dumps(You.__dict__, ensure_ascii=False))
# # запись в файл
# with open('data' + str(datetime.datetime.now()) + '.json', 'w') as outfile:
#     json.dump(You.__dict__, outfile, ensure_ascii=False)
# print("""Nice! For next step you need to give me access to your Yandex.Disk.
#     You will be redirected to Yandex login page. After sign in, you will get code.
#     Remember this code and enter to field bellow.
#
#     Press ENTER for redirect!
#     """)
# input()
webbrowser.open(code_url)
code = input("Enter your code:\n")
print(code)
r = requests.get(f"https://oauth.yandex.ru/authorize?grant_type=authorization_code&code={code}&client_id={app_id}&response_type=token")
print(r.json())