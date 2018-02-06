Minecraft Messages Bot
=====

我的世界聊天消息自动同步到qq群

> 有人催我把这个程序开源，本来想完闪好了再开源的。再下懒犯了。不知什时才完善好
>
> 先发出来再说。别吐槽代写的烂。。。。。

## 服务器----->qq部分原理
1. Minecraft 服务端实写入记录 logs/latest.log
2. 使用Linux 系统钩子函数触发命令 inotify 当写入完成时，会触发命令
3. 读取文件进行信息筛选，然后发送信息
4. qq机器人监听消息，然后把消息发送到qq群里
## qq--------->服务器部分原理
1. 向qqbot注册事件的回调函数，qq群有新消息时被调用
2. 通过RCON协议实现其他进程与minecraft服务端的远程通信

目前只写单通信（服务器 ---> qq 群）， 懒癌犯了。另一种通信不知道什么时候才开始写。。。。

欢迎提 pr

## 依赖

    apt install inotify-tools
	server.proporties中要开启RCON相关的支持，先设置mc.rcon=true,然后设置port和password重新开服
	apt install python3
	RCON协议的python实现
##  简单使用
    把sample.py,mcrcon.py放到qqbot的plugins文件夹下(具体可以参考qqbot文档)
	qq plug sample注册插件(qqbot文档)
	或许setup.sh可以完成这个功能

我是部署debian上的

windows管不着

### qq-bot
https://github.com/pandolia/qqbot
### RCON协议的python实现
https://github.com/barneygale/MCRcon


## Todo

- [ ] English Docs
- [ ] 优化代码，现在太丑陋了
- [ ] 继续扩展功能，增强qqbot可调戏性
- [ ] 服务器----->qq的shell用python重构
