#!/bin/sh

source_path=PaperSpigot-1.12.2-b1318/logs/latest.log


while /usr/bin/inotifywait -e modify ${source_path};
do
	wget -qO- http://127.0.0.1:8188/send/group/OutLife_minecraft-v1.12.2服/$(tail -1 ${source_path} | grep 'Async Chat Thread' | awk '{print $7 $8}') >> /dev/null
done


