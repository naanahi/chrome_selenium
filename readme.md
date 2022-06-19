# docker-composeコマンド備忘録

1. Dockerイメージの作成→コンテナのビルド→コンテナの起動
```
docker-compose up -d --build
```

2. 起動しているコンテナを確認
```
$ docker ps

CONTAINER ID   IMAGE                        COMMAND     CREATED          STATUS          PORTS     NAMES
2d78b9c451a2   chromedriver_win32_python3   "python3"   23 minutes ago   Up 23 minutes             python3
```
3. コンテナに接続
```
docker compose exec python3 bash
```

4. カレントディレクトリの状態  
※ result.csvとitems.dbはスクリプト実行時に作成される
```
root@2d78b9c451a2:/usr/src/app# ls -l

total 72
drwxr-xr-x 1 root root  4096 Jun 19 13:25 __pycache__
-rwxrwxrwx 1 root root   234 Jun 19 09:46 create_sqlite.py
-rwxrwxrwx 1 root root  1527 Jun 19 08:23 dataframe.py
-rw-r--r-- 1 root root 32768 Jun 19 13:25 items.db
-rwxrwxrwx 1 root root  2009 Jun 19 12:52 main.py
-rwxrwxrwx 1 root root   243 Jun 19 09:50 read_sqlite.py
-rw-r--r-- 1 root root 22141 Jun 19 13:25 result.csv
-rwxrwxrwx 1 root root  2020 Jun 19 07:03 search_items.py
-rwxrwxrwx 1 root root   954 Jun 19 08:23 search_pages.py
-rwxrwxrwx 1 root root   538 Jun 19 06:42 search_word.py
-rwxrwxrwx 1 root root   192 Jun 19 13:25 settings.py
```

5. main.pyを実行(実行が正常終了した場合、result.csvとitems.dbが作成される)
```
python3 main.py
```

