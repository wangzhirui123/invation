@echo off
scrapy crawl ShiJiaZhuang
ping -n 3 127.0.0.1 >nul
scrapy crawl HBwinbid
ping -n 3 127.0.0.1 >nul
scrapy crawl HeBeiZhengFuCaiGou
ping -n 3 127.0.0.1 >nul
scrapy crawl HeBeiZhengFuCaiGouZhongBiao
