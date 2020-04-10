# -*- coding: utf-8 -*-

# Scrapy settings for doub project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'doub'

SPIDER_MODULES = ['doub.spiders']
NEWSPIDER_MODULE = 'doub.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'doub (+http://www.yourdomain.com)'
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False
LOG_LEVEL="WARNING"
# LOG_LEVEL="INFO"
LOG_FILE="./log.log"
# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default) 
# 设置cookie
# COOKIES_ENABLED = False
# REDIRECT_ENABLED = False  #禁止重定向
# HTTPERROR_ALLOWED_CODES = [301]
# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False
# MEDIA_ALLOW_REDIRECTS = True
# Override the default request headers:
# DEFAULT_REQUEST_HEADERS = {
#    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#    'Accept-Language': 'en',
#    'Accept-Encoding': 'gzip, deflate, br',
#    'Connection': 'keep-alive',
#    'Host': 'read.douban.com',
#    'Cookie':'ll="118302"; bid=XtyX44cFcDE; __utmv=30149280.18773; douban-profile-remind=1; __gads=ID=3cbb2317b527f7a9:T=1566869187:S=ALNI_MZC99pOe5YKS9n0FsqhAO1qAcL04g; _vwo_uuid_v2=DB50A1B048BBEFC90E3DC60B322BA1174|cdde8fe011ff40c41719857cab980348; gr_user_id=db380e3e-22ac-43cb-b823-fbec0411e1ab; _ga=GA1.2.1815196810.1564661306; viewed="34937425_34863426_34934004_34910653_34863428_34970714_26944962_26163454"; ct=y; _ga=GA1.3.1815196810.1564661306; _gid=GA1.3.663939979.1583577794; __utma=30149280.1815196810.1564661306.1583582139.1583599449.18; __utmz=30149280.1583599449.18.13.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; _pk_ref.100001.a7dd=%5B%22%22%2C%22%22%2C1583630689%2C%22https%3A%2F%2Fbook.douban.com%2F%22%5D; _pk_ses.100001.a7dd=*; _pk_id.100001.a7dd=3607239cca518ded.1583577794.4.1583631141.1583599630.'
# }

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'doub.middlewares.DoubSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'doub.middlewares.DoubDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'doub.pipelines.DoubPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
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
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
