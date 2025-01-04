# 自己写的一些有用的python脚本
    由于shell脚本的不可调试以及这种情况的假设：
    简单的程序加入系统，在系统不是标准的情况下，使用init文件；系统标准的情况下，可以通过linux系统的systemd,做一个service文件来启动服务
    复杂的程序，可以使用编写脚本如shell(win上为bat)来模拟系统逐步启动程序，并对程序的状态进行监控。
    但是脚本如shell或者bat，不能进行调试，对于编写者的能力是巨大的挑战，尤其是在一些不可恢复操作上。这种时候就需要python来充替脚本的角色了，
    同时python还兼具编程的特色。
    从历史的角度看待编程世界：
        第一代语言 二进制bin，计算机直接识别并执行的
        第二代语言 汇编,稍微扩展了可读性
        第三代语言       shell(1970)
                        c(1972)
                        sql(1974)
                        c++(1979)
                        HTML(1990)
                        python(1991)
                        css(1994)
                        java(1995)
                        javascript(1995)
                        go(2007)
                        docker(2013)
                        k8s(2014)
    上面的第三代语言列举了本人常用编程语言的生日，每种语言的出现都有特定的时代背景和它擅长解决的问题，借鉴已存在的编程语言的优点，并与之兼容。
    编程语言的强大依赖出生时的好爹，强大的公司背景或者个人实力，这是天赋；同样依赖后天的发育环境，比如开源带来的集思广益。
    选择编程语言就是选择工具，同时在人工智能的冲击下，基础的编程技巧显得乏力，且不具备时间竞争力，复合编程能力，系统的架构组织能力才具备时间竞争力。
![分布式系统](images/分布式系统.png)

目录 daemon中就是一个守护脚本的例子

.ipynb文件是交互式的python
python的机器学习的体会，会清楚的明白，系统的稳定和可靠性是靠强大的数据集来训练出来的。
一般做法不是从零开始作模型，而是通过下载一个系列的模型及它相关的写好的训练、检测的脚本，用自己的找好的数据集来进行专门的训练。
python机器学习切忌在没有深入理解python前，就提前进入专门的大型的学习模型中去，容易受到打击而陷入迷茫。
其实从机器学习立意开始，就奠定了尽量简单的利用已经编好的东西，包括代码、模型，来进行自己的操作。
绝技要配合心法，否则容易受到反噬。

yolov5下载---准备数据集---python训练train.py---测试detect.py---导出模型export.py---C++端进行生产环境部署opencv的dnn加载模型.onnx

## 跟着尚硅谷学python
    目录 learn中就是根据尚硅谷的python教程(去掉了ppt和pdf)
    b站地址 https://www.bilibili.com/video/BV1eZ421b7ag/?spm_id_from=333.1007.top_right_bar_window_custom_collection.content.click&vd_source=d5fa5216fd2846a4da58ccfad53b6049
    通过视频去了解python的基本情况，达到能看懂简单python文件的程度。

## 工程组织

什么是工程，基于一定的目标，利用科学知识和技术手段，借助系统的手段，将现有的数据转化为目标数据的过程。
    数据---工程化手段---数据‘
所以手段一般不要太复杂化，尽量的用通俗的、易于理解的方式进行组织，达到能够稳定且正确的将数据进行转换即可

### docker

docker 安装方式参考 https://blog.csdn.net/Stromboli/article/details/142486565
    镜像地址 https://1ms.run/
    官方文档地址 https://docs.docker.com/manuals/
    docker是将单体应用进行容器化的工具，主要是3部分，CLI、Dockerfile、Docker compose。 其中：
    Dockerfile是用文件(脚本文件)的形式，将一个原始开源的基础镜像，改造成包含自己编写的应用的镜像。
    Docker compose 是用文件的形式(yaml文件)替代长串的docker镜像启动成容器的命令行
    经过Dockerfile和Docker compose后，会在系统中有容器存在，后面就可以对容器进行启动、停止、删除等操作。

#### Dockerfile
    可以用docker的方式将单一容器内的服务进行组织，编写成一个自己的镜像
    1、用Dockerfile，拉取单个基础镜像如 ubuntu (一般ubuntu的默认apt源是国外的，需要将本地的apt源替换掉镜像的： COPY /etc/apt/sources.list /etc/apt )
    2、将本地的应用程序拷贝到基础镜像内
    3、将镜像内的应用的基础依赖如库、环境变量设置好
    4、用EXPOSE、VOLUME等关键词标注下
    5、设置程序的自启动，如CMD (CMD ["executable","param1","param2"]),或者systemd的服务

    下面是一个简单的Dockerfile文件写法
    FROM ubuntu:latest
    LABEL authors="lining"
    COPY /etc/apt/sources.list /etc/apt
    COPY ./app /app/
    EXPOSE 10001
    VOLUME ["/app/log/"]
    CMD ["executable","param1","param2"]

