# -*- coding: utf-8 -*-

# Scrapy settings for HeBei project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'HeBei'

SPIDER_MODULES = ['HeBei.spiders']
NEWSPIDER_MODULE = 'HeBei.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = 'HeBei (+http://www.yourdomain.com)'
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.117 Safari/537.36'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Cookie': 'PHPSESSID=6vk41ojbmjub8acoajavt8it16; ASP.NET_SessionId=fe0bfd45whuojfz0k4qd53rg; __utmc=218362450; __utma=218362450.1029440943.1528104172.1534476691.1534490035.10; __utmz=218362450.1534490035.10.9.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utmb=218362450.2.10.1534490035',
    'Host': 'zbb.hebjs.gov.cn',
    'Pragma': 'no-cache',
    'Referer': 'http://zbb.hebjs.gov.cn/',
    'Upgrade-Insecure-Requests': '1'
}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'HeBei.middlewares.HebeiSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
   'HeBei.middlewares.HebeiDownloaderMiddleware': 200,
}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'HeBei.pipelines.HebeiPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
ALLOWED_URL = ['http://zbb.hebjs.gov.cn/?a=eng-anc-list',
'http://www.hebpr.cn/inteligentsearch/rest/inteligentSearch/getFullTextDataNew',
'http://www.ccgp-hebei.gov.cn/province/cggg/zbgg/index_746.html/',
'http://search.hebcz.gov.cn:8080/was5/web/search?channelid=228483&province=130000000&city=&select=&searchword=&searchword1=',
'http://search.hebcz.gov.cn:8080/was5/web/search?channelid=228483&province=130000000&city=&purchaseWay=&lanmu=zhbgg&syprovince=&sydoctitle=&admindivcode=130000000&purchaseWay1=&PurchaserName=&searchword1=',



               ]