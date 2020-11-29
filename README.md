# news-search
## 前提条件
Pythonがインストールされていること。(Pythonをインストールする際、パスを通しておくこと)

OS:Windows (.batファイルでプログラムを自動で起動するため)

## How to Use
**STEP1：pip installで必要なライブラリをインストールするため、「pip-install.bat」をダブルクリックする。**

**STEP2：keywords.txtに検索したいキーワードを記入**

例：keywords.txtの中身を下記のように記入
>ハイブリッドIT

この場合、記事に「ハイブリッドIT」という単語が存在するかを検索する。

(複数のキーワードを検索したい場合、ハイブリッドITの下にキーワードを記入するとできるが、テストが不十分なため非推奨。)

**STEP2.5:proxy.txtにプロキシ設定を記入(プロキシ環境で使用する場合) 
>"http://yourProxy:proxyPort"  
>"https://yourProxy:proxyPort" 

**STEP3：「NewsSearch.bat」をダブルクリックする。**

現在はCloudWatch・ZDNET・xtechから記事を検索し、キーワードに合致した記事のタイトルとリンクを「HybridIT.xlsx」に保存している。
