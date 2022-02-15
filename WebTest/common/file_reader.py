"""
===============================
 -*- coding:utf-8 -*-
 @Software: PyCharm
 @Author: Zoe
 @Email: 1120003477@qq.com
 @Time: 2021-06-15 12:35
 @File: file_reader.py
 @Msg:
===============================
"""
import os
import yaml


class File:
    def __init__(self, file_path: str):
        if not os.path.exists(file_path):
            raise FileNotFoundError
        self._file_path = file_path
        self._data = None


class YamlRader(File):
    def __init__(self, yaml_path: str, multi: bool = False):
        super(YamlRader, self).__init__(yaml_path)
        self._multi = multi

    @property
    def data(self):
        if not self._data:
            with open(self._file_path, 'rb') as fp:
                if self._multi:
                    self._data = list(yaml.safe_load_all(fp))  # 将生成器转为列表;多节参数为ture
                else:
                    self._data = list(yaml.safe_load(fp)) # 将生成器转为列表;单节参数为ture
        return self._data


# obj = YamlRader(yaml_path='',multi=True)
