#! usr/bin/env python3
# -*- coding:utf-8 -*-

import requests
import re
from Reslove_JD_Cookie import Resolve_Cookie
import traceback


def _check_in(pt_key, pt_pin):
    url = "https://api.m.jd.com/client.action?functionId=signBeanAct&body=%7B%22fp%22%3A%22-1%22%2C%22shshshfp%22%3A%22-1%22%2C%22shshshfpa%22%3A%22-1%22%2C%22referUrl%22%3A%22-1%22%2C%22userAgent%22%3A%22-1%22%2C%22jda%22%3A%22-1%22%2C%22rnVersion%22%3A%223.9%22%7D&appid=ld&client=apple&clientVersion=10.0.4&networkType=wifi&osVersion=14.8.1&uuid=3acd1f6361f86fc0a1bc23971b2e7bbe6197afb6&openudid=3acd1f6361f86fc0a1bc23971b2e7bbe6197afb6&jsonp=jsonp_1645885800574_58482"
    headers = {
        "Connection": "keep-alive",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Cache-Control": "no-cache",
        "User-Agent": "okhttp/3.12.1;jdmall;android;version/10.3.4;build/92451;",
        "accept": "*/*",
        "connection": "Keep-Alive",
        "Accept-Encoding": "gzip,deflate",
        "Cookie": "__jd_ref_cls=JingDou_SceneHome_NewGuidExpo;\
                        mba_muid=1645885780097318205272.81.1645885790055;\
                        mba_sid=81.5;\
                        __jda=122270672.1645885780097318205272.1645885780.1645885780.1645885780.1;\
                        __jdb=122270672.1.1645885780097318205272|1.1645885780; __jdc=122270672;\
                        __jdv=122270672%7Ckong%7Ct_1000170135%7Ctuiguang%7Cnotset%7C1644027879157;\
                        pre_seq=0;\
                        pre_session=3acd1f6361f86fc0a1bc23971b2e7bbe6197afb6|143;\
                        unpl=JF8EAKZnNSttWRkDURtVThUWHAgEWw1dH0dXOjMMAFVcTQQAEwZORxR7XlVdXhRKFx9sZhRUX1NIVw4YBCsiEEpcV1ZVC0kVAV9XNVddaEpkBRwAExEZQ1lWW1kMTBcEaWcAUVpeS1c1KwUbGyB7bVFeXAlOFQJobwxkXGhJVQQZBR0UFU1bZBUzCQYXBG1vBl1VXElRAR8FGxUWS1hRWVsISCcBb2cHUm1b%7CV2_ZzNtbRYAFxd9DUNcKRxYB2ILGloRUUYcIVpAAHsbWQZjVBEJclRCFnUUR11nGlgUZgIZXkFcQRRFCEJkexhdB24LFFtEUHMQfQ5GXH0pXAQJbRZeLAcCVEULRmR6KV5VNVYSCkVVRBUiAUEDKRgMBTRREV9KUUNGdlxAByhNWwVvBUIKEVBzJXwJdlR6GF0GZAoUWUdRQCUpUBkCJE0ZWTVcIlxyVnMURUooDytAGlU1Vl9fEgUWFSIPRFN7TlUCMFETDUIEERZ3AEBUKBoIAzRQRlpCX0VFIltBZHopXA%253d%253d; \
                        pt_key=xxx;\
                        pt_pin=xxx;\
                        pwdt_id=jd_505bacd333f6b;\
                        sid=1b2c8b7ce820c4188f048e689bf58c8w;\
                        visitkey=36446698972455355",
    }

    headers["Cookie"] = replace_cookie_spaces(headers["Cookie"])

    cookie = cookie_to_dict(headers["Cookie"])
    cookie["pt_key"] = pt_key
    cookie["pt_pin"] = pt_pin

    headers["Cookie"] = dict_to_cookie(cookie)

    response = requests.post(url=url, headers=headers)
    print(response.text)
    matchs = re.search(r"签到成功|签到失败|今天已签到|用户未登录", response.text, re.DOTALL)
    # print(matchs)
    return matchs.group(0)


def replace_cookie_spaces(cookie):
    new_cookie = ""
    for i in cookie.split():
        new_cookie += i
    return new_cookie


def cookie_to_dict(cookie):
    # return {item.split('=')[0]: item.split('=')[1] for item in cookie.split(';')}
    cookie_dic = {}
    for i in cookie.split(";"):
        cookie_dic[i.split("=")[0]] = i.split("=")[1]
    return cookie_dic


def dict_to_cookie(dic):
    dic = str(dic)
    cookie = re.sub(r"\{|\}|\'|\ |\,|\:", replace, dic)
    # cookie = re.sub(r'\{|\}|\'|\ ', "", dic)
    # cookie = re.sub(r'\,', ";", cookie)
    # cookie = re.sub(r'\:', "=", cookie)
    return cookie


def replace(match):
    if match.group(0) == ",":
        return ";"
    elif match.group(0) == ":":
        return "="
    else:
        return ""


def main():
    try:
        rc = Resolve_Cookie()
        info_dict = rc.resolve_cookie()
        pt_key, pt_pin = info_dict["pt_key"], info_dict["pt_pin"]
        matchs = _check_in(pt_key, pt_pin)
    except Exception as e:
        traceback.print_exc()

    try:
        from WX_Push_Services import APP_PUSH

        push = APP_PUSH()
        push.send_message(message=matchs)

    except ImportError:
        print("推送服务异常")
        print("请配置安装WX_Push_Services：pip install WX_Push_Services")
        with open("./output.log", "a+") as f:
            f.write(match)
        print("当前程序运行结果已保存到output.log文件中")
    except Exception:
        print("推送服务异常")
        traceback.print_exc()
    finally:
        pass


if __name__ == "__main__":
    main()
