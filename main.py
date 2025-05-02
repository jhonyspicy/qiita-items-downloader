import requests
import time
import os
import re
from datetime import datetime
from dotenv import load_dotenv

# .envファイルから環境変数を読み込む
load_dotenv()

USER_NAME = os.getenv("USER_NAME")
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
QIITA_TEAM_NAME = os.getenv("QIITA_TEAM_NAME")

headers = {
    "Authorization": f"Bearer {ACCESS_TOKEN}"
}

team = f"{QIITA_TEAM_NAME}." if QIITA_TEAM_NAME else ""
url = f"https://{team}qiita.com/api/v2/users/{USER_NAME}/items"

page = 1
per_page = 100
has_next_page = True

while has_next_page:
    params = {
        'page': page,
        'per_page': per_page
    }

    print(f"ページ {page} の記事を取得中...")

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        items = response.json()

        # 取得した記事がない場合、ループを終了
        has_next_page = False
        if not items:
            has_next_page = False
            print("すべての記事を取得しました。")
            break

        # 記事情報の表示と保存
        for item in items:
            # ファイル名から無効な文字を削除
            def sanitize_filename(filename):
                return re.sub(r'[<>:"/\\|?*]', '', filename)


            # 記事の日付を取得してフォーマット
            created_date = datetime.fromisoformat(item['created_at'].replace('Z', '+00:00')).strftime('%Y%m%d')

            # ファイル名を作成
            filename = f"{created_date}_{sanitize_filename(item['title'])}.md"

            # 記事保存用のディレクトリを作成
            os.makedirs('articles', exist_ok=True)

            # 記事を保存
            with open(os.path.join('articles', filename), 'w', encoding='utf-8') as f:
                f.write(f"# {item['title']}\n\n")
                f.write(f"Author: {item['user']['id']}\n")
                f.write(f"Created: {item['created_at']}\n\n")
                f.write(item['body'])

            # print(f"タイトル: {item['title']}")
            # print(f"ユーザー：{item['user']['id']}")
            # print(f"投稿日: {item['created_at']}")
            # print(f"保存先: articles/{filename}")
            # print("-" * 40)

        # 次のページへ
        page += 1

        # 1秒待機
        print("次のページを取得する前に1秒待機します...")
        time.sleep(1)
        
    else:
        print("取得失敗:", response.status_code, response.text)
        has_next_page = False