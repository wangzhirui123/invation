@echo off
scrapy crawl JiangXi
ping -n 3 127.0.0.1 >nul
scrapy crawl JiangXiZhongBiao
ping -n 3 127.0.0.1 >nul