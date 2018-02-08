import configparser
def readCfg():
	cfg=configparser.ConfigParser()
	cfg.read("info.conf")
	password=cfg.get("server","rcon_pwd")
	ip=cfg.get("server","rcon_ip")
	port=cfg.get("server","rcon_port")
	#print(password,ip,port)
	return (ip,port,password)


#ip,port,password=readCfg()
#print(ip,port,password)
