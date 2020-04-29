#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2020/4/29 10:43
# @Author: xk
# @File  : resumeParserPlugHtmlZhilianInbox.py
import json

from bs4 import BeautifulSoup


class ResumeParserPlugHtmlZhilianInbox(object):

    # 读取html文件
    def readFile(self, htmlPath):
        html = open(htmlPath, mode='r', encoding='utf-8').read()
        return html

    # 将html简历按照板块区分

    def getResumeModuleDict(self, htmlStr):
        moduleDict = {}
        soup = BeautifulSoup(htmlStr, 'html.parser', from_encoding='utf-8')

        # ------------------------------------------------基本信息------------------------------------------------
        基本信息_element = soup.find(class_="resume-content__candidate-basic")
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

        # moduleJson = json.dumps(moduleDict, ensure_ascii=False)
        # print(moduleJson)

        return moduleDict

    def parseResumeHtmlModule(self, moduleDict):
        print('\n------------------------------------------------基本信息------------------------------------------------')
        基本信息 = moduleDict['基本信息']
        self.getSeekerBaseInfo(基本信息)

        print('\n------------------------------------------------求职意向------------------------------------------------')
        求职意向 = moduleDict['求职意向']
        self.getJobHuntBaseInfo(求职意向)

        print('\n------------------------------------------------教育经历------------------------------------------------')
        教育经历 = moduleDict['教育经历']
        self.getEduBaseInfo(教育经历)

        print('\n------------------------------------------------工作经验------------------------------------------------')
        工作经验 = moduleDict['工作经验']
        self.getWorkExpBaseInfo(工作经验)

        print('\n------------------------------------------------项目经验------------------------------------------------')
        项目经验 = moduleDict['项目经验']
        self.getProjectExpBaseInfo(项目经验)

        print('\n------------------------------------------------专业技能------------------------------------------------')
        专业技能 = moduleDict['专业技能']
        self.getSkillBaseInfo(专业技能)

        print('\n------------------------------------------------自我评价------------------------------------------------')
        自我评价 = moduleDict['自我评价']
        self.getSelfEvalBaseInfo(自我评价)

        print('\n------------------------------------------------培训经历------------------------------------------------')
        培训经历 = moduleDict['培训经历']
        self.getTrainBaseInfo(培训经历)

        # print('\n------------------------------------------------所获证书------------------------------------------------')
        # 所获证书 = moduleDict['所获证书']
        #
        # print('\n------------------------------------------------在校情况------------------------------------------------')
        # 在校情况 = moduleDict['基本信息']
        #
        # print('\n------------------------------------------------语言能力------------------------------------------------')
        # 语言能力 = moduleDict['语言能力']

    def getSeekerBaseInfo(self, 基本信息):
        soup = BeautifulSoup(基本信息, 'html.parser', from_encoding='utf-8')
        性别 = soup.find('span', attrs={'data-bind': '$key: genderDesc'}).text
        print("性别:", 性别)

    def getJobHuntBaseInfo(self, 求职意向):
        pass

    def getTrainBaseInfo(self, 培训经历):
        pass

    def getSelfEvalBaseInfo(self, 自我评价):
        pass

    def getSkillBaseInfo(self, 专业技能):
        pass

    def getProjectExpBaseInfo(self, 项目经验):
        pass

    def getWorkExpBaseInfo(self, 工作经验):
        pass

    def getEduBaseInfo(self, 教育经历):
        pass


if __name__ == '__main__':
    zhilian = ResumeParserPlugHtmlZhilianInbox()
    htmlPath = '/Users/admin/Desktop/简历解析/智联招聘/智联招聘-插件-已下载模块-openFrom-2-李宁-直接报错.html'
    htmlStr = zhilian.readFile(htmlPath)
    moduleDict = zhilian.getResumeModuleDict(htmlStr)
    zhilian.parseResumeHtmlModule(moduleDict)
