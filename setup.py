# -*- coding: utf-8 -*-
# @Time : 2020/7/30 8:50
# @Author : B站@电脑初哥
# @Email : 1009019824@qq.com
# @File : setup.py.py

from setuptools import setup, find_packages

setup(
    name = "ipku",
    version = "0.1.0",
    keywords = ("pip", "ip代理池"),
    description = "基于py3开发的ip代理池",
    long_description = "基于python3开发的ip代理池,由广州电脑初哥工作室开发。由ip3366.cn及快代理提供服务",
    license = "MIT Licence",


    url = "https://github.com/fengmm521/pipProject",
    author = "B站@电脑初哥",
    author_email = "xhrzg2017@gmail.com",

    packages = find_packages(),
    include_package_data = True,
    platforms = "any",
    install_requires = ['requests','parsel','random',]
)