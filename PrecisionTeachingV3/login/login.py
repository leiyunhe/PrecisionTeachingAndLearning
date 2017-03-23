#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import getpass

def login():
    USERNAME = input("请输入github用户名：")
    PASSWORD = getpass.getpass("请输入密码：")
    return (USERNAME,PASSWORD)

if __name__ == "__main__":
	login()
