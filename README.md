# 从python学习扩展到运维
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
---
![分布式系统](images/分布式系统.png)

**本文中服务和应用是等同了，都是代表容器中运行的业务进程**

    学习docker和k8s分布式系统管理工具，能够更好的理解现代互联网大型系统的结构，从大处见真知。
    常用端口(单体应用在对外提供服务端口的时候，应该尽量避开这些常用的系统端口，以保证应用在系统中的适应性,一般至少是10000以上)
    服务名称                端口号     说明
    ftp                     21      文件上传下载
    ssh                     22      linux远程登录
    telnet                  23      win远程登录
    smtp                    25      简单邮件传输服务
    dns                     53      域名解析服务
    http                    80      web
    https                   443     加密的web
    
    mysql                   3306    mysql数据库
    PostgreSQL              5432    
    redis                   6379
    
    docker                  本地socket
    k8s         
    kube-apiserver          6443
    etcd                    2379（客户端通信）和 2380（节点间通信）
    kube-controller-manager 10252
    kube-scheduler          10251
    kubelet                 10250
    kube-proxy              10249

    随着系统的功能增加，服务会越来越多，监听的端口也会越来越多，为了系统的稳定性，一般而言会有国际惯例来约定端口资源，
    也会利用容器技术将系统进行软隔离。
    学习大型的系统，可以分析其态势，了解它们使用的框架信息，比如编程语言、日志系统、通信机制等等。

---

## 目录说明

---
    daemon  python写的守护脚本的例子
    learn   尚硅谷的python教程(去掉了ppt和pdf) https://www.bilibili.com/video/BV1eZ421b7ag/?spm_id_from=333.1007.top_right_bar_window_custom_collection.content.click&vd_source=d5fa5216fd2846a4da58ccfad53b6049
    images  README.md文件使用的图片
    k8s     docker和k8s的一些文件

---
    目录 daemon中就是一个守护脚本的例子
    
    .ipynb文件是交互式的python
    python的机器学习的体会，会清楚的明白，系统的稳定和可靠性是靠强大的数据集来训练出来的。
    一般做法不是从零开始作模型，而是通过下载一个系列的模型及它相关的写好的训练、检测的脚本，用自己的找好的数据集来进行专门的训练。
    python机器学习切忌在没有深入理解python前，就提前进入专门的大型的学习模型中去，容易受到打击而陷入迷茫。
    其实从机器学习立意开始，就奠定了尽量简单的利用已经编好的东西，包括代码、模型，来进行自己的操作。
    绝技要配合心法，否则容易受到反噬。
    
    yolov5下载---准备数据集---python训练train.py---测试detect.py---导出模型export.py---C++端进行生产环境部署opencv的dnn加载模型.onnx
## 工程组织

---
    什么是工程，基于一定的目标，利用科学知识和技术手段，借助系统的手段，将现有的数据转化为目标数据的过程。
        数据---工程化手段---数据‘
    所以手段一般不要太复杂化，尽量的用通俗的、易于理解的方式进行组织，达到能够稳定且正确的将数据进行转换即可
    
    首先讲软件的开发、交付、部署、排错、升级都是一个循环的过程，就像是事物总是会螺旋上升一样。
    1、开发到交付，存在即便是再丰富的测试、都会存在bug，为了避免因为运行环境的差异引起的程序适应性，出现了docker这种镜像工具，出现了从交付安装包到交付镜像的过程。
    2、交付到部署，存在重复性工作的特性，而面对简单重复的工作，计算机编程总是比人可靠。出现了运维工具，比如k8s(将业务以pod的形式存在，并设立若干的辅助进程来保证业务pod能够按照期望运行)
    3、部署到排错，则希望业务pod是一个矩阵，能够接收数据并将数据转化为所需数据，如数据库，并在运行过程中产生日志，所以日志和数据都会以数据卷的形式在pod中挂载到另外的k8s节点上
    同时为了将交付部署自动化，出现了jenkins。而重复类的工作呢，又出现了ansible
    4、排错到升级，从版本管理出发，合理安排业务框架、k8s节点框架。
    
    运维手段虽然在不断的更新迭代，但究其根本，还是用软件化的工具配合配置文件来完成重复性工作。
    明确了目的，就要寻找流行适合的工具。如docker k8s jenkins gitlab ansible等等
