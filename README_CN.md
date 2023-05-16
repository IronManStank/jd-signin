# JingDong_AutoSignin
Auto Sign in JD and daily check in.
# 特色
- [x] 自动签到
- [x] 采用wx_push_services推送签到结果，可在企业微信端直接查看（该选项可选，非必选）。
关于wx_push_services的配置方式，请移步![wx_push_services](https://github.com/IronManStank/WX-Push-Services)
- [x] 采用GitHub Action定时运行，无需服务器，无需配置，开箱即用。
- [x] 若采用本地服务器运行，可直接使用wx_push_services命令行推送方式推送消息，
- [x] 采用JD_COOKIE解析引擎(Reslove_JD_Cookie)，自动解析JD_COOKIE，无需手动寻找pt_key,pt_pin。
## 关于Reslove_JD_Cookie说明：
它提供了三种获取`JD_COOKIE`的方式:
1. 环境变量:会首先尝试从`JD_COOKIE`环境变量获取,如果存在则返回。我们非常推荐使用该种方式添加`COOKIE`。
Github Action中添加环境变量的方式如下:
在仓库的Settings->Secrets中添加名为`JD_COOKIE`的环境变量,值为获取到的`JD_COOKIE`。
2. 本地文件:如果环境变量不存在,则尝试从当前目录下的`cookies.txt`文件获取。
3. 手动输入:如果前两种方式都失败,则提示用户手动输入`JD_COOKIE`。

## 用法
1. 本地服务器运行：
- 安装依赖:
`pip install -r requirements.txt`
- 参照Reslove_JD_Cookie说明添加JD_COOKIE
- 运行
`python Auto_SignIn.py`
2. GitHub Action 运行：

1. Fork该仓库到您的GitHub账号下
2. 打开您Fork后的仓库,点击“Actions”
3. 点击“Run workflow”开始运行GitHub Action

## 交流反馈
如果您在使用过程中有任何问题或建议,欢迎提issue与我交流。
我会积极解答您的疑问,并持续优化和更新脚本,感谢您的使用与支持!
## 最后
如果出现问题,请重新配置JD_COOKIE或提issue与我交流解决。
这个京东签到解决方案通过Cookie管理,签到脚本自动更新和推送提醒等一系列设计,实现真正意义上的全自动化签到。让我们无需每日手动签到,就能轻松完成所有的京东签到活动。
希望它能带来便利,也让我们重拾对生活的简单欣赏。