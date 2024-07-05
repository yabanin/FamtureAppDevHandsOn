import requests

# APIのURL
url = "http://127.0.0.1:8000/todos/"

# POSTリクエストで送信するデータ
item_data = {
    "title": "aaa",
    "done": False
}

# POSTリクエストを送信
response = requests.post(url, json=item_data)

# レスポンスの内容を出力
if response.status_code == 200:
    print("アイテムが作成されました:")
    print(response.json())
else:
    print(f"リクエストが失敗しました。ステータスコード: {response.status_code}")
    print(response.json())