---
    **docker存在的意义**
    
    以牺牲小部分系统性能的代价，解决程序的环境适应性。而且docker compose 依然是单机微服务部署的最好选择
    是docker成就了k8s，所以这次的部署不出现最新版本的k8s，只以1.18.0(过去非常流行的旧版) 1.23.6(支持docker的较新版本)
    作为学习的开始
    
    **k8s存在的意义**
    分布式系统，以一个或者若干的控制节点，将业务pod按照期望部署到工作节点上，并使业务pod能够按照要求来运行
    微服务降低了业务系统模块间的耦合性，而分布式在降低系统宕机风险、充分利用服务器资源上有明显的架构优势。
    k8s是一个比service更大更丰富的微服务群一样，降低了单体程序员的技能要求，提高了系统的整个性能。
## 分布式相关(容器与k8s)

---
### 1、docker
    docker 安装方式参考 https://blog.csdn.net/Stromboli/article/details/142486565
    镜像地址 https://1ms.run/
    官方文档地址 https://docs.docker.com/manuals/
    docker是将单体应用进行容器化的工具，主要是3部分，CLI、Dockerfile、Docker compose。 其中：
    Dockerfile是用文件(脚本文件)的形式，将一个原始开源的基础镜像，改造成包含自己编写的应用的镜像。
    Docker compose 是用文件的形式(yaml文件)替代长串的docker镜像启动成容器的命令行
    经过Dockerfile和Docker compose后，会在系统中有容器存在，后面就可以对容器进行启动、停止、删除等操作。

    类似gitlab对比github一样，harbor对比docker hub来管理docker镜像   https://github.com/goharbor/harbor
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

### 2、k8s
    k8s的集群架构
    下面的主旨，对初期学习k8s给自己打气很重要
    学习k8s，尤其是搭建集群、建立pod的时候，会比学习docker困难，很正常的现象，
    docker是要设置好镜像地址，会写Dockerfile、docker-compose.yml文件，会定制镜像并分享出去就行了，单体应用的范围，要体会的要义少。
    k8s是集群搭建、镜像编排，确实有些费时间，遇到的问题也多，所幸这么多年的积累，能查到的资料也多，老实的按照教程，一步一步搭建好k8s的微服务组件以及与之相对应的docker版本就好
    要体会的要义多，但是和docker一样，要先理解这个是干什么的，有着怎么样的架构，微服务组件间是怎么通信工作的就好了。
    其实k8s更好的体现了，在大型的高可用系统中，从单一微服务用容器的方式实现(增加微服务的系统环境适应力)到各个微服务间的组合形成更大型的服务。
    可以体会到，容器化的微服务群，有助于系统功能的解耦、迁移。只要保证好各个微服务版本间的兼容就好了。

#### 2.1、搭建k8s集群
    k8s集群包含两部分，主控节点Master和工作节点Node
---
    kubeadm方式比较简单
    kubeadm是官方社区推出的快速部署k8s集群的工具
    1、创建master节点，kubeadm init
    2、创建node节点，kubeadm join master的ip和端口
    
    这里有两个版本的k8s
    一个对应1.18.0版本的(docker-ce~19.03.10)
    一个对应1.23.6版本的(docker-ce~20.10.18)
--- 
    软件说明:
    win上建立虚拟机软件 Vmware17.6.2
    虚拟机系统 ubuntu20.04-server
    docker 19.03.10 api:1.40 (docker --version  19.03.10)
    k8s 1.18.0 (kubelet --version Kubernetes v1.18.0)

