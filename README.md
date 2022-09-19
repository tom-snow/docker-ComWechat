# docker-ComWechat
A docker image for [ComWeChatRobot](https://github.com/ljc545w/ComWeChatRobot)


``` shell
docker run \
    --name comwechat  \
    -p 5905:5905 \
    -p 18888:18888 \
    -p 123456:123456 \
    -e VNCPASS=asdfgh123 \
    -dti  \
    --ipc=host \
    --privileged \
    -v $(pwd)/volume/WeChat\ Files/:'/home/user/.wine/drive_c/users/user/My Documents/WeChat Files/'  \
    -v $(pwd)/volume/Application\ Data:'/home/user/.wine/drive_c/users/user/Application Data/' \
    tomsnow1999/docker-com_wechat_robot
```

### 参数说明
* 端口 5905: VNC 服务的端口（请勿修改冒号后部分的 5905）
* 其他端口：可以自行定义（建议冒号前后相同）
* 环境变量 VNCPASS: 连接 VNC 的密码（可自定义，建议在服务器上使用本镜像的话设置得难一点）
* 目录映射 `WeChat Files`: 微信收到的图片/文件存储的目录(可以取消目录映射)
* 目录映射 `Application Data`: 微信数据目录(可以取消目录映射)

## 如何使用
1. 运行上方命令启动镜像
2. 待完善

