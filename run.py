# nginx auto config system
## develop by sori
## You need root privileges.
import os
jenkins = "172.30.1.5"
def menu():
	print "==# nginx auto config system #=="
	print "1. config files"
	print "2. restart nginx"
	print "3. show route list.."
	print "4. exit"
	menu = raw_input("select menu : ")
	return menu
#file name
def config():
	service = raw_input("service name : ")
	domain = raw_input("domain : ")
	port = raw_input("port : ")
	print "empty = localhost"
	print "jenkins = jenkins server"
	print "you write ip and remote http url"
	ip = raw_input("host : ")
	if ip=='':
		ip = "127.0.0.1"
	elif ip=='jenkins':
		ip = jenkins
	node_config = '''server { 
	listen 80;
        server_name '''+domain+'''.rinc.kr;
        location / {
                proxy_pass http://'''+ip+''':'''+port+''';
        }
}
'''
	f = open("/etc/nginx/sites-enabled/"+service,"w")
	f.write(node_config)
	f.close()
	print "load config file and nginx restart"
	restart()
def restart():
	os.system("service nginx restart")
def routeList():
	os.system("ls /etc/nginx/sites-enabled/")
if __name__ == '__main__':
	print "!!!Just only ubuntu & node.js configurations!!!\n\n"
	while True:
		select = menu()
		if select == "1":
			config()
		elif select == "2":
			restart()
		elif select == "3":
			routeList()
		elif select == "4":
			break
		else:
			print "select 1~4"
		
