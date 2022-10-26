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

* Visual Studio Codeでライブラリやモジュールが could not be resolved になる時の対処法
https://startlab.jp/learning-python/vscode-settings/

## STEP03

* .env と --env-file の違い
https://qiita.com/SolKul/items/989727aeeafcae28ecf7
https://labor.ewigleere.net/2022/05/23/docker-compose-change-enviroment-variables-file/

## STEP04

* 【Python】sys.pathに追加したディレクトリからimportする処理でPEP8に違反した際の対処
https://qiita.com/ninomiyt/items/76f6f7e3c1f833cf99e5
https://stackoverflow.com/questions/36827962/pep8-import-not-at-top-of-file-with-sys-path
https://teratail.com/questions/65319

* alembicの使い方
https://zenn.dev/jafro/articles/183020be3a0cea482c5b

* schemaの付け方　op.execute()を使う
https://qiita.com/taito273/items/d35b08f73812c8ab9b17
https://stackoverflow.com/questions/49582020/sqlalchemy-alembic-create-schema-migration

* default値の付け方　server_default=xxx
https://gene.hatenablog.com/entry/20140131/1391186587

* timestampの使い方
https://nmomos.com/tips/2021/02/21/fastapi-docker-6/

* postgresqlのtimezone
https://qiita.com/rururu_kenken/items/972314402d588e073d40
https://zenn.dev/team_zenn/articles/postgresql-timestamp

* sql
https://zenn.dev/team_zenn/articles/postgresql-timestamp
https://qiita.com/rururu_kenken/items/972314402d588e073d40

INSERT INTO todo.tasks VALUES (DEFAULT, 'title1', 'desctiption', '316');
UPDATE todo.tasks SET status = 'DOING' WHERE id = 1;
show timezone;
select now();
SET SESSION timezone TO 'Asia/Tokyo';
