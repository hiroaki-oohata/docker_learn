## 目的
(1) [alps_value.pyの実行を DockerContainer から動作させたい。](#1-実行コマンドと結果)  
(2) [生成したDockerImageを他のPCでも使用できるようsave->loadしてみたい。](#2-実行コマンドと結果)  
(3) [DockerHubを使用してみたい。](#3-実行コマンドと結果)  

## (1) 実行コマンドと結果
本プロジェクトの使い方を、以下のログで説明する。  
順番に実行することで株式会社アルプス技研の株価の推移が表示される。  
※venv/docker-buildx.shの実行は初回のみで良い。  
```bash
hiroaki@SURPRO-8:~/e/docker_learn$ venv/docker-buildx.sh
--2024-06-22 15:33:32--  https://github.com/docker/buildx/releases/download/v0.11.1/buildx-v0.11.1.linux-amd64
Resolving github.com (github.com)... 20.27.177.113
Connecting to github.com (github.com)|20.27.177.113|:443... connected.
HTTP request sent, awaiting response... 302 Found
Location: https://objects.githubusercontent.com/github-production-release-asset-2e65be/177210627/43a036a5-40f5-4895-98a8-96306c595fb4?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=releaseassetproduction%2F20240622%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240622T063333Z&X-Amz-Expires=300&X-Amz-Signature=d5942919cb99b10aa2d5c8c6dd33eb5a252c955efa0391e2ef948decc33c9eda&X-Amz-SignedHeaders=host&actor_id=0&key_id=0&repo_id=177210627&response-content-disposition=attachment%3B%20filename%3Dbuildx-v0.11.1.linux-amd64&response-content-type=application%2Foctet-stream [following]
--2024-06-22 15:33:32--  https://objects.githubusercontent.com/github-production-release-asset-2e65be/177210627/43a036a5-40f5-4895-98a8-96306c595fb4?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=releaseassetproduction%2F20240622%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240622T063333Z&X-Amz-Expires=300&X-Amz-Signature=d5942919cb99b10aa2d5c8c6dd33eb5a252c955efa0391e2ef948decc33c9eda&X-Amz-SignedHeaders=host&actor_id=0&key_id=0&repo_id=177210627&response-content-disposition=attachment%3B%20filename%3Dbuildx-v0.11.1.linux-amd64&response-content-type=application%2Foctet-stream
Resolving objects.githubusercontent.com (objects.githubusercontent.com)... 185.199.108.133, 185.199.109.133, 185.199.111.133, ...
Connecting to objects.githubusercontent.com (objects.githubusercontent.com)|185.199.108.133|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 54452224 (52M) [application/octet-stream]
Saving to: ‘buildx-v0.11.1.linux-amd64’

buildx-v0.11.1.linux-amd64               100%[===============================================================================>]  51.93M  21.1MB/s    in 2.5s    

2024-06-22 15:33:35 (21.1 MB/s) - ‘buildx-v0.11.1.linux-amd64’ saved [54452224/54452224]

hiroaki@SURPRO-8:~/e/docker_learn$ docker build ./venv/ -t alps
[+] Building 58.4s (13/13) FINISHED                                                                                                               docker:default
 => [internal] load build definition from dockerfile                                                                                                        0.0s
 => => transferring dockerfile: 475B                                                                                                                        0.0s
 => [internal] load metadata for docker.io/library/ubuntu:20.04                                                                                             0.0s
 => [internal] load .dockerignore                                                                                                                           0.0s
 => => transferring context: 2B                                                                                                                             0.0s
 => [1/8] FROM docker.io/library/ubuntu:20.04                                                                                                               0.0s
 => [internal] load build context                                                                                                                           0.0s
 => => transferring context: 382B                                                                                                                           0.0s
 => [2/8] RUN apt update                                                                                                                                    5.7s
 => [3/8] RUN apt upgrade                                                                                                                                   1.9s
 => [4/8] RUN apt install -y python3.9                                                                                                                     12.7s 
 => [5/8] RUN apt install -y python3-pip                                                                                                                   20.7s 
 => [6/8] COPY requirements.txt .                                                                                                                           0.0s 
 => [7/8] RUN python3.9 -m pip install -r requirements.txt                                                                                                 15.8s 
 => [8/8] COPY alps_value.py .                                                                                                                              0.0s 
 => exporting to image                                                                                                                                      1.3s 
 => => exporting layers                                                                                                                                     1.3s 
 => => writing image sha256:ba156cb1c5d208cc44ed91164233fe2e04606d0701871f0eef4ffb164b722870                                                                0.0s 
 => => naming to docker.io/library/alps                                                                                                                     0.0s 
hiroaki@SURPRO-8:~/e/docker_learn$ docker images
REPOSITORY                                                                             TAG       IMAGE ID       CREATED              SIZE
alps                                                                                   latest    ba156cb1c5d2   About a minute ago   644MB
hiroaki@SURPRO-8:~/e/docker_learn$ docker run alps:latest
[*********************100%%**********************]  1 of 1 completed
              Open    High     Low   Close  Adj Close  Volume
Date                                                         
2024-06-03  2585.0  2585.0  2548.0  2557.0     2557.0   35800
2024-06-04  2553.0  2584.0  2550.0  2574.0     2574.0   21200
2024-06-05  2563.0  2578.0  2551.0  2578.0     2578.0   22300
2024-06-06  2578.0  2578.0  2540.0  2545.0     2545.0   18500
2024-06-07  2545.0  2553.0  2528.0  2532.0     2532.0   18000
2024-06-10  2532.0  2547.0  2520.0  2534.0     2534.0   19000
2024-06-11  2545.0  2546.0  2525.0  2533.0     2533.0   22100
2024-06-12  2529.0  2536.0  2510.0  2513.0     2513.0   40900
2024-06-13  2505.0  2512.0  2456.0  2456.0     2456.0   41200
2024-06-14  2446.0  2520.0  2444.0  2509.0     2509.0   46900
2024-06-17  2482.0  2491.0  2450.0  2491.0     2491.0   30900
2024-06-18  2510.0  2529.0  2503.0  2512.0     2512.0   15300
2024-06-19  2502.0  2537.0  2502.0  2537.0     2537.0   24200
2024-06-20  2536.0  2545.0  2520.0  2536.0     2536.0   47200
2024-06-21  2550.0  2560.0  2503.0  2520.0     2520.0   79000
hiroaki@SURPRO-8:~/e/docker_learn$ 
```

## (2) 実行コマンドと結果
下記のコマンドを実行すると、同階層にalps_latest.tar.gzが生成される。（名前は適当に付けて良い）  
```bash
docker save alps:latest | gzip > alps_latest.tar.gz
```
アーカイブを他のPC（WindowsPC）に保管して、他のPCでloadしてみる。  
※windowsPC側でDockerDesktop（アプリ）が起動している必要があります。
　（windowsPC側にもdockerがインストールされている必要があります。）  
```bash
docker load -i alps_latest.tar.gz
```
以下のようになればOK  
<img src="./images/windows.png" width="50%">

同じように実行すると同じ出力になります。  
```bash
docker run alps:latest
```

## (3) 実行コマンドと結果
### Ubuntu(WSL2)側の操作
Imageをpushしてリポジトリへ登録します。  
```bash
hiroaki@SURPRO-8:~$ docker images
REPOSITORY   TAG       IMAGE ID       CREATED       SIZE
alps         latest    ba156cb1c5d2   4 hours ago   644MB
hiroaki@SURPRO-8:~$ docker tag ba156cb1c5d2 hiroakioohata/alps:latest
hiroaki@SURPRO-8:~$ docker images
REPOSITORY           TAG       IMAGE ID       CREATED       SIZE
hiroakioohata/alps   latest    ba156cb1c5d2   4 hours ago   644MB
alps                 latest    ba156cb1c5d2   4 hours ago   644MB
hiroaki@SURPRO-8:~$ docker push hiroakioohata/alps:latest
The push refers to repository [docker.io/hiroakioohata/alps]
227489176006: Pushed
a2e7b85e6729: Pushed
5abadeda6c04: Pushed
c7bda4e1e64d: Pushed
5b4f42c3969f: Pushed
7aa680970fde: Pushed
d4b9cc13a959: Pushed
3ec3ded77c0c: Pushed
latest: digest: sha256:a0324694dd23c7e180a2268c4dd07507038bc074f9e84b67cc747049286bdfd6 size: 1998
hiroaki@SURPRO-8:~$
```

### リポジトリの確認
登録されていることを確認できます。  
<img src="./images/hub.png" width="75%">  

### Windows側の操作
リポジトリからpullしてインポートします。  
```bash
PS C:\> docker pull hiroakioohata/alps:latest
latest: Pulling from hiroakioohata/alps
Digest: sha256:a0324694dd23c7e180a2268c4dd07507038bc074f9e84b67cc747049286bdfd6
Status: Image is up to date for hiroakioohata/alps:latest
docker.io/hiroakioohata/alps:latest
PS C:\> docker images
REPOSITORY           TAG       IMAGE ID       CREATED       SIZE
hiroakioohata/alps   latest    ba156cb1c5d2   5 hours ago   644MB
PS C:\> docker run hiroakioohata/alps:latest
[*********************100%%**********************]  1 of 1 completed
              Open    High     Low   Close  Adj Close  Volume
Date
2024-06-03  2585.0  2585.0  2548.0  2557.0     2557.0   35800
2024-06-04  2553.0  2584.0  2550.0  2574.0     2574.0   21200
2024-06-05  2563.0  2578.0  2551.0  2578.0     2578.0   22300
2024-06-06  2578.0  2578.0  2540.0  2545.0     2545.0   18500
2024-06-07  2545.0  2553.0  2528.0  2532.0     2532.0   18000
2024-06-10  2532.0  2547.0  2520.0  2534.0     2534.0   19000
2024-06-11  2545.0  2546.0  2525.0  2533.0     2533.0   22100
2024-06-12  2529.0  2536.0  2510.0  2513.0     2513.0   40900
2024-06-13  2505.0  2512.0  2456.0  2456.0     2456.0   41200
2024-06-14  2446.0  2520.0  2444.0  2509.0     2509.0   46900
2024-06-17  2482.0  2491.0  2450.0  2491.0     2491.0   30900
2024-06-18  2510.0  2529.0  2503.0  2512.0     2512.0   15300
2024-06-19  2502.0  2537.0  2502.0  2537.0     2537.0   24200
2024-06-20  2536.0  2545.0  2520.0  2536.0     2536.0   47200
2024-06-21  2550.0  2560.0  2503.0  2520.0     2520.0   79000
PS C:\>
```