##### 2.1.1、安装ubuntu server系统
    安装server版本的时候，如果提示更新installer，记得更新下，不然容易安装失败
    由于安装的是服务器版的，需要在安装时先把apt源换到国内aliyun的 http://mirrors.aliyun.com/ubuntu 。设置超级用户密码，安装基础软件，git、wget、curl、net-tools、ssh
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
##### 2.1.2、安装docker
    2.1、deb文件安装
    将k8s/docker文件夹下的所有deb文件安装上(文件夹文件都是从 http://mirrors.aliyun.com/docker-ce/linux/ubuntu/dists/focal/pool/stable/amd64/ 下载的)
    2.1、apt安装(**ubuntu20server 在apt安装的时候总会自动安装最高版本，所以建议deb安装**)
        # step 1: 安装必要的一些系统工具
        sudo apt-get update
        sudo apt-get -y install apt-transport-https ca-certificates curl software-properties-common
        # step 2: 安装GPG证书
        curl -fsSL https://mirrors.aliyun.com/docker-ce/linux/ubuntu/gpg | sudo apt-key add -
        # Step 3: 写入软件源信息
        sudo add-apt-repository "deb [arch=amd64] https://mirrors.aliyun.com/docker-ce/linux/ubuntu $(lsb_release -cs) stable"
        # Step 4: 更新并安装Docker-CE(指定版本的，因为docker的版本应该和k8s相适应)
        sudo apt-get -y update
        sudo apt-get -y install docker-ce=5:20.10.18~3-0~ubuntu-focal

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
    上面文件的作用有两个，一个是设置镜像拉取地址(docker hub 被墙了)；一个是设置docker的cgroup为systemd，防止后面k8s主节点初始化有问题
    其中下面的那个地址为自己的aliyun的镜像加速地址，可以替换成自己的
    sudo systemctl daemon-reload
    sudo systemctl restart docker
    此时输入 docker info 会发现生效
    sudo apt-mark hold docker
##### 2.1.3、安装k8s
    永久关闭交换
    sudo swapoff -a
    同时编辑/etc/fstab文件，将swap行注释掉
    添加k8s的安装地址
    curl -s https://mirrors.aliyun.com/kubernetes/apt/doc/apt-key.gpg | sudo apt-key add -

    在/etc/apt/sources.list.d/kubernetes.list 添加 deb https://mirrors.aliyun.com/kubernetes/apt/ kubernetes-xenial main

    sudo apt update
    1.18.0版本
    sudo apt install -y kubelet=1.18.0-00 kubeadm=1.18.0-00 kubectl=1.18.0-00
    或者 1.23.6版本 
    sudo apt install -y kubelet=1.23.6-00 kubeadm=1.23.6-00 kubectl=1.23.6-00

    sudo apt-mark hold kubelet kubeadm kubectl (标记一个包为held back状态，阻止该包自动安装、更新和删除)
    添加命令补全
    在 /etc/bash.bashrc文件中最后一行添加
    source <(kubectl completion bash)
    保存后， source /etc/bash.bashrc
    **在master和node节点，分别设置hostname！！！**
    sudo hostnamectl set-hostname k8s-master
    sudo hostnamectl set-hostname k8s-node1

##### 2.1.4、在master节点上进行初始化操作
        kubeadm init \
      --apiserver-advertise-address=192.168.127.250 \
      --image-repository registry.aliyuncs.com/google_containers \
      --kubernetes-version v1.18.0 \
      --service-cidr=10.96.0.0/12 \
      --pod-network-cidr=10.244.0.0/16
    
        kubeadm init \
      --apiserver-advertise-address=192.168.127.150 \
      --image-repository registry.aliyuncs.com/google_containers \
      --kubernetes-version v1.23.6 \
      --service-cidr=10.96.0.0/12 \
      --pod-network-cidr=10.244.0.0/16

    执行成功后，在master中执行docker images 会有
![k8s-master](images/k8s-master.png)

    默认token有效期为24小时，当过期之后，该token就不可用了。这时就需要重新创建token(永久期限)，操作如下：
    kubeadm token create --print-join-command --ttl=0

    使用kubectl工具：
    mkdir -p $HOME/.kube
    sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
    sudo chown $(id -u):$(id -g) $HOME/.kube/config

##### 2.1.5、在node节点上加入master
    kubeadm join 192.168.127.250:6443 --token qwfasm.n7hx820fmlu1cqnw \
        --discovery-token-ca-cert-hash sha256:9d7c74156cbfeee22bfd402a115ba3bb3ce82bd9d73e382f32414296d03bcf60

    如果忘记上面的，可以再master上执行
    kubeadm token create 没有加参数时，可以通过下面的命令查看加入要写的参数值
    kubeadm token list 查看token，得到值后，输入
    openssl x509 -pubkey -in /etc/kubernetes/pki/ca.crt | openssl rsa -pubin -outform der 2>/dev/null | openssl dgst -sha256 -hex | sed 's/^.* //'
    

##### 2.1.6、master部署 CNI
    **无论哪个都是要和k8s的版本做适应的，推荐使用calico**

    ---使用 kubectl 部署 flannel
    wget https://raw.githubusercontent.com/coreos/flannel/master/Documentation/kube-flannel.yml
    kubectl apply -f kube-flannel.yml
    ---使用kubectl 部署 calico.yaml
    calico和k8s版本也有对应的关系 具体可以在https://github.com/projectcalico/calico/releases 一个一个查看说明
    k8s-1.18.0(calico-3.14.2)
    k8s-1.23.6(calico-3.25.0)
    
    这里有个小知识，一个整个的yaml其实很庞大，
    一般就需要注意两个方面，一个是apiVersion，一个是image。可以使用命令
    grep xxx yyy.yaml 来过滤信息查看

    kubectl get nodes

##### 2.1.7、测试
    在master上执行
    kubectl create deployment nginx --image=nginx
    kubectl expose deployment nginx --port=80 --type=NodePort
    kubectl get pod,svc -o wide (以后尽量加 -o wide可以看到运行的节点)

    此时就可以在master和node的任意的ip 加上容器内80映射到节点的端口号来访问nginx了    
    
    测试完毕，删除 nginx
    kubectl delete deployment nginx
    kubectl delete service nginx

##### 2.1的总结
    以上步骤主要参考 https://blog.csdn.net/weixin_60197334/article/details/136735056
    
    由于使用apiserver来做整体的操作入口，所以存在下面两点注意
    1、k8s版本与docker版本相适应
    2、插件必须与k8s的版本相适应，并且要查看插件的yaml文件中的image地址是否被墙，可以使用docker pull下载下试试
    
    在k8s和docker安装完毕后，从4步开始 所有操作有问题后，都有一个类型重启k8s环境的操作
    sudo kubeadm reset -f

    如果想在node节点执行kubectl的命令，由于api-server是运行在master节点上的，所以需要让node节点知道这个命令是向谁请求
    

#### 2.2、k8s中各个组件
    理解组件可以从k8s的结构和微服务组合角度来看
    
    在master上输入(kubectl get pod -n kube-system -o wide)可以看到
    ---master上有 
    kube-apiserver (集群的统一入口，以restful方式，交给etcd存储,后续的能否执行成功和它的api版本很相关)
    kube-controller-manager (控制器管理，管理各种类型的控制器，对k8s中的各种资源进行管理)
    cloud-controller-manager (云控制器管理器，第三方云平台提供的控制器API对接管理平台)
    kube-scheduler (调度器，负责将Pod基于一定的算法(资源要求、亲和性等)，将其调用到更合适的节点(服务器)上)
    etcd (键值类型的分布式存储系统，用于保存集群相关的数据，类似k8s的数据库)
    container runtime (docker 容器化工具)

    ---node上有(一般不用特别关注)
    kubelet (主控节点派到工作节点的代表，负责Pod的声明周期、存储、网络)
    kube-proxy (提供网络代理，负载均衡等操作，4层负载)
    container runtime (docker 容器化工具)
    
    ---还有一些附加组件如 ingress dashboard等

    k8s节点内组件关系图
![k8s](images/k8s.png)

#### 2.3、k8s命令行工具 kubectl

---
    https://kubernetes.io/zh-cn/docs/reference/kubectl/
    弃用api的说明 https://kubernetes.io/zh-cn/docs/reference/using-api/deprecation-guide/

    语法格式
    kubectl [command] [TYPE] [NAME] [flags]

    command:对资源进行的操作
    TYPE:资源类型 大小写敏感
    NAME:资源名称 大小写敏感，
    flags:可选参数 大小写敏感

    **与kubectl命令行工具相对的，有一些web类型的可视化界面(注意k8s版本适配)**，如
    Dashboard(https://github.com/kubernetes/dashboard)
    kuBoard(https://www.kuboard.cn/)

    kubectl 是通过yaml文件形成http请求，向restful api风格接口的ApiServer发送请求
    (apiVersion 可以通过 kubectl api-versions查询，kind 可以通过 kubectl api-resources查询)


##### 2.3.1、资源管理和编排部署的文件(yaml)

    **一个yaml文件是存在master上的，是一个部署相关的资源清单，
    可以在ide中通过ssh和sftp的功能拉到本地编辑再同步到服务器
    同时在ide中添加k8s的插件，方便文件编写**
    其实k8s的资源和对象，可以理解为编程语言中的类和对象，
    类比 k8s和go
    k8s         go
    资源清单     很多结构体
    资源          结构体
    对象          实例
    只不过k8s因为基于特定的任务出现的(ApiSever版本)，所以它的资源要分成若干功能，
    而编程语言的go的结构体，就可以根据自己的理解做很多类型的
    k8s的资源编排就是编辑若干的类型对象，调用ApiServer来生成各种实例，完成任务
    go的工程就是根据go提供的数据类型和函数体，来组合成结构体，生成各种实例，完成任务
    可编程的本质，就是调用环境的api，来完成特定任务。

    通过kubectl命令使用资源编排文件来对大量的资源对象进行编排部署

    资源编排yaml文件要记住很痛苦，可以使用 kubectl (help、explain、create --dry-run -o yaml)来帮助自己生成
    也可以IDE中搜索kubernetes拉安装插件
    
    yaml语法格式，2空格表示缩进关系的；冒号或者逗号加1个空格；#表示注释；---表示一个新的文件开始
    
    **一般编排文件的组成部分(再2.5 2.6章节有具体的说明，在练习中学习)**：
    以template为分割的
    
    ---资源定义
    
    apiVersion      API版本 kubectl api-versions
    kind            资源类型 kubectl api-resources
    metadata        资源元数据 
    spec            资源规格(期望状态)
      replicas      副本数量
      selector      标签选择器
    
    ---被控制对象
    
    template        Pod模板
    metadata        Pod元数据
    spec            Pod规格
    containers      容器配置
    
    **由于从零开始手写yaml文件很困难，可以使用特殊的方式来生成资源编排文件: 从新生成 kubectl create 生成;从已部署好的中获取 kubectl get**
    
    --- 从新生成 kubectl create (生成模板)
    
    kubectl create deployment web --image=nginx -o yaml --dry-run > xxx.yaml （xxx为自定义名称）
    
    ---从已有导出 kubectl get
    
    kubectl get deploy xxx -o=yaml --export > yyy.yaml (xxx为已存在的编排，yyy为自定义名称)

#### 2.4、Helm

https://helm.sh/zh/
helm的版本应该和k8s的版本相适应 详见 https://helm.sh/zh/docs/topics/version_skew/
安装参考 https://helm.sh/zh/docs/intro/install/
在 https://github.com/helm/helm/releases/tag/v3.10.0 下载 linux/amd64版本的安装包
将压缩包解压后，将执行文件拷贝到/usr/local/bin目录下


版本 3.10.2(k8s-1.23.6)
版本 3.0.0(k8s-1.18.0)

添加chart仓库
helm repo add bitnami https://charts.bitnami.com/bitnami
helm repo add stable http://mirror.azure.cn/kubernetes/charts
helm repo add aliyun https://kubernetes.oss-cn-hangzhou.aliyuncs.com/charts
helm repo update
搜索可用的
helm search repo xxx (xxx为包名)


#### 2.5、资源类型

---
    七大类:负载、服务、存储、配置、安全、策略、调度
    都是有两部分内容 属性(metadata)/期望(spec) <apiVersion和Kind 可以通过kubectl api-resources 查看>
    属性是定义资源的，可以用于显示(name)、被筛选(labels)、命名空间(namespaces)
    期望是描述调度器和控制器应该怎么做的，用来筛选(selector)、template(模板)、副本、重启策略、探针等等，类型不一样，支持的内容不一样。
    **下面的分节，是对常用资源的元素的说明，包括说明、常用创建命令、元素说明**
    视频学习可以参考 叩丁狼的B站视频 https://www.bilibili.com/video/BV1MT411x7GH 
    通过kubectl api-resources 得到的APIVERSION KIND的信息分类
    k8s用的程序的深浅就是在下面这些资源类型的使用程序
    在 https://kubernetes.io/zh-cn/docs/concepts/ 下
    它们分为 7类，必须掌握的是负载、服务、存储、配置(涉及了服务的生命周期管理、对外服务暴露、数据存放、配置相关，都是紧紧要的)。
    其他的慢慢来，其实后面的多多少少不是独立存在的，需要嵌套写入到前面4项中。
    1、负载 Pod、Deployment、StatefulSet、DaemonSet、Job、CronJob
    2、服务 Service、Ingress
    3、存储 Volume Pod
    4、配置 ConfigMap、Secret、探针
    5、安全 ServiceAccount RBAC(基于角色的访问控制)
    6、策略 LimitRange 
    7、调度 Pod Label/Selector 污点/亲和性

    在k8s/xxx(版本号(主要是1.23.6))/yaml/文件夹下是对资源类型学习的yaml-demo(这里可以根据自身角色的定位进行有选择的学习k8s，比如开发的深度就没有运维的高)
    workloads
        ├─pods              ---Pod(无法动态更改的工作负载)
        ├─deployment        ---Deployment
        ├─statefulset       ---StatefulSet
        ├─daemonset         ---DaemonSet     
        └─jobs              ---Job/CronJob


#### 2.5.1、工作负载 Pod/Deployment/StatefulSet/DaemonSet/Job/CronJob

    ---1、无状态服务：认为Pod都是相同的，没有顺序要求，不用考虑在哪个node上运行，随意进行伸缩和扩展
    ---2、有状态服务：Pod是不一样的，有顺序要求，考虑在哪个node上运行，不可随意伸缩扩展；每个Pod独立，保持Pod的启动顺序和唯一性
    ---3、守护进程:DaemonSet
    ---4、任务:一次性任务Job、定时任务CronJob

    根据要控制的服务的特点,分为四大类:适用无状态服务、适用有状态服务、守护进程、任务/定时任务
    包括:
    无状态服务
    ReplicationController(RC) （从1.11后就废除了）控制Pod扩容/缩容
    ReplicaSet(RS) (基于label和selector的机制，替代了RC的绑定，淘汰了RC，也不常用)控制Pod扩容/缩容
    Deployment (**最常用的**，对RS再次升级)提供更丰富的部署，控制Pod扩容、缩容、滚动升级/回退
    
    有状态服务
    StatefulSet 部署有状态应用，结合Service、存储等实现对有状态应用部署
    守护进程
    DaemonSet 守护进程集，运行在所有集群节点(包括master), 比如使用filebeat,node_exporter
    任务/定时任务
    Job 一次性
    Cronjob 周期性

    HPA 自动扩容缩容 https://kubernetes.io/zh-cn/docs/concepts/workloads/autoscaling/

##### 2.5.1.1、Pod

---
    https://kubernetes.io/zh-cn/docs/concepts/workloads/pods/
    图示创建Pod的过程
![createPod](images/createPod.png)

    **说明**
        1、基本概念：
        最小的部署单元；Pod里面是一组容器的组合；一个Pod中的容器共享网络命名空间；pod是短暂存在的
        2、存在的意义：
        一个容器，运行一个应用程序，是一个进程；Pod是多进程设计(1个pause根容器和用户容器)；亲密性应用(应用间的通信)
        3、实现机制：
        共享网络,通过pause容器把其他的业务容器加入到同一命名空间中。
        共享存储，持久化存储Volume数据卷
        4、重启策略决定容器挂掉后该怎么操作，而探针来实现获取容器是否存在(https://kubernetes.io/zh-cn/docs/concepts/configuration/liveness-readiness-startup-probes/)
        spec.template.spec.restartPolicy
        spec.template.spec.containers[].xxxProbe
        livenessProbe 存活探针
        readinessProbe 就绪探针
        startupProbe 启动探针
    **常用创建命令**
        kubectl xxx pod (xxx 表示操作类型，一般创建就是手写 delete set describe)
    **元素说明**
        详见 k8s/xxx/yaml/workfloads/pod

**但是因为原生Pod的扩容/升级很不方便，所以出现了按业务类型分类管理的Deployment/StatefulSet/DaemonSet/Job/CronJob**

##### 2.5.1.2、Deployment

---
    https://kubernetes.io/zh-cn/docs/concepts/workloads/controllers/deployment/
    **说明**
        最常用的部署无状态服务的资源
        通过label和selector标签来建立Pod和Controller的关联关系
        部署、暂停/恢复、扩容/缩容、滚动升级/回归等
        应用场景 web服务 微服务
    **常用创建命令**
        kubectl xxx deployment (xxx 表示操作类型，create delete set describe)
    **元素说明**
        详见 k8s/xxx/yaml/workfloads/deployment

##### 2.5.1.3、StatefulSet

---
    https://kubernetes.io/zh-cn/docs/concepts/workloads/controllers/statefulset/
    **说明**
        部署有状态应用，部署、暂停/恢复、扩容/缩容、滚动升级/回归等
        Headless Service DNS管理(网络)
        volumeClaimTemplates 持久化卷(存储)
        
        灰度发布/金丝雀发布 目的是将项目上线后产生问题的影响，尽量降到最低。
        做法就是先更新整个副本的一小部分，如果确认没问题，就更新全部，有问题，就回滚这一小部分。
        利用 spec.updateStrategy.rollingUpdate.partition字段进行分区更新(倒序的顺序)       

        更新策略有OnDelete 当删除时才进行更新(可以达到更新指定的pod)

    **常用创建命令**
        kubectl xxx std (xxx 表示操作类型，一般用文件创建 delete set describe)
    **元素说明**
        详见 k8s/xxx/yaml/workfloads/statefulset

##### 2.5.1.4、DaemonSet

---
    https://kubernetes.io/zh-cn/docs/concepts/workloads/controllers/daemonset/
    **说明**
    守护进程，每个节点最多一个。
    场景:日志收集组件fluentd,搜集日志，将日志发送到指定节点。
    按节点进行部署。spec.template.spec.nodeSelector
    命令行  kubectl label no xxx(node的hostname) 向节点添加label

    **常用创建命令**
    **元素说明**

##### 2.5.1.5、Job

---
    https://kubernetes.io/zh-cn/docs/concepts/workloads/controllers/job/
    **说明**
    一次性任务
    **常用创建命令**
    **元素说明**

##### 2.5.1.6、CronJob

---
    https://kubernetes.io/zh-cn/docs/concepts/workloads/controllers/cron-jobs/
    **说明**
    周期性任务
    **常用创建命令**
    **元素说明**

#### 2.5.2、网络服务、负载均衡 Service/Ingress

    Service是容器内部通信
    Ingress是容器对外提供服务

##### 2.5.2.1、Service

---
    https://kubernetes.io/zh-cn/docs/concepts/services-networking/service/
    **说明**
    东西流量，实现k8s集群内部网络调用、负载均衡(四层负载)
    **常用创建命令**
    **元素说明**

##### 2.5.2.1、Ingress

---
    https://kubernetes.io/zh-cn/docs/concepts/services-networking/ingress/
    **说明**
    南北流量，将k8s内部的服务暴露给外网访问(七层负载)
    **常用创建命令**
    **元素说明**

#### 2.5.3、存储(Volume)

---
    https://kubernetes.io/zh-cn/docs/concepts/storage/volumes/
    **说明**
    数据存储卷
    **常用创建命令**
    **元素说明**

#### 2.5.4、配置(ConfigMap)

---
    https://kubernetes.io/zh-cn/docs/concepts/configuration/configmap/
    **说明**
    KV类型的配置信息
    **常用创建命令**
    **元素说明**

#### 2.5.5、安全(Secret)

---
    https://kubernetes.io/zh-cn/docs/concepts/configuration/secret/
    **说明**
    用加密数据存储配置信息
    **常用创建命令**
    **元素说明**

#### 2.5.6、策略(LimitRange/NetworkPolicy/ResourceQuota)

---
    https://kubernetes.io/zh-cn/docs/concepts/policy/
    **说明**
    用加密数据存储配置信息
    **常用创建命令**
    **元素说明**
