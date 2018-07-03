from wxpy import *
import time
import random

# 新建机器人
bot = Bot(cache_path = True)

# 获取所有好友
# all_friends = bot.friends()
# print('👨👨👨  你目前的好友数：{}\n'.format(len(all_friends)))

# while循环
while True:

    # 提示输入群名
    groupName = input('你想要给哪个群的好友加备注（按t退出）：')

    # 输入t直接退出
    if groupName == 't':
        print('您的微信成功登出了本程序。')
        break
    
    # 进入下一步
    else:

        # 提示正在寻找该群
        print('\n🔍🔍🔍  正在寻找包含 {} 的群！\n'.format(groupName))

        # 找到指定的微信群组
        groups = bot.groups().search(groupName)

        # 通过群组长度判断是找到0/1个群/多个群
        lens = len(groups)
        print('✅✅✅  找到指定群的数目是：{}'.format(lens))

        if lens != 1:
            print('⚠️️️️️⚠️⚠️  请输入仅可找到1个群的关键词！')
            print('\n')
            continue
        else:

            # 找到1个群
            group = groups[0]

            # 群成员数量
            nums = len(group)

            # 提示找到了该群
            print('✅✅✅  已定位到 {} ！'.format(group.name))
            print('👨👨👨  该群有 {} 个群成员！'.format(nums))

            # 改备注
            # count = 0
            # for friend in all_friends:
            #     if friend in group:
            #         remarkName = friend.name
            #         if '魔王课' not in remarkName:
            #             friend.set_remark_name(remarkName + ' 魔王课')
            #             count = count + 1
            #             print('正修改 -- {} -- 的备注名'.format(remarkName))
            #             print('✅✅✅  已成功修改 {} 位好友的备注！'.format(count))
            #             sleeptime = random.randint(50, 70)
            #             print('⌚️️️️️️⌚️⌚️  睡眠{}秒后修改下一个好友备注!'.format(sleeptime))
            #             time.sleep(sleeptime)

            # 该群中，多少人是你的好友 
            count_myfriend = 0
            count_rename = 0
            for member in group:
                if member.is_friend:
                    count_myfriend = count_myfriend + 1
                    nickName = member.nick_name
                    if '魔王课' in nickName:
                        count_rename = count_rename + 1

            print('👩👩👩  该群中，{}人是你的好友'.format(count_myfriend))
            print('👩👩👩  未改备注的好友数目是：{}\n'.format(count_myfriend - count_rename))

            while True:
                # 提示输入备注名
                tag = input('🤔🤔🤔  你想要给这个群的好友加什么备注：')
                print('"{}" 的备注会添加在好友微信名后，以空格隔开！\n'.format(tag))

                # 再次确认备注名
                iftag = input('🤔🤔🤔  按1确认添加改备注，其他键重新设置备注名！')
                if iftag == '1':
                    break
                else:
                    continue

            print('🐶🐶🐶  将在10秒后添加备注" {}"！\n'.format(tag))
            time.sleep(10)

            # 改备注
            count = 0
            for member in group:
                if member.is_friend:
                    remarkName = member.nick_name
                    if tag not in remarkName:
                        member.set_remark_name(remarkName + ' ' + tag)
                        count = count + 1
                        print('正修改 "{}" 的备注名'.format(remarkName))
                        print('✅✅✅  已成功修改 {} 位好友的备注！'.format(count))
                        sleeptime = random.randint(50, 70)
                        print('⌚️️️️️️⌚️⌚️  睡眠{}秒后修改下一个好友备注!'.format(sleeptime))
                        time.sleep(sleeptime)

            print('🎉🎉🎉  修改成功/全部好友都已加备注，无需修改！\n')

            # 是否继续改备注
            goon = input('按1继续；按其他键退出：')

            if goon == '1':
                continue
            else:
                break
# 退出微信
bot.logout()


