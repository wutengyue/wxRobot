from wxpy import *
import time

#新建机器人
bot = Bot(cache_path = True)

#文件路径
path = '/Users/tengyue/Downloads/'

#文件位置 Windows，win中用反斜杠\表示目录,而unix中，\是转义字符
#path = 'C:\\path\\file'

#提示输入群名
groupName = input('请输入1个需要监听的群：')

#找到指定的微信群列表
group = bot.groups().search(groupName)
print('group')
print(group)
print('\n')

#将group赋值给另一个列表groups，以便继续添加群组
groups = group
print('groups')
print(groups)
print('\n')

#循环输入需要监听的群
while True:

    #是否继续添加群
    goon = input('按1添加其他群；按其他键退出：')

    if goon == '1':

        #提示输入群名
        groupName = input('请输入1个需要监听的群：')

        #找到指定的微信群组
        group = bot.groups().search(groupName)
        print('group')
        print(group)
        print('\n')

        #遍历群列表中的群，加到groups中
        for i in group:
            groups.append(i)

        #打印添加新群组后的groups列表
        print('groups')
        print(groups)
        print('\n')

        continue

    else:
        break

print('\n')
print('开始监听群消息！')
@bot.register(groups)
def print_messages(msg):
    with open(path + 'gMsgs.csv', 'a', encoding = 'utf8') as f:
        
        #日期转字符串
        strTime = msg.create_time.strftime('%Y-%m-%d %H:%M:%S')
        # print(strTime)

        msgStr = strTime + ',' + msg.sender.nick_name + ',' + msg.member.nick_name + ',' + msg.text + '\n'
        # print(msgStr)
        f.write(msgStr)

# 堵塞线程，并进入 Python 命令行
embed()