#### docker compose
    docker compose 可以运行多个容器。默认是compose.yml，语法也比较简单，可以参考 https://www.cnblogs.com/minseo/p/11548177.html
    官方文档地址 https://docs.docker.com/reference/compose-file/
    顶级元素有：
    name        名字
    services    服务
    networks    网络
    volumes     卷
    configs     配置
    secrets     密钥
    以下是一个模板
    version: '3'
    services:
      web:
        image: dockercloud/hello-world
        ports:
          - 8080
        networks:
          - front-tier
          - back-tier
    
      redis:
        image: redis
        links:
          - web
        networks:
          - back-tier
    
      lb:
        image: dockercloud/haproxy
        ports:
          - 80:80
        links:
          - web
        networks:
          - front-tier
          - back-tier
        volumes:
          - /var/run/docker.sock:/var/run/docker.sock 
    
    networks:
      front-tier:
        driver: bridge
      back-tier:
        driver: bridge

    
### k8s
k8s的集群架构
下面的主旨，对初期学习k8s给自己打气很重要
学习k8s，尤其是搭建集群、建立pod的时候，会比学习docker困难，很正常的现象，
docker是要设置好镜像地址，会写Dockerfile、docker-compose.yml文件，会定制镜像并分享出去就行了，单体应用的范围，要体会的要义少。
k8s是集群搭建、镜像编排，确实有些费时间，遇到的问题也多，所幸这么多年的积累，能查到的资料也多，老实的按照教程，一步一步搭建好k8s的微服务组件以及与之相对应的docker版本就好
要体会的要义多，但是和docker一样，要先理解这个是干什么的，有着怎么样的架构，微服务组件间是怎么通信工作的就好了。
其实k8s更好的体现了，在大型的高可用系统中，从单一微服务用容器的方式实现(增加微服务的系统环境适应力)到各个微服务间的组合形成更大型的服务。
可以体会到，容器化的微服务群，有助于系统功能的解耦、迁移。只要保证好各个微服务版本间的兼容就好了。
![k8s](images/k8s.png)
从上图可以看出，k8s集群包含两部分，主控节点Master和工作节点Node

#### 主控节点Master
主要有的组件是
**APIserver**
    集群的统一入口，以restful方式，交给etcd存储
**scheduler**
    节点调度，选择node节点，进行应用部署
**controller-manager**
    处理集群中常规的后台任务，一个资源对应一个控制器
**etcd**
    存储系统，用于保存集群相关的数据

#### 工作节点Node
主要有的组件是
**docker**
    容器化工具
**kubelet**
    主控节点派到工作节点的代表，管理本机容器
**kube-proxy**
    提供网络代理，负载均衡等操作

#### k8s核心概念
通过Service统一入口进行访问，由controller创建Pod进行部署
**Pod**
    最小的部署单元
    一组容器的集合
    里面的容器是共享网络的
    声明周期是短暂的

**controller**
    确保预期的Pod的副本数量
    无状态应用部署
    有状态应用部署(有特定条件才能使用，比如存储、网络ip等)
    确保所有的node运行同一个Pod
    一次性任务和定时任务
**Service**
    定义一组Pod的访问规则
    

#### 搭建k8s集群
两种方式kubeadm和二进制包

##### kubeadm方式比较简单
kubeadm是官方社区推出的快速部署k8s集群的工具
1、创建master节点，kubeadm init
2、创建node节点，kubeadm join master的ip和端口

win上建立虚拟机软件Vmware17.6.2
虚拟机系统 ubuntu20.04-server
docker 24.0.7 api:1.43 (docker --version  24.0.7-0ubuntu2~20.04.1)
k8s 1.23.5 (kubelet --version Kubernetes v1.23.5)
0、安装server版本的时候，如果提示更新installer，记得更新下，不然容易安装失败
1、由于安装的是服务器版的，需要在安装时先把apt源换到国内aliyun的 http://mirrors.aliyun.com/ubuntu 。设置超级用户密码，安装基础软件，git、wget、curl、net-tools、ssh
sudo passwd
sudo apt update
sudo apt install git wget curl net-tools ssh ca-certificates software-properties-common apt-transport-https
    编辑 /etc/netplan/xxx.yaml文件设置静态ip
    下面是例子(注意缩进关系)
      network:
      ethernets:
        ens33:
          dhcp4: false
          addresses: [192.168.127.250/24]
          gateway4: 192.168.127.2
          nameservers:
            addresses: [8.8.8.8]
  version: 2
