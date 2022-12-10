# docker-ComWechat
[![docker 镜像](https://dockeri.co/image/tomsnow1999/docker-com_wechat_robot)](https://hub.docker.com/r/tomsnow1999/docker-com_wechat_robot/tags)

[![镜像大小](https://badgen.net/docker/size/tomsnow1999/docker-com_wechat_robot)](https://hub.docker.com/r/tomsnow1999/docker-com_wechat_robot/tags)

A docker image for [ComWeChatRobot](https://github.com/ljc545w/ComWeChatRobot)


``` shell
docker run \
    --name comwechat  \
    --network host \
    -e VNCPASS=asdfgh123 \
    -e COMWECHAT=https://github.com/ljc545w/ComWeChatRobot/releases/download/3.7.0.30-0.0.5/3.7.0.30-0.0.5.zip \
    -dti  \
    --ipc=host \
    --privileged \
    -v $(pwd)/volume/WeChat\ Files/:'/home/user/.wine/drive_c/users/user/My Documents/WeChat Files/'  \
    -v $(pwd)/volume/Application\ Data:'/home/user/.wine/drive_c/users/user/Application Data/' \
    tomsnow1999/docker-com_wechat_robot
```

### 参数说明
* 端口 5905: VNC 服务的端口(无法/无需修改)
* network host: 使用宿主机网络(在 Linux Docker 环境下使用)
* 环境变量 VNCPASS: 连接 VNC 的密码（可自定义，建议在服务器上使用本镜像的话设置得难一点）
* 环境变量 COMWECHAT: [ComWeChatRobot](https://github.com/ljc545w/ComWeChatRobot/releases)具体版本的动态库文件压缩包(右键复制发布的文件的下载链接)【不设置此参数则默认为`3.7.0.30-0.0.5`的链接】
* 目录映射 `WeChat Files`: 微信收到的图片/文件存储的目录(可以取消目录映射)
* 目录映射 `Application Data`: 微信数据目录(可以取消目录映射)

## 如何使用
1. 运行上方命令启动镜像(更推荐使用 [docker-compose](./docker-compose.yaml) )
2. 连接上 VNC 扫码登陆微信(建议扫码登陆后把微信的版本号弹窗等关闭)
3. 使用 python 与微信通信(示例文件 [test.py](./test.py) )


## 鸣谢
[ljc545w/ComWeChatRobot](https://github.com/ljc545w/ComWeChatRobot): ComWeChatRobot 项目本体

[0honus0/ComWeChat_Inject](https://github.com/0honus0/ComWeChat_Inject): 本镜像所使用的注入器

## 相关项目
[efb-wechat-comwechat-slave](https://github.com/0honus0/efb-wechat-comwechat-slave): 使用 Telegram 来接收&管理微信消息

## 声明
**本项目仅供学习研究，强烈反对商业用途或者滥用(通过程序化控制微信对其他人进行骚扰诈骗等)！使用本项目造成的一切责任与本人无关，一切责任由使用者自行承担！**
