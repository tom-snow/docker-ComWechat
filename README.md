# docker-ComWechat
[![docker 镜像](https://dockeri.co/image/tomsnow1999/docker-com_wechat_robot)](https://hub.docker.com/r/tomsnow1999/docker-com_wechat_robot/tags)

[![镜像大小](https://badgen.net/docker/size/tomsnow1999/docker-com_wechat_robot)](https://hub.docker.com/r/tomsnow1999/docker-com_wechat_robot/tags)

A docker image for [ComWeChatRobot](https://github.com/ljc545w/ComWeChatRobot)


``` shell
docker run \
    --name comwechat  \
    --network host \
    -e VNCPASS=asdfgh123 \
    -dti  \
    --ipc=host \
    --privileged \
    -v $(pwd)/volume/WeChat\ Files/:'/home/user/.wine/drive_c/users/user/My Documents/WeChat Files/'  \
    -v $(pwd)/volume/Application\ Data:'/home/user/.wine/drive_c/users/user/Application Data/' \
    tomsnow1999/docker-com_wechat_robot
```

### 参数说明
* 端口 5905: VNC 服务的端口(无法/无需修改)
* 环境变量 VNCPASS: 连接 VNC 的密码（可自定义，建议在服务器上使用本镜像的话设置得难一点）
* 目录映射 `WeChat Files`: 微信收到的图片/文件存储的目录(可以取消目录映射)
* 目录映射 `Application Data`: 微信数据目录(可以取消目录映射)

## 如何使用
1. 运行上方命令启动镜像(更推荐使用 [docker-compose](./docker-compose.yaml) )
2. 连接上 VNC 扫码登陆微信(建议扫码登陆后把微信的版本号弹窗等关闭)
3. 使用 python 与微信通信(参考文件 [test.py](./test.py) )


## 鸣谢
[ljc545w/ComWeChatRobot](https://github.com/ljc545w/ComWeChatRobot)
[@0honus0](https://github.com/0honus0)
