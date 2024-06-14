# 最新のPythonバージョンを使用
FROM python:3.8-slim

# 必要なビルドツールとライブラリをインストール
RUN apt-get update && apt-get install -y \
    gcc \
    musl-dev \
    python3-dev \
    libpcre3-dev \
    libssl-dev \
    build-essential \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# pipを最新にアップグレード
RUN groupadd -r uwsgi && useradd -r -g uwsgi uwsgi
RUN pip install --upgrade pip

# FlaskとuWSGI、Werkzeugをインストール
RUN pip install Flask==2.1.2 uWSGI==2.0.19.1 Werkzeug==2.2.2 requests==2.5.1 redis==2.10.3

# ワーキングディレクトリを設定
WORKDIR /app

# ホストのappディレクトリをコンテナの/appディレクトリにコピー
COPY app /app
COPY cmd.sh /

EXPOSE 9090 9191
USER uwsgi

CMD ["/cmd.sh"]
