#! usr/bin/env python3
# -*- coding:utf-8 -*-

import re
from os import environ
import argparse


def get_args() -> argparse.Namespace:
    """获取命令行参数
    Returns:
    _type_: argparse.Namespace
    """
    parser = argparse.ArgumentParser(
        description="Add parased jd_cookie to environment variables"
    )
    parser.add_argument(
        "-f",
        "--add_to_file_path",
        default="./add_envs.sh",
        type=str,
        help="Add parased jd_cookie to file",
    )
    parser.add_argument("-cf", "--Cookie_file", type=str,default="./config.txt", help="cookie file path")
    parser.add_argument(
        "-tf",
        "--to_file",
        type=bool,
        default=False,
        help="Signal to switch to output_file mode",
    )
    # parser.add_argument('-td','--to_dic',type=bool,default=True,help='Signal to switch to output_dic mode')
    args = parser.parse_args()
    return args


def get_jd_cookie() -> str:
    """获取JD_COOKIE，通过环境变量获取，如果没有则尝试本地文件获取，如果没有则尝试手动输入获取
    Returns:
        _type_: str
    """

    try:
        cookie = environ.get("JD_COOKIE")
        if cookie:
            return cookie
        else:
            raise ValueError("当前环境变量中没有JD_COOKIE")
    except ValueError as e:
        print("正在尝试本地文件获取……请确保当前目录下存在cookies.txt文件")
        try:
            config_path = get_args().Cookie_file
            with open(config_path, "r") as f:
                cookies = f.read()
                if cookies:
                    return cookies
                else:
                    raise ValueError("本地文件获取失败，请检查cookies.txt文件是否存在")
        except Exception as e:
            print(e, "本地文件获取失败，请检查cookies.txt文件是否存在")
            print("正在尝试手动输入……")
            try:
                cookies = input("请输入您的JD_COOKIE（按回车结束）：")
                return cookies
            except Exception as e:
                print(e, "手动输入失败，请重试")


class Resolve_Cookie:
    def __init__(self):
        self.cookie = get_jd_cookie()
        self.to_file_signal = get_args().to_file
        self.add_to_file_path = get_args().add_to_file_path

    def resolve_cookie(self) -> dict:
        """解析cookie，返回pt_key和pt_pin

        Args:
            cookie (str): jd_cookie

        Raises:
            ValueError: ValueError

        Returns:
            dict: pt_key和pt_pin
        """
        pt_key_rule = re.compile(r"pt_key=(.*?);")
        pt_pin_rule = re.compile(r"pt_pin=(.*?);")
        try:
            pt_key = re.findall(pt_key_rule, self.cookie)[0]
            pt_pin = re.findall(pt_pin_rule, self.cookie)[0]
        except Exception as e:
            print(e, "Cookie解析失败,请输入正确的Cookie")
        result = {}
        try:
            if pt_key and pt_pin:
                result["pt_key"] = pt_key
                result["pt_pin"] = pt_pin
            elif not result:
                raise ValueError("Cookie解析失败,请输入正确的Cookie")

            else:
                raise ValueError("Cookie解析失败,请输入正确的Cookie")

        except Exception as e:
            print(e)
        return result

    @property
    def add_keys_to_env(self) -> None:
        """将pt_key和pt_pin添加到环境变量中"""
        for key, value in self.resolve_cookie().items():
            environ[key] = value

    @property
    def add_keys_to_file(self) -> None:
        """将pt_key和pt_pin添加到文件中"""
        if self.to_file_signal:
            try:
                with open(self.add_to_file_path, "a+") as f:
                    for key, value in self.resolve_cookie().items():
                        f.write(f"export {key}={value}\n")
            except Exception as e:
                print(e)
        else:
            raise ValueError("请使用-f参数指定文件路径,尝试使用自动添加环境变量中……")


def resolve_cookie():
    rc = Resolve_Cookie()
    try:
        rc.add_keys_to_file
    except Exception as e:
        rc.add_keys_to_env


if __name__ == "__main__":
    resolve_cookie()
    