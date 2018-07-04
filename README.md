# wxRobot

**wxRobot**中的微信机器人，是基于[wxpy](https://wxpy.readthedocs.io/)开发，感谢[wxpy](https://wxpy.readthedocs.io/)团队提供的易用、丰富的API接口。


#### 目前包含3个微信机器人

* 导出微信群成员
  wxGroupMembers.py
* 监听微信群消息
  wxGroupMsgs.py
* 改微信好友备注
  wxRemarkName.py

#### 使用

* #### 确保用来当机器人的微信可以登录web微信
  该机器人使用web微信的接口开发，可能导致新注册微信号无法扫码登录，需要更换老号
  
* #### 确保运行环境是python3.4及以上版本
  MAC打开Terminl，输入'python3'，查看自己的python版本

* #### 确保python安装了wxpy包  
  执行以下命令进行安装，如果提示找不到pip3命令，需要先安装pip3
  
  ```bash
  pip3 install wxpy
  ```
  
* #### 确保更改了py文件中path的值
  path：生成的文件放在哪里，Windows系统中路径示例 C:\path\file
   
* #### 运行py文件
  ```bash
  python3 wxGroupMember.py
  ```
