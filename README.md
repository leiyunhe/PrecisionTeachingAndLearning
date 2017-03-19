# PrecisionTeachingAndLearning

```2017-3-18```

## 说明

> 更新时间：2017-3-18
> 版本说明：V1.0
> 功能：运行在本地服务器的程序。

## 文件目录

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
