import mcrcon

address = "mc.cityjianyi.com"
port = 35575
password = "admin"
print("#connecting the server: %s:%d" % (address, port))
mc = mcrcon.MCRcon()
mc.connect(address, port, password)
print("#connection has been established,ready to work")


def onQQMessage(bot, contact, member, content):
    if content == '#hello':
        bot.SendTo(contact, '我是outlife_debugger，我会把群内聊天记录同步到服务器')
        bot.SendTo(contact, '输入/list查看服务器在线人数')
    elif content[0] == '/':
        if content[1:] == 'list':
            bot.SendTo(contact, 'listing')
            response = mc.command('list')
            bot.SendTo(contact, response)
    if not(member.name=='mc_debug'):
    #bot.SendTo(contact, 'received')
     mccommand = 'say'+' '+member.name+'说:"'+content+'"'
    #bot.SendTo(contact,  mccommand)
     response = mc.command(mccommand)