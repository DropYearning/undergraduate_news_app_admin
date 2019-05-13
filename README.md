# HDU_news_app_xadmin


毕业设计《基于Android的新闻推荐客户端设计与实现》基于Django+Xadmin的Web后台

> 这是一个为实际部署到VPS而设置的新分支!

## 截图

#### 首页
![](https://pic-1253509712.cos.ap-shanghai.myqcloud.com/20190513113613.png)
#### 统计页 
![](https://pic-1253509712.cos.ap-shanghai.myqcloud.com/20190513113858.png)

#### 新闻列表页
![](https://pic-1253509712.cos.ap-shanghai.myqcloud.com/20190513113646.png)

## 待增加功能
- [x] 定制首页, 显示入库新闻统计
- [x] 部署Django 到 VPS
- [ ] 增加新APP(userApp) 管理用户个人信息, 历史行为
- [ ] 增加新APP(推荐功能) 实现对推荐功能的后台记录
- [ ] 增加日志显示功能
- [x] 修改爬虫, 将日志信息录入数据库
- [x] 保存所有部署相关配置文件

## 待改进的地方
- [] 请求API时使用异步多线程
- [] 采集函数改为使用mysqlclient库提升性能

 
