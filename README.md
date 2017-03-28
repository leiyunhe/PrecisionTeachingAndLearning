# PrecisionTeachingAndLearning

+ [研究计划](https://github.com/leiyunhe/PrecisionTeachingAndLearning/blob/master/DevPlan.md)
+ [功能需求书](https://github.com/leiyunhe/PrecisionTeachingAndLearning/blob/master/FunctionalRequirement.md)
+ [开发版本日志](https://github.com/leiyunhe/PrecisionTeachingAndLearning/issues/12)
  + [V2说明](https://github.com/leiyunhe/PrecisionTeachingAndLearning/issues/10)
  + [V3说明](https://github.com/leiyunhe/PrecisionTeachingAndLearning/issues/11)
+ [路演资料](https://github.com/leiyunhe/PrecisionTeachingAndLearning/issues/9)
  + [视频文案](https://github.com/leiyunhe/PrecisionTeachingAndLearning/issues/16)
  + [视频设计资料](https://github.com/leiyunhe/PrecisionTeachingAndLearning/tree/master/ppt)
  + [路演步骤](https://github.com/leiyunhe/PrecisionTeachingAndLearning/issues/18)


------------------------------------------
# V1-本地运行的程序 ```2017-3-18```

## 说明

> 更新时间：2017-3-18
> 版本说明：V1.0
> 功能：运行在本地服务器的程序。


## 文件目录



PrecisionTeachingV1

+ run.py 主程序
+ templates/index.html 程序的网页模板
+ update_db_from_api.py 从github API读取数据，存储到数据库中。
+ get_submit_time.py 实现github API的不同的功能

## 改善计划

+ ```enhancement```

    - 整个班级的作业提交情况统计表
    - 变化趋势图
    - 历史记录<sqlite3.Row object at 0x03BEFA30>转换为实际的数据，存储并返回。
    - 部署云端heroku
    - 部署微信公众号

+ ```bug``` 

    - 测试“leiyunhe”，chap1的数据为None。
    - 历史按钮的返回值，<sqlite3.Row object at 0x03BEFA30>转换为实际的数据，存储并返回。


# V2-heroku上运行的程序 ```2017-3-23```

## 说明

> 更新时间：2017-3-23
> 版本说明：V2.0
> 功能：部署在heroku上的程序

## V1.0-2.0改善计划完成情况

- [x] 整个班级的作业提交情况统计表
- [ ] 变化趋势图
- [x] 历史记录<sqlite3.Row object at 0x03BEFA30>转换为实际的数据，存储并返回。
- [x] 部署云端heroku
- [ ] 部署微信公众号
- [x] 测试“leiyunhe”，chap1的数据为None。

    + 原因：获取issue的条件不精确，导致长三角地区chap1的数据被其他名称中包含有“长三角”和“ch1”的issue覆盖。
    + 解决方法：修改issue获取条件，通过labels描述筛选出各大区提交作业的issue。
- [x] 历史按钮的返回值，<sqlite3.Row object at 0x03BEFA30>转换为实际的数据，存储并返回。
    + 原因：row对象的读取问题
    + 解决方法：将row对象转化为元组形式，再写入历史记录的list中。

## 文件目录

PrecisionTeachingV2

+ run2.py 主程序
+ templates/index2.html 程序的网页模板
+ update_db_from_api2.py 从github API读取数据，存储到数据库中。

## 改善计划

```enhancement```

- [ ] 前期开发中，未考虑补交作业的绿色通道issue。
- [ ] html页面设计与优化
- [ ] 增加可查询的学生名单，即数据库中的用户名列表
- [ ] 撰写用户文档
- [ ] 数据库使用的是sqlite3，考虑sqlalchemy

```bug```

- [ ] 更新数据库时，用于获取API数据的用户名和密码容易泄露


# V3-进行中