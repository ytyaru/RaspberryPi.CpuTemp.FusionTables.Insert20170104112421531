# このソフトウェアについて

RaspberryPi.CpuTemp.FusionTables.Insert20170104112421531は私個人が学習目的で作成したソフトウェアである。

RaspberryPiのCPU温度をGoogleFusionTablesに記録する。

# 開発環境

* Raspberry Pi 3B
    * Raspbian Jessie 2016-09-23
    * Python 3.4.2
* Windows XP Pro SP3 32bit
    * コンソール(cmd.exe)
    * SQLite3
    * Python 3.4.4, 2.7.10
    * Firefox 50.1.0
* Google
    * [Account](https://accounts.google.com/signup)
    * [Developers Console](https://console.developers.google.com/)
        * Projectを作成する
            * ClientId, ApiKeyを作成する
            * [Fusion Tables API](https://developers.google.com/fusiontables/)を有効にする
    * [Drive](https://drive.google.com/drive/my-drive)
        * [Fusion Tables](https://fusiontables.google.com/DataSource?dsrcid=implicit)
    * [Fusion Tables query API](https://developers.google.com/fusiontables/docs/v2/using)
        * https://www.googleapis.com/fusiontables/v2/query
    * [Google Identity Platform](https://developers.google.com/identity/)
        * [get token API](https://developers.google.com/identity/protocols/OAuth2InstalledApp)
            * https://www.googleapis.com/oauth2/v4/token
        * [get code API](https://developers.google.com/identity/protocols/OAuth2UserAgent)
            * https://accounts.google.com/o/oauth2/auth

# 実行

```sh
python3 CpuTempInserter.py
```

Raspberry Piで実行する。指定したFusionTablesにCPU温度がInsertされる。

## 補足

コード|説明
------|----
CpuTempInserter.py|メイン。doc_idなどキー値を指定する。
FusionTablesRequester.py|FusionTablesAPIを実行する。
AccessTokenRequester.py|RefreshTokenからAccessTokenを取得する。
GoogleKeysGetter.py|SQLite3データベースから各キー値を取得する。

CpuTempInsert.pyからコードを追えばわかるが、必要なキーの取得はProjectIdから取ってきている。client_secretなどの重要なキーはハードコーディングせずDBから参照するようにしてある。

## 事前準備

* ![GitHub](http://www.google.com/s2/favicons?domain=github.com "GitHub")[Google.OAuth.Database](https://github.com/ytyaru/Google.OAuth.Database20170103111721000)で必要なキー(MailAddress, Password, ProjectId, ApiKey, ClientId, ClientSecret, RefreshToken)を登録すること
* DBは`Google.Accounts.sqlite3`というファイル名で`CpuTempInsert.py`と同じディレクトリに配置すること

* [Fusion Tables](https://fusiontables.google.com/DataSource?dsrcid=implicit)でテーブルを作成したときのdoc_idをCpuTempInsert.pyに設定する。カラム名をinsert文と一致させる。

# ライセンス #

このソフトウェアはCC0ライセンスである。

[![CC0](http://i.creativecommons.org/p/zero/1.0/88x31.png "CC0")](http://creativecommons.org/publicdomain/zero/1.0/deed.ja)
