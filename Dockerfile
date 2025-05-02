FROM python:3.12.4-slim

WORKDIR /app

# 依存パッケージをインストール
COPY dependency_list.txt .
RUN pip install --no-cache-dir -r dependency_list.txt

# アプリケーションコードをコンテナにコピー
COPY . .

# コンテナ起動時のコマンド
CMD ["python", "-m", "ipython"]