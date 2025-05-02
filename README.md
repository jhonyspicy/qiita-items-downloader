# qiita-items-downloader
Qiitaの記事をダウンロードしてローカルに保存します。
# Qiita記事ダウンローダー

このプロジェクトはQiitaの記事をダウンロードして、ローカルのMarkdownファイルとして保存するツールです。

## セットアップ

1. 依存関係をインストールします：
   ```
   pip install -r dependency_list.txt
   ```

2. `.env`ファイルを作成し、以下の情報を設定します：
   ```
   USER_NAME=あなたのQiitaユーザー名
   ACCESS_TOKEN=あなたのQiitaアクセストークン
   QIITA_TEAM_NAME=あなたのQiitaチーム名（チームがない場合は空欄）
   ```

## 使用方法

スクリプトを実行するには：