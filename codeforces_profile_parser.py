import requests

handle = "The_Witcher76"  # Put your CF handle
url = f"https://codeforces.com/api/user.info?handles={handle}"

response = requests.get(url)  # This is the "API Call"
data = response.json()        # This converts the "text" into a Python Dictionary
print(data)
if data["status"] == "OK":
    user_info = data["result"][0]
    print(f"Handle: {user_info['handle']}")
    print(f"Current Rating: {user_info['rating']}")
    print(f"Rank: {user_info['rank']}")