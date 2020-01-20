import requests
from user import User
import webbrowser

app_id = "b80beaf6f51d41a78c7e7e5b95703a41"
secret = "3c991ff268ab4b9b9eb7d687341e9361"
callback_url = "https://oauth.yandex.ru/verification_code"
code_url = f"https://oauth.yandex.ru/authorize?" \
           f"response_type=code&client_id={app_id}"
code = ""

name = input("Hi! What is your first name?\n")
l_name = input("Nice to meet you! And the last name?\n")
age = input(f"The last question here, how old is {name} {l_name}?\n")
user = User(name, l_name, age)
print("Nice! For next step you need to give me access to your Yandex.Disk."
      "\nYou will be redirected to Yandex login page. "
      "After sign in, you will get code."
      "\nRemember this code and enter to field bellow."
      "\nPress ENTER to open browser.")
input()
webbrowser.open(code_url)
if len(code) == 0:
    code = input("Enter your code:\n")
while len(code) != 7 or str.isdigit(code) is False:
    print("No way you get this code from Yandex! Try again!\n"
          "Code must consist of 7 digits")
    code = input("Enter your code:\n")

oauth_headers = {"Accept": "application/x-www-form-urlencoded",
                 "Content-Type": "application/json; charset=UTF-8"}
data = f"grant_type=authorization_code" \
       f"&code={code}" \
       f"&client_id={app_id}" \
       f"&client_secret={secret}"
get_token = requests.post(f"https://oauth.yandex.ru/token",
                          headers=oauth_headers,
                          data=data)
token = get_token.json()
headers = {"Authorization": "OAuth " + token["access_token"],
           "Accept": "application/json",
           "Content-Type": "application/json; charset=UTF-8"}

print("Great! Now we can upload data.json to your Yandex.Disk.\n")

pr = requests.get("https://cloud-api.yandex.net/v1/disk/resources/upload"
                  "?path=data1.json&fields=href&overwrite=true",
                  headers=headers)
upload_link = pr.json()
f = open("data.json")
up = requests.put(upload_link["href"], headers=headers, data=f)
if up.status_code != 201:
    print("Error occurred. Try again")
else:
    print("Success!")
input("Press ENTER to exit")
