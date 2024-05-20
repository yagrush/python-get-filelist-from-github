# PythonでGithubのリポジトリの特定のディレクトリ直下にあるファイルを全て取得してローカルに保存する

## 試し方

### Githubのリポジトリの読み込み権限があるGithubアカウントのアクセストークンを作成する
https://github.com/settings/tokens

### `config.yaml`の`github_token`にそれを設定する

### `config.yaml`のその他の項目を設定する
- target_github_repository
  - author
  - name
  - target_dir_path

### python仮想環境を設定する
(グローバル環境を汚さないために)
```bash
python -m venv .venv
chmod 777 .venv/bin/activate
source ./.venv/bin/activate
```

### 必要なpythonパッケージをインストールする
```bash
pip install -r requirements.txt
```

### 実行する
```bash
python -m src
```
 ↓
このプロジェクトのルートディレクトリにディレクトリとファイルが保存されていればOK

## 使用ライブラリ
- [PyGithub](https://github.com/PyGithub/PyGithub)
