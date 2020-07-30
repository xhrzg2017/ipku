# -*- coding: utf-8 -*-
# @Time : 2020/7/29 19:53
# @Author : B站@电脑初哥
# @Email : 1009019824@qq.com
# @File : ipku.py


import requests
import parsel
import random
from fake_useragent import UserAgent


ua = UserAgent()
headers={'User-Agent': UserAgent().random}
all_can_use=[]
def ip3366():
    def check_ip(proxies_list):
        can_use_ip3366 = []
        for ip in proxies_list:
            try:
                response =requests.get(url='https://www.taobao.com/',headers=headers,proxies=ip,timeout=0.1)
                if response.status_code==200:
                    can_use_ip3366.append(ip)
                    all_can_use.append(ip)
            except Exception:
                print('当前代理ip',ip,"请求超时,检测不通过！")
            finally:
                print('当前代理ip',ip, "检测通过！")
        return can_use_ip3366

    proxies_list = []

    for page in range(1,8):
        print('=============正在抓取ip3366.cn第{}页============='.format(page))

        base_url = 'http://www.ip3366.net/free/?stype=1&page={}'.format(str(page))

        response = requests.get(url=base_url, headers= headers)

        data = response.text

        html_data = parsel.Selector(data)
        parse_list = html_data.xpath('//table[@class="table table-bordered table-striped"]/tbody/tr')
        # print(parse_list)

        for tr in parse_list:
            http_type = tr.xpath('./td[4]/text()').extract_first()#协议
            ip_num = tr.xpath('./td[1]/text()').extract_first()#ip地址
            ip_port = tr.xpath('./td[2]/text()').extract_first()#端口
            # print(http_type,ip_num,ip_port)

            proxies_dict={}
            proxies_dict[http_type] = ip_num + ":" + ip_port
            print('保存成功',proxies_dict)
            proxies_list.append(proxies_dict)

    print(proxies_list)
    print('获取到的代理ip数量',len(proxies_list))

    print('+'*15+'正在检测ip质量'+'+'*15)
    can_use_ip3366 = check_ip(proxies_list)
    print('质量高的',can_use_ip3366)
    print('质量高的代理ip数',str(len(can_use_ip3366)))
    ip_ip3366 = random.choice(can_use_ip3366)
    print('由ip3366.cn',ip_ip3366)
    return ip_ip3366


def kuai():
    def check_ip(proxies_list):
        can_use_kuai = []
        for ip in proxies_list:
            try:
                response = requests.get(url='https://www.taobao.com/', headers=headers, proxies=ip, timeout=0.1)
                if response.status_code == 200:
                    can_use_kuai.append(ip)
                    all_can_use.append(ip)
            except Exception:
                print('当前代理ip', ip, "请求超时！")
            finally:
                print('当前代理ip', ip, "检测通过！")

        return can_use_kuai

    proxies_list = []
    for page in range(1, 8):
        print('=============正在抓取快代理第{}页============='.format(page))

        base_url = 'https://www.kuaidaili.com/free/inha/{}'.format(str(page))

        response = requests.get(url=base_url, headers=headers)

        data = response.text

        html_data = parsel.Selector(data)
        parse_list = html_data.xpath('//table[@class="table table-bordered table-striped"]/tbody/tr')
        # print(parse_list)

        for tr in parse_list:
            http_type = tr.xpath('./td[4]/text()').extract_first()  # 协议
            ip_num = tr.xpath('./td[1]/text()').extract_first()  # ip地址
            ip_port = tr.xpath('./td[2]/text()').extract_first()  # 端口
            # print(http_type,ip_num,ip_port)

            proxies_dict = {}
            proxies_dict[http_type] = ip_num + ":" + ip_port
            print('保存成功', proxies_dict)
            proxies_list.append(proxies_dict)

    print(proxies_list)
    print('获取到的代理ip数量', len(proxies_list))

    print('+' * 15 + '正在检测ip质量' + '+' * 15)
    can_use_kuai = check_ip(proxies_list)
    print('质量高的', can_use_kuai)
    print('质量高的代理ip数', str(len(can_use_kuai)))
    kuai_ip= random.choice(can_use_kuai)
    print('由快代理',kuai_ip)
    return kuai_ip



def radom_all():
    ip3366()
    kuai()
    all_ip = random.choice(all_can_use)
    print('全部提供',all_ip)
    return all_ip


if __name__ == '__main__':
    ip3366()
    kuai()
    radom_all()


