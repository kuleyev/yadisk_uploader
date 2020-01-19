import requests
import json
import datetime
from user import User
import webbrowser

app_id = "b80beaf6f51d41a78c7e7e5b95703a41"
secret = "3c991ff268ab4b9b9eb7d687341e9361"
callback_url = "https://oauth.yandex.ru/verification_code"

code_url = f"https://oauth.yandex.ru/authorize?response_type=code&client_id={app_id}"

name = input("Hi! What is your first name?\n")
l_name = input("Nice to meet you! And the last name?\n")
age = input("The last question here, how old is " + name + " " + l_name + "?\n")
You = User(name, l_name, age)

# проверка
print(json.dumps(You.__dict__, ensure_ascii=False))
# запись в файл
with open('data.json', 'w') as outfile:
    json.dump(You.__dict__, outfile, ensure_ascii=False)
print("""   Nice! For next step you need to give me access to your Yandex.Disk.
    You will be redirected to Yandex login page. After sign in, you will get code.
    Remember this code and enter to field bellow.

    Press ENTER for redirect!
    """)
input()
webbrowser.open(code_url)
code = input("Enter your code:\n")
print(f"Your code is:{code}.\nAnd another one little step: we need authorization token."
      f"\nYou will be redirected to Yandex login page. Copy token, and paste to field bellow."
      f"\nPress ENTER for redirect!")
input()
webbrowser.open(f"https://oauth.yandex.ru/authorize?grant_type=authorization_code"
                f"&code={code}&client_id={app_id}&response_type=token")
token = input("Enter your token:")
print("Great! Now we can upload data.json to your Yandex.Disk. "
      "Are you ready? (Enter Y for 'yes', or 'N' for 'no'")
url = "https://cloud-api.yandex.net/v1/disk"
headers = {"Authorization": "OAuth AgAAAAAGJItvAAYU1waZ0TdN00hTo94dlCmsIlo", "Accept" : "application/json", "path": "/"}
r = requests.get(url, headers=headers)
print(r.json())

