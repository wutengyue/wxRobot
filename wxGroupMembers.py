from wxpy import *
import csv

#新建机器人对象
bot = Bot(cache_path=True)
#bot = Bot()

#文件位置 Mac
path = '/Users/wutengyue/Downloads/'

#文件位置 Windows，win中用反斜杠\表示目录,而unix中，\是转义字符
#path = 'C:\\path\\file'

#while循环
while True:

    #提示输入群名
    groupName = input('请输入仅可找到1个群的关键词（按t退出）：')

    #输入t直接退出
    if groupName == 't':
        print('您的微信成功登出了本程序。')
        break
    
    #进入下一步
    else:

        #提示正在寻找该群
        print('🔍🔍🔍  正在寻找包含 {} 的群！'.format(groupName))
        print('\n')

        #找到指定的微信群组
        groups = bot.groups().search(groupName)

        #通过群组长度判断是找到0/1个群/多个群
        lens = len(groups)

        #未找到群
        if lens == 0:
            print('⚠️️️️️⚠️⚠️  未找到该群，请重新输入！')
            print('\n')
            continue
        
        #找到多个群
        elif lens > 1:
            for i in groups:
                print(i.name)
            
            print('\n')
            print('⚠️⚠️⚠️  找到{}个群，请重新输入！'.format(lens))
            print('\n')
        
        #找到1个群
        else:
            group = groups[0]

            #群成员数量
            nums = len(group)

            #提示找到了该群
            print('✅✅✅  已定位到 {} ！'.format(group.name))
            print('\n')

            print('👨👨👨  该群有 {} 个群成员，即将打印！'.format(nums))
            print('\n')
        
            #新建一个文件'gMembers.csv'，用于输出结果
            with open(path + 'gMembers.csv', 'w', encoding='utf-8-sig') as f:

                #使用列表list存储群成员昵称
                lst = []

                #使用index打印list
                index = 0

            #遍历群成员，并存储到list中
                for member in group:
                    lst.append(member.nick_name + '\n')
                    #print(lst[index])
                    index = index + 1
            
            #将list写入文件
                f.writelines(lst)
            
            print('🎉🎉🎉  打印成功！')
            print('\n')

            #是否继续打印其他群
            goon = input('按1打印其他群；按其他键退出：')

            if goon == '1':
                continue
            else:
                break
#退出微信
bot.logout()
