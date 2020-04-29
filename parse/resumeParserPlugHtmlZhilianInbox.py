#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2020/4/29 10:43
# @Author: xk
# @File  : resumeParserPlugHtmlZhilianInbox.py
import json

from bs4 import BeautifulSoup

import MyEncoder


class ResumeParserPlugHtmlZhilianInbox(object):

    def readFile(self, htmlPath):
        html = open(htmlPath, mode='r', encoding='utf-8').read()
        return html

    def getResumeModuleDict(self, htmlStr):
        moduleDict = {}
        myModuleObj = moduleObj()
        soup = BeautifulSoup(htmlStr, 'html.parser', from_encoding='utf-8')
        print("------------------------------------------------基本信息------------------------------------------------")
        基本信息_element = soup.find_all(class_="resume-content__candidate-basic")
        print(基本信息_element)
        moduleDict['基本信息_element'] = str(基本信息_element)
        myModuleObj.moduleName = '基本信息_element'
        myModuleObj.moduleHtml = 基本信息_element

        求职意向_element = soup.find(id="resumeDetail").find('div', attrs={'data-bind': 'visible: isShowIntent'})
        print(求职意向_element)
        moduleDict['求职意向_element'] = str(求职意向_element)

        # moduleJson = json.dumps(moduleDict, cls=MyEncoder)
        moduleJson = json.dumps(moduleDict, ensure_ascii=False)
        print(moduleJson)


class moduleObj(object):
    moduleName = ''
    moduleHtml = ''


if __name__ == '__main__':
    zhilian = ResumeParserPlugHtmlZhilianInbox()
    htmlPath = '/Users/admin/Desktop/简历解析/智联招聘/智联招聘-插件-已下载模块-openFrom-2-李宁-直接报错.html'
    htmlStr = zhilian.readFile(htmlPath)
    zhilian.getResumeModuleDict(htmlStr)