2、安装docker
    sudo apt install -y docker.io
    二进制安装 下载地址 https://mirrors.aliyun.com/docker-ce/linux/ubuntu/dists/focal/pool/stable/amd64/?spm=a2c6h.25603864.0.0.2be77ed5imBeND
    将当前用户添加到docker组
    sudo usermod -aG docker $USER（替换$USER为你的用户名）
    重启系统使上面添加docker用户的行为生效
    输入 docker version 不再出现错误 unix /var/run/docker.sock: connect: permission denied
    由于docker hub 被墙的原因，将docker镜像源替换到国内的"https://docker.1ms.run" 就很好
    新建 /etc/docker/daemon.json 将下面的内容添加到文件内
    {
        "registry-mirrors": [
            "https://docker.1ms.run",
            "https://d4s22q5s.mirror.aliyuncs.com"
        ],
        "exec-opts": ["native.cgroupdriver=systemd"]
    }
    其中下面的那个地址为自己的aliyun的镜像加速地址，可以替换成自己的
    sudo systemctl daemon-reload
    sudo systemctl restart docker
    此时输入 docker info 会发现生效
    sudo apt-mark hold docker
3、安装k8s
    永久关闭交换
    
    curl -s https://mirrors.aliyun.com/kubernetes/apt/doc/apt-key.gpg | sudo apt-key add -
    sudo tee /etc/apt/sources.list.d/kubernetes.list <<EOF 
deb https://mirrors.aliyun.com/kubernetes/apt/ kubernetes-xenial main
EOF
    sudo apt update
    sudo apt install -y kubelet=1.23.5-00 kubeadm=1.23.5-00 kubectl=1.23.5-00
    sudo apt-mark hold kubelet kubeadm kubectl (标记一个包为held back状态，阻止该包自动安装、更新和删除)
4、在master节点上进行初始化操作
    kubeadm init \
  --apiserver-advertise-address=192.168.127.250 \
  --image-repository registry.aliyuncs.com/google_containers \
  --kubernetes-version v1.23.5 \
  --service-cidr=10.96.0.0/12 \
  --pod-network-cidr=10.244.0.0/16

    cat >> /etc/hosts << EOF
192.168.127.250 k8s-master
192.168.127.251 k8s-node1
192.168.127.252 k8s-node2
EOF

    默认token有效期为24小时，当过期之后，该token就不可用了。这时就需要重新创建token(永久期限)，操作如下：
    kubeadm token create --print-join-command --ttl=0

使用kubectl工具：
mkdir -p $HOME/.kube
sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
sudo chown $(id -u):$(id -g) $HOME/.kube/config

5、在node节点上加入master
kubeadm join 192.168.127.250:6443 --token qwfasm.n7hx820fmlu1cqnw \
        --discovery-token-ca-cert-hash sha256:9d7c74156cbfeee22bfd402a115ba3bb3ce82bd9d73e382f32414296d03bcf60

6、部署 CNI
使用 kubectl 部署 flannel 。
vim /etc/hosts/
加入 185.199.110.133 raw.githubusercontent.com 否则下载 kube-flannel.yml 会失败
 #下载 kube-flannel.yml 
wget https://raw.githubusercontent.com/coreos/flannel/master/Documentation/kube-flannel.yml

kubectl apply -f kube-flannel.yml
kubectl get nodes

7、测试
在master上执行
kubectl create deployment nginx --image=nginx
kubectl expose deployment nginx --port=80 --type=NodePort
kubectl get pod,svc

kubectl get pod -o wide可以看到是运行在哪个节点

测试完毕，删除 nginx
kubectl delete deployment nginx
kubectl delete service nginx

以上步骤主要参考 https://blog.csdn.net/weixin_60197334/article/details/136735056

在k8s和docker安装完毕后，从4步开始 所有操作有问题后，都有一个类型重启k8s环境的操作
sudo kubeadm reset -f

##### 二进制包方式比较复杂，但是可以学习到各个组件的关系
由于kubeadm的方式比较好用，这部分就按照教程，学习组件关系，不再进行二进制的安装操作。



