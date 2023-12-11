Render.com 公開先リンク（※ファイル保存のバグあり）
https://pjt1.onrender.com/

スケーターと貸切主催者の代わりに「CD・音源集め」をしてくれるアプリです。

PythonのDjangoフレームワークを活用しました。

### step0:Githubのクローン

プロジェクトフォルダを作成。Github上のファイルをローカル環境にクローン : `git clone このリポジトリのアドレス`

### step1:Pythonの仮想環境を構築

次のコマンドを実行して`env`という仮想環境を作成 : `python3 -m venv env`

仮想環境を起動する。これにより、Pythonのパッケージ管理が非常にやりやすくなる。（もしパッケージインストールでバグが出たら`env`フォルダごと削除して作り直せばOK）: `. env/bin/activate`(Macの場合。Windowsは別コマンドなので注意)

### step2:Django関連のパッケージをインストール

requirements.txtに記載されたパッケージをまとめてインストール : `pip install -r requirements.txt`

追加でインストールしたい場合 : `pip install パッケージ名`

### step3:SQLite３データベースを構築

マイグレーションファイルを実行してデータベースを構築 : `python manage.py migrate`

### step4:管理者(superuser)を作成

次のコマンドで管理者アカウントを作成。コンソール上でユーザー名・メールアドレス（任意）・パスワード（8文字以上）を入力して作成。 : `python manage.py createsuperuser`

### step5:アプリのサーバーを起動

次のコマンドを実行してサーバーを起動。コンソールに表示されるURLに接続するとアプリが表示される（ハズ） : `python manage.py runserver`

もしコンソールにバグが表示されたら、いったん`Control + C`でサーバーを停止して対処法をググる。
