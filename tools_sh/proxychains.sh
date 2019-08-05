#1.安装proxychains

sudo apt install proxychains

#2.配置proxychains

#sudo vim /etc/proxychains.conf

#将最后一行改成：

#socks5 127.0.0.1 1080

#3.proxychains使用

#proxychains wget https://www.google.com
