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
        soup = BeautifulSoup(htmlStr, 'html.parser', from_encoding='utf-8')

        # ------------------------------------------------基本信息------------------------------------------------
        基本信息_element = soup.find_all(class_="resume-content__candidate-basic")
        moduleDict['基本信息'] = str(基本信息_element)

        # ------------------------------------------------求职意向------------------------------------------------
        求职意向_element = soup.find(id="resumeDetail").find(
            'div', attrs={'data-bind': 'visible: isShowIntent'})
        moduleDict['求职意向'] = str(求职意向_element)

        # ------------------------------------------------教育经历------------------------------------------------
        教育经历_element = soup.find(id="resumeDetail").find(
            attrs={'data-bind': 'if: educationExperience().length'})
        moduleDict['教育经历'] = str(教育经历_element)

        # ------------------------------------------------工作经验------------------------------------------------
        工作经验_element = soup.find(id="resumeDetail").find(
            'div', attrs={'data-bind': 'if: workExperience().length'})
        moduleDict['工作经验'] = str(工作经验_element)

        # ------------------------------------------------项目经验------------------------------------------------
        项目经验_element = soup.find(id="resumeDetail").find(
            'div', attrs={'data-bind': 'if: projectExperience().length'})
        moduleDict['项目经验'] = str(项目经验_element)

        # ------------------------------------------------专业技能------------------------------------------------
        专业技能_element = soup.find(id="resumeDetail").find(
            'div', attrs={'data-bind': 'if: professionalSkill().length'})
        moduleDict['专业技能'] = str(专业技能_element)

        # ------------------------------------------------自我评价------------------------------------------------
        自我评价_element = soup.find(id="resumeDetail").find(
            'div', attrs={'data-bind': 'if: evaluate.content'})
        moduleDict['自我评价'] = str(自我评价_element)

        # ------------------------------------------------培训经历------------------------------------------------
        培训经历_element = soup.find(id="resumeDetail").find(
            'div', attrs={'data-bind': 'if: trainingExperience().length'})
        moduleDict['培训经历'] = str(培训经历_element)

        # ------------------------------------------------所获证书------------------------------------------------
        所获证书_element = soup.find(id="resumeDetail").find(
            'div', attrs={'data-bind': 'if: achieveCertificate().length'})
        moduleDict['所获证书'] = str(所获证书_element)

        # ------------------------------------------------在校情况------------------------------------------------
        在校情况_element = soup.find(id="resumeDetail").find(
            'div',
            attrs={'data-bind': 'if: achieveScholarship().length || achieveAward().length || studyInfomation()'})
        moduleDict['在校情况'] = str(在校情况_element)

        # ------------------------------------------------语言能力------------------------------------------------
        语言能力_element = soup.find(id="resumeDetail").find(
            'div', attrs={'data-bind': 'if: languageSkill().length'})
        moduleDict['语言能力'] = str(语言能力_element)

        moduleJson = json.dumps(moduleDict, ensure_ascii=False)

        print(moduleJson)




if __name__ == '__main__':
    zhilian = ResumeParserPlugHtmlZhilianInbox()
    htmlPath = '/Users/admin/Desktop/简历解析/智联招聘/智联招聘-插件-已下载模块-openFrom-2-李宁-直接报错.html'
    htmlStr = zhilian.readFile(htmlPath)
    zhilian.getResumeModuleDict(htmlStr)
