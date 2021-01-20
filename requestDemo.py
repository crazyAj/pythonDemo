import json
import traceback
from urllib import request, parse

import requests
import urllib3

#  忽略 python3 https 请求警告
urllib3.disable_warnings()

"""
content-type: text/html;charset:utf-8;
常见的媒体格式类型如下：
    text/html                   HTML格式
    text/plain                  纯文本格式      
    text/xml                    XML格式
    image/gif                   gif图片格式    
    image/jpeg                  jpg图片格式 
    image/png                   png图片格式
    
    application/xhtml+xml       XHTML格式
    application/xml             XML数据格式
    application/atom+xml        Atom XML聚合格式    
    application/json            JSON数据格式
    application/pdf             pdf格式  
    application/msword          Word文档格式
    application/octet-stream    二进制流数据（如常见的文件下载）
    application/x-www-form-urlencoded   <form encType=””>中默认的encType，form表单数据被编码为key/value格式发送到服务器（表单默认的提交数据的格式）
    multipart/form-data         需要在表单中进行文件上传时，就需要使用该格式
"""

__charset = 'utf-8'


def testUrllibGet():
    """ 测试 Urllib GET 请求 """
    url = r"http://192.168.11.164:8888/spring-boot/rest/testGet"
    params = {'a': '啊', 'b': '2'}
    # URL参数 encode
    encodeParam = parse.urlencode(params)
    # URL拼接参数
    encodeUrl = "?".join([url, encodeParam])
    res = request.urlopen(encodeUrl, timeout=5)
    print('测试 Urllib GET 请求')
    try:
        print("url = ", res.geturl())
        print("code = ", res.getcode())
        print("body = ", res.read().decode(__charset))
        print("headers = ", res.getheaders())
        print("info = ", res.info())
    except Exception as e:
        print("Urllib GET 请求异常 ", e)


def testUrllibPost():
    """ 测试 Urllib POST 请求 """
    url = r"http://192.168.11.164:8888/spring-boot/rest/testPost"
    params = {'a': '啊', 'b': '2'}
    # URL参数 encode
    encodeParam = parse.urlencode(params)
    # URL拼接参数
    encodeUrl = '?'.join([url, encodeParam])
    print('测试 Urllib POST 请求： ', encodeUrl)
    # body 数据
    data = {
        'a': '嗷嗷嗷',
        'b': 'haha'
    }
    # 请求头 header
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) "
                      "AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/68.0.3440.106 Safari/537.36",
        "content-type": "application/json; charset=UTF-8"
    }
    # 代理
    ip_port = "192.168.11.164:2333"
    proxies = {
        "http": "http://" + ip_port,
        "https": "https://" + ip_port
    }
    try:
        proxy_hander = request.ProxyHandler(proxies)
        opener = request.build_opener(proxy_hander)
        req = request.Request(encodeUrl, headers=headers, data=bytes(json.dumps(data), __charset))
        res = opener.open(req, timeout=10)
        print("url = ", res.geturl())
        print("code = ", res.getcode())
        print("body = ", res.read().decode(__charset))
        print("headers = ", res.getheaders())
        print("info = ", res.info())
    except Exception as e:
        print("Urllib POST 请求异常 ", e)


def testRequestsGet():
    """ 测试 Requests GET 请求 """
    url = r"http://192.168.11.164:8888/spring-boot/rest/testGet"
    params = {'a': '啊', 'b': '2'}
    # # URL参数 encode
    # encodeParam = parse.urlencode(params)
    # # URL拼接参数
    # encodeUrl = '?'.join([url, encodeParam])
    # print('测试 Requests GET 请求： %s' % encodeUrl)
    try:
        # res = requests.get(encodeUrl, timeout=5)
        res = requests.get(url, params=params, timeout=5)
        print(res.headers)
        print(res.content.decode(__charset))
    except Exception as e:
        print("Requests GET 请求异常 %s" % e)


