# wxRobot

**wxRobot**中的微信机器人，是基于[wxpy](https://wxpy.readthedocs.io/)开发，感谢[wxpy](https://wxpy.readthedocs.io/)团队提供的易用、丰富的API接口。


#### 目前包含3个微信机器人
> 后面工作需要的话，会把3个机器人合并成一个，运行一个py文件即可。

* 导出微信群成员
  wxGroupMembers.py
* 监听微信群消息
  wxGroupMsgs.py
* 改微信好友备注
  wxRemarkName.py

#### 使用
* #### 确保运行环境是python3.4及以上版本
  MAC打开Terminl，输入'python3'，查看自己的python版本

* #### 确保python安装了wxpy包  
  执行以下命令进行安装，如果提示找不到pip3命令，需要先安装pip3
  ```bash
  pip3 install wxpy
  ```
  
* #### 运行相应机器人的py文件
  运行前，先修改一下机器人程序中的path变量（path：生成的文件放在哪里），Windows系统中路径示例 C:\path\file

  ```bash
  python3 wxGroupMember.py
  ```
