# microk8s学習用ファイルセット
## Copyright
Copyright (C) RC30-popo

## Overview
microk8sを使ってkubernetesのservice,deployment,replicaset,pod及びingress-controllerの動作確認をするためのサンプル定義ファイル等です。

kubernetesの初心者向けの記事ではnginxをpodとして起動することが定番ですが、python3+flaskでシンプルなアプリを作り、クライアントやHTTPヘッダ情報をHTTP responseとして返すことでpodの内側からクライアントIPやHTTP requestがどう見えるを確認出来る様にしています。

# 本セットに含まれるファイル
## サンプルアプリ
### hello.py
python3 + flaskで動作するhello worldアプリにクライアントIPやHTTPヘッダの表示機能を追加したものです。
### Dockerfile
上記hello.pyを起動するためのDockerイメージを作成するためのDockerfileです。
Ubuntu 18.04をベースにイメージをbuildします。

## Service,Deployment,Replicaset,Podの定義ファイル
### svc-flaskhello.yaml
一番基本的なClusterIPモードで上記のhello.pyをpod内で起動する定義です。
replica数2でpodを起動しflask-helloと名称でserviceを起動します。

Clusterネットワーク内から「flask-hello.default.svc.cluster.local」というFQDNでserviceを検索出来る様になります。

### svc-nodeport-flaskhello.yaml
上記のflask-hello serviceをType:NodePortで起動する定義ファイルです。

### svc-nodeport2-flaskhello.yaml
同じくNodePort serviceの定義ですが、クライアントIPでSticky sessionを実現する例です。

## Ingress Controllerの定義ファイル
nginx ingress controllerの定義ファイル例です。
### ingress-flaskhello.yaml
ノードのport80、パス/flask-helloでflask-hello serviceにアクセスを可能とするIngress Controllerの定義です。
svc-flaskhello.yamlでClusterIPモードで起動したserviceと組み合わせて使用してください。
### ingress-flaskhello-ss.yaml
上記にcookieベースのSticky sessionを追加した例です。

# 本ファイルセットの使用例
以下のブログエントリーで紹介しています。
https://rc30-popo.hatenablog.com/entry/2021/05/16/173136
https://rc30-popo.hatenablog.com/entry/2021/05/30/223723
https://rc30-popo.hatenablog.com/entry/2021/12/25/233311
https://rc30-popo.hatenablog.com/entry/2022/01/02/164504
https://rc30-popo.hatenablog.com/entry/2022/01/09/234105

