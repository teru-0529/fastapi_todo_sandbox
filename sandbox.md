FastAPIのスキーマクラスをOpenAPIから生成する方法
https://gift-tech.co.jp/articles/fastapi-openapi/

DockerでFastAPIの環境を作ってGETするまで
https://zenn.dev/satonopan/articles/c4e6d55a64da0c

FastAPI を使ってWEBアプリを作ってみる　その1
https://nmomos.com/tips/2021/01/23/fastapi-docker-1/

* SQLAlchemyを使用する

公式
https://fastapi.tiangolo.com/ja/

## STEP01

* PYTHONDONTWRITEBYTECODE
モジュールをimportするとデフォルトでインタープリターがソースコードをbytecodeに変換した結果をpycファイルとして書き出すようになっているが不要。`__pycache__`という名前のディレクトリに出力される。
https://devlights.hatenablog.com/entry/2018/02/23/124719

* PYTHONUNBUFFERED
非空なら標準出力・標準エラーのストリームのバッファリングを行わない
https://www.lifewithpython.com/2021/05/python-docker-env-vars.html

* vscodeのエクステンション/Lint
https://yurupro.cloud/767/
https://endy-tech.hatenablog.jp/entry/get_started_with_python_with_vscode
https://zenn.dev/yhay81/articles/yhay81-202102-pythonlint

## STEP03

* .env と --env-file の違い
https://qiita.com/SolKul/items/989727aeeafcae28ecf7
https://labor.ewigleere.net/2022/05/23/docker-compose-change-enviroment-variables-file/
