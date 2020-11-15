# news-search
## 前提条件
Pythonがインストールされていること。

OSがWindows (.batファイルでプログラムを自動で起動するため)

## How to Use
- STEP1.　pip installで必要なライブラリをインストールするため、「pip-install.bat」をダブルクリックする。

- STEP2.　keywords.txtに検索したいキーワードを記入

例：keywords.txtの中身を下記のように記入
>ハイブリッドIT

この場合、記事に「ハイブリッドIT」という単語が存在するかを検索する。

(複数のキーワードを検索したい場合、ハイブリッドITの下にキーワードを記入するとできるが、テストが不十分なため非推奨。)

- STEP3.　「NewsSearch.bat」をダブルクリックする。

現在はCloudWatchとZDNETから記事を検索し、キーワードに合致した記事のタイトルとリンクを「HybridIT.xlsx」に保存する。
