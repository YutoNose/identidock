# ベースイメージとして最新のJenkins LTSを使用
FROM jenkins/jenkins:lts

# rootユーザーとして作業を開始
USER root

# 必要なパッケージをインストール
RUN apt-get update && \
    apt-get install -y apt-transport-https ca-certificates curl gnupg lsb-release sudo && \
    curl -fsSL https://download.docker.com/linux/debian/gpg | gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg && \
    echo "deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/debian $(lsb_release -cs) stable" > /etc/apt/sources.list.d/docker.list && \
    apt-get update && \
    apt-get install -y docker.io && \
    rm -rf /var/lib/apt/lists/*

# jenkinsユーザーにsudo権限を付与（Dockerグループには追加しない）
RUN usermod -aG sudo jenkins && \
    echo "jenkins ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers

# Docker Composeをインストールする
RUN curl -L "https://github.com/docker/compose/releases/download/1.4.1/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose && \
    chmod +x /usr/local/bin/docker-compose

# jenkinsユーザーに切り替え
USER jenkins

# プラグインリストをコピー
COPY plugins.txt /usr/share/jenkins/plugins.txt

# Jenkinsプラグインのインストール
RUN jenkins-plugin-cli --plugin-file /usr/share/jenkins/plugins.txt

# Docker CLIが動作することを確認するためのエントリポイントを設定
ENTRYPOINT ["jenkins.sh"]
