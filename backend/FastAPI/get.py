import requests

# APIのURL
url = "http://127.0.0.1:8000/todos/"

# POSTリクエストを送信
response = requests.get(url=url)

# レスポンスの内容を出力
if response.status_code == 200:
    print(response.json())
else:
    print(response.json())
