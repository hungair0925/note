$docker run hello-world
 => 1. docker pull: イメージの取得
    2. docker create: コンテナの作成
    3. docker start: コンテナの起動

便利なイメージ群 => DockerHub
イメージは複数のレイヤーで構成されている。
Rails
-----
Ruby
-----
CentOS
例.上矢印

dockerの詳細情報
docker inspect イメージ名/イメージid

dockerイメージの削除
docker rmi イメージ名/id
=> 強制削除は -f オプション付与

dockerイメージの取得
dokcer pull  イメージ名/id
