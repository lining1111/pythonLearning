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

docker 安装方式参考 https://blog.csdn.net/Stromboli/article/details/142486565
    镜像地址 https://1ms.run/
    官方文档地址 https://docs.docker.com/manuals/

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

    