def testRequestsPost():
    """ 测试 Requests POST 请求 """
    url = r"http://192.168.11.164:8888/spring-boot/rest/testPost"
    params = {'a': '啊', 'b': '2'}
    # URL参数 encode
    encodeParam = parse.urlencode(params)
    # URL拼接参数
    encodeUrl = '?'.join([url, encodeParam])
    print('测试 Requests POST 请求： %s' % encodeUrl)
    # body 数据
    data = {
        'a': '嗷嗷嗷',
        'b': 'haha'
    }
    # 请求头 header
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) "
                      "AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/68.0.3440.106 Safari/537.36",
        "content-type": "application/json; charset=UTF-8"
    }
    # cookie
    cookies = {
        "cookieKey": "cookieVal"
    }
    # 代理
    ip_port = "192.168.11.164:10808"
    proxies = {
        "http": "http://" + ip_port,
        "https": "https://" + ip_port
    }
    try:
        res = requests.post(encodeUrl, headers=headers, proxies=proxies, cookies=cookies, json=data, timeout=10)
        # code != 200  会抛出异常
        res.raise_for_status()
        print(res.headers)
        print(res.content.decode(__charset))
    except Exception as e:
        print("Requests POST 请求异常 %s")
        traceback.print_exec()


def testUrllib3():
    """ 测试 urllibe3 http 连接池 """
    url = r"https://www.baidu.com"
    try:
        # 创建一个连接池的实例
        # 1. retry: 重试重定向次数, 默认次数为3次, 如果想要关闭重定向, 但是不想关闭重试只需redirect = Flase, 如果重定向重试都关闭, retries = False
        # 2. timeout: 超时, 可以设置链接超时和读超时  timeout = urllib3.Timeout(connect=1, read=2)
        # 3. numpools: 池子的数量, 假如有10个池子, 当你访问第11个ip的时候第一个池子会被干掉, 然后建一个新的供第11个使用.一个池子是作用于同一个ip下的,
        #    即：http: // aaa.com / a 和http: // aaa.com / b是会共用一个池子的
        # 4. maxsize: 一个池子缓存的最大连接数量.没有超过最大链接数量的链接都会被保存下来.在block为false的情况下,
        #    添加的额外的链接不会被保存一般多用于多线程之下, 一般情况是设置为和线程数相等的数量, 保证每个线程都能访问一个链接.
        # 5. 还有一个参数是block, 默认为False, 如果线程数量大于池子最大链接数量.这时设置block为true, 则会阻塞线程, 因为线程会等其他线程使用完链接,
        #    如果设置为False, 则不会阻塞线程, 但是会新开一个链接.有一个弊端是, 使用完之后这个链接会关闭, 所以如果 多线程经常建立链接会影响性能, 多占用多余的资源
        timeout = urllib3.Timeout(connect=5, read=5)  # 也可以设置 timeout=10 连接和读写都是10s
        http = urllib3.PoolManager(retries=2, timeout=timeout, num_pools=20, maxsize=20, block=False)
        for i in range(1, 3):
            print("\n--- 第 " + str(i) + " 次 请求 ---")
            res = http.request(method='GET',
                               url=url,
                               headers={'Content-Type': 'application/json'},
                               # GET 参数 (POST 无效， 需要拼接 url 参数转义)
                               fields={"key": "value"},
                               # POST 内容
                               body=None)
            # 状态码
            print("status = ", res.status)
            # 数据
            print("data = ", res.data.decode(__charset)[0:15])
            # 响应头
            print("headers = ", json.dumps(dict(res.headers)))
    except Exception as e:
        print("Urllib3 http 连接池 请求异常")
        traceback.print_exc()


# 测试 Requests GET 请求
# testRequestsGet()

# 测试 Requests POST 请求
testRequestsPost()

# testUrllibGet
# testUrllibGet()

# 测试 Urllib POST 请求
# testUrllibPost()

# 测试 urllibe3 http 连接池
# testUrllib3()
