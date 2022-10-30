# VisibleCode

### About VisibleCode
...

### TO DO List
- [x] 代码上传界面点击分析异步提交表单，在当前页面显示文件结构的树状图/包含图，放个按钮“生成图表”，跳转到图表界面。
- [ ] 图表生成界面能正常生成的图表显示，不能正常显示的先不显示。添加搜索和过滤图表功能。
- [ ] 先把python搞好，然后支持多语言！
- [ ] 分析完了给出代码修改建议（还没想好怎么写
- [ ] 另开一个页面，在线IDE，用来放代码执行过程可视化（画大饼
- [ ] 页面美化相关...
- [ ] 还有啥visible相关的？
- [ ] README.md可以补一下
- [ ] .......

### How to use?
1. 点击 `fork` ，创建你的复制仓库，记下复制仓库的https。
2. 在本地找个文件夹使用 `git clone （你的仓库的https）-b dev`
3. 使用**专业版pycharm**打开刚刚clone下来的项目。
4. 在pycharm右上角选择 **运行配置 - 编辑配置 - 添加新配置 - Django 服务器**，将名称改为VisibleCode，环境变量改为 `PYTHONUNBUFFERED=1;DJANGO_SETTINGS_MODULE=VisibleCode.settings`
5. 下载 mysql ，记下**登录时的账号密码**，在 `settings.py` 的 `DATABASES` 中的 `USER` 和 `PASSWORD` 改为刚才记下的账号密码
6. 在 mysql 中使用建库语句 `create database Visible_Code DEFAULT CHARSET utf8 COLLATE utf8_general_ci;`
7. 使用 pycharm 任务栏中的 **工具 - 运行 manage.py 任务**，执行两段代码 `makemigrations` 和 `migrate`
8. 接下来就可以愉快地开发了！
9. 每次写完代码后，`commit` 到你 fork 的仓库的 dev 分支中，`pull request` 到原仓库的 **dev** 分支下

### About Us
...
