FROM python:3.13.2

# 作業ディレクトリ
WORKDIR /workspace

# 必要パッケージ
COPY requirements.txt ./
RUN pip install -r requirements.txt

# コンテナ起動時にVSCodeが接続するための環境
CMD ["sleep", "infinity"]