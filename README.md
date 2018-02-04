Minecraft Messages Bot
=====

我的世界聊天消息自动同步到qq群

> 有人催我把这个程序开源，本来想完闪好了再开源的。再下懒犯了。不知什时才完善好
>
> 先发出来再说。别吐槽代写的烂。。。。。

## 原理
1. Minecraft 服务端实写入记录 logs/latest.log
2. 使用Linux 系统钩子函数触发命令 inotify 当写入完成时，会触发命令
3. 读取文件进行信息筛选，然后发送信息
4. qq机器人监听消息，然后把消息发送到qq群里

目前只写单通信（服务器 ---> qq 群）， 懒癌犯了。另一种通信不知道什么时候才开始写。。。。

欢迎提 pr

## 依赖

    apt install inotify-tools

我是部署debian上的

windows管不着

### qq-bot
https://github.com/pandolia/qqbot


## Todo

- [ ] English Dosc
- [ ] qq 群 --> 服务器
- [ ] 优化代码，现在太丑陋了
