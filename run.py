#!/usr/bin/python3
import subprocess, os, signal, datetime, time


class DockerWechatHook:
    def __init__(self):
        signal.signal(signal.SIGINT, self.now_exit)
        signal.signal(signal.SIGHUP, self.now_exit)
        signal.signal(signal.SIGTERM, self.now_exit)

    def now_exit(self, signum, frame):
        self.exit_container()

    def prepare(self):
        # if not os.path.exists("/comwechat/http/SWeChatRobot.dll"):
        if not os.path.exists("/dll_downloaded.txt"):
            COMWECHAT = os.environ['COMWECHAT']
            # NOTE: 当 ComWeChatRobot 的仓库地址变动的话需要修改
            if not COMWECHAT.startswith("https://github.com/ljc545w/ComWeChatRobot/releases/download/"):
                print("你提供的地址不是 COMWECHAT 仓库的 Release 下载地址，程序将自动退出！")
                self.exit_container()
            self.prepare = subprocess.run(['wget', COMWECHAT, '-O', 'comwechat.zip'])
            self.prepare = subprocess.run(['unzip', '-d', 'comwechat', 'comwechat.zip'])
            self.prepare = subprocess.run(['mv', '/WeChatHook.exe', '/comwechat/http/WeChatHook.exe'])
            with open("/dll_downloaded.txt", "w") as f:
                f.write("True\n")

    def run_vnc(self):
        # 根据 VNCPASS 环境变量生成 vncpasswd 文件
        os.makedirs('/root/.vnc', mode=755, exist_ok=True)
        passwd_output = subprocess.run(['/usr/bin/vncpasswd','-f'],input=os.environ['VNCPASS'].encode(),capture_output=True)
        with open('/root/.vnc/passwd', 'wb') as f:
            f.write(passwd_output.stdout)
        os.chmod('/root/.vnc/passwd', 0o700)
        self.vnc = subprocess.Popen(['/usr/bin/vncserver','-localhost',
            'no', '-xstartup', '/usr/bin/openbox' ,':5'])

    def run_wechat(self):
        # if not os.path.exists("/wechat_installed.txt"):
        #     self.wechat = subprocess.run(['wine','WeChatSetup.exe'])
        #     with open("/wechat_installed.txt", "w") as f:
        #         f.write("True\n")
        # self.wechat = subprocess.run(['wine', 'explorer.exe'])
        self.wechat = subprocess.Popen(['wine','/home/user/.wine/drive_c/Program Files/Tencent/WeChat/WeChat.exe'])
        # self.wechat = subprocess.run(['wine','/home/user/.wine/drive_c/Program Files/Tencent/WeChat/WeChat.exe'])

    def run_hook(self):
        print("等待 5 秒再 hook")
        time.sleep(5)
        self.reg_hook = subprocess.run(['wine','/comwechat/http/WeChatHook.exe'])
        # self.reg_hook = subprocess.run(['wine', 'explorer.exe'])

    def exit_container(self):
        print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')+ ' 正在退出容器...')
        try:
            print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')+ ' 退出微信...')
            os.kill(self.wechat.pid, signal.SIGTERM)
        except:
            pass
        try:
            print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')+ ' 退出Hook程序...')
            os.kill(self.reg_hook.pid, signal.SIGTERM)
        except:
            pass
        try:
            print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')+ ' 退出VNC...')
            os.kill(self.vnc.pid, signal.SIGTERM)
        except:
            pass

    def run_all_in_one(self):
        print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')+ ' 启动容器中...')
        self.prepare()
        self.run_vnc()
        self.run_wechat()
        self.run_hook()
        print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')+ ' 感谢使用.')


if __name__ == '__main__' :
    print('---All in one 微信 ComRobot 容器---')
    hook = DockerWechatHook()
    hook.run_all_in_one()