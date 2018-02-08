import mcrcon
from readInfo import readCfg

ip,port,password=readCfg()
mc = mcrcon.MCRcon()
mc.connect(ip, int(port), password)
print("connection established")

def onQQMessage(bot, contact, member, content):
    if content == '':
        print("输入无效，无法同步")
        bot.SendTo(contact, '输入无效，无法同步')
        return
    if content == '#hello':
        bot.SendTo(contact, '我是outlife_debugger，我会把群内聊天记录同步到服务器')
        bot.SendTo(contact, ('->输入/list查看服务器在线人数\n'
                             '->输入/plugins查看服务器支持插件\n'
                             '->输入/version查看服务器版本\n'
                             '->其它的，欢迎探索哦'))
    commands = ["/list", "/plugins", "/version", "/restart", "/stop", "/time","/whitelist"]
    opcommands = ["/restart", "/stop", "/time","/whitelist"]
    op = ["traceback", "metal", "抽奖和白名单请私聊我"]
    core = content.split()[0]
    commander = member.name
    if content in commands:
        if (core in opcommands) and (commander in op):
            print("you are permitted")
            bot.SendTo(contact,"you are permitted")
            response = mc.command(content[1:])
            bot.SendTo(contact, response)
            return
        elif (not(commander in op))and(core in opcommands):
            bot.SendTo(contact, "permission denied")
            return
        else:
            response = mc.command(content[1:])
            bot.SendTo(contact, response)
            return
    if not (member.name == 'mc_debug'):
        # bot.SendTo(contact, 'received')
        mccommand = 'say' + ' ' + member.name + '说:"' + content + '"'
        # bot.SendTo(contact,  mccommand)
        response = mc.command(mccommand)
