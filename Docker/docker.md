# $docker runコマンド構成
 1. docker pull: イメージの取得
 2. docker create: コンテナの作成
 3. docker start: コンテナの起動

# 便利なイメージ群はDockerHubから参照
   - イメージは複数のレイヤーで構成されている。
   - (例)CentOs => Ruby => Rails 
# dockerの詳細情報
   - docker inspect イメージ名/id
# dockerイメージの削除
  - docker rmi イメージ名/id
     - 強制削除は -f オプション付与

# dockerイメージの取得
  - dokcer pull  イメージ名/id
