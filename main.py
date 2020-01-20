import requests
import json
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
print("Nice! For next step you need to give me access to your Yandex.Disk."
      "\nYou will be redirected to Yandex login page. After sign in, you will get code."
      "\nRemember this code and enter to field bellow.\nPress ENTER to open browser.")
input()
webbrowser.open(code_url)
code = input("Enter your code:\n")
print(f"Your code is:{code}.\nAnd another one little step: we need authorization token. \nYou will be redirected to Yandex login page. "
      f"Copy token, and paste to field bellow.\nPress ENTER to open browser")
input()
webbrowser.open(f"https://oauth.yandex.ru/authorize?grant_type=authorization_code"
                f"&code={code}&client_id={app_id}&response_type=token")
token = input("Enter your token:\n")
headers = {"Authorization": "OAuth " + token, "Accept": "application/json", "Content-Type": "application/json; charset=UTF-8"}

print("Great! Now we can upload data.json to your Yandex.Disk.\nPress ENTER to continue!")

pr = requests.get("https://cloud-api.yandex.net/v1/disk/resources/upload?path=data1.json&fields=href&overwrite=true", headers=headers)
upload_link = pr.json()
up = requests.put(upload_link["href"], headers=headers, data=json.dumps(You.__dict__))
if up.status_code != 201:
    print("Error occurred. Try again")
else:
    print("Success!")
input("Press ENTER to exit")


