#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2020/4/29 10:43
# @Author: xk
# @File  : resume_parser_plug_html_zhilian_inbox.py
import json

from bs4 import BeautifulSoup


class ResumeParserPlugHtmlZhilianInbox(object):

    # 读取html文件
    def func_read_file(self, htmlPath):
        html = open(htmlPath, mode='r', encoding='utf-8').read()
        return html

    # 将html简历按照板块区分
    def func_get_resume_module_dict(self, htmlStr):
        moduleDict = {}
        soup = self.func_soup_html(htmlStr)

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

    def func_parse_resume_html_module(self, moduleDict):
        print('\n------------------------------------------------基本信息------------------------------------------------')
        基本信息 = moduleDict['基本信息']
        self.func_get_seeker_base_info(基本信息)

        print('\n------------------------------------------------求职意向------------------------------------------------')
        求职意向 = moduleDict['求职意向']
        self.getJobHuntBaseInfo(求职意向)

        print('\n------------------------------------------------教育经历------------------------------------------------')
        教育经历 = moduleDict['教育经历']
        self.func_get_edu_baseinfo(教育经历)

        print('\n------------------------------------------------工作经验------------------------------------------------')
        工作经验 = moduleDict['工作经验']
        self.func_get_work_exp_baseinfo(工作经验)

        print('\n------------------------------------------------项目经验------------------------------------------------')
        项目经验 = moduleDict['项目经验']
        self.func_get_project_exp_baseInfo(项目经验)

        print('\n------------------------------------------------专业技能------------------------------------------------')
        专业技能 = moduleDict['专业技能']
        self.func_get_skill_baseInfo(专业技能)

        print('\n------------------------------------------------自我评价------------------------------------------------')
        自我评价 = moduleDict['自我评价']
        self.func_get_self_eval_baseInfo(自我评价)

        print('\n------------------------------------------------培训经历------------------------------------------------')
        培训经历 = moduleDict['培训经历']
        self.func_get_train_baseinfo(培训经历)

    # 用BeautifulSoup亲吻一遍html
    def func_soup_html(self, baseText):
        soup = BeautifulSoup(baseText, 'html.parser', from_encoding='utf-8')
        return soup

    def func_get_seeker_base_info(self, 基本信息):
        soup = self.func_soup_html(基本信息)

        姓名 = soup.find('span', attrs={'data-bind': 'textQ: candidateName'}).text
        性别 = soup.find('span', attrs={'data-bind': '$key: genderDesc'}).text
        年龄 = soup.find('span', attrs={'data-bind': 'text: age'}).text
        工作年限 = soup.find('span', attrs={'data-bind': 'text: workYears'}).text
        学历 = soup.find('span', attrs={'data-bind': 'text: eduLevel()'}).text
        当前城市 = soup.find('span', attrs={'data-bind': 'textQ: currentCity()'}).text
        户口 = soup.find('span', attrs={'data-bind': 'textQ: hukou()'}).text
        手机 = soup.find('span', attrs={'data-bind': 'textQ: mobilePhone'}).text
        邮箱 = soup.find('span', attrs={'data-bind': 'textQ: email'}).text

        print("姓名:%s\n性别:%s\n年龄:%s\n工作年限:%s\n学历:%s\n当前城市:%s\n户口:%s\n手机:%s\n邮箱:%s"
              % (姓名, 性别, 年龄, 工作年限, 学历, 当前城市, 户口, 手机, 邮箱))

    def func_get_jobhunt_baseinfo(self, 求职意向):
        soup = self.func_soup_html(求职意向)
        keys = soup.find('dl', attrs={'data-bind': "foreach: { data: intents, as: 'intent' }"}).find_all('dt')
        values = soup.find('dl', attrs={'data-bind': "foreach: { data: intents, as: 'intent' }"}).find_all('dd')
        jobHuntDict = {}
        for key_index, key_info in enumerate(keys):
            key = key_info.text
            val = values[key_index]
            jobHuntDict[key] = val.text

        print('jobHuntDict',jobHuntDict)


    def func_get_train_baseinfo(self, 培训经历):
        pass

    def func_get_self_eval_baseInfo(self, 自我评价):
        pass

    def func_get_skill_baseInfo(self, 专业技能):
        pass

    def func_get_project_exp_baseInfo(self, 项目经验):
        pass

    def func_get_work_exp_baseinfo(self, 工作经验):
        '''
        :param 工作经验:
        :return:
        '''

    def func_get_edu_baseinfo(self, 教育经历):
            pass


if __name__ == '__main__':
    zhilian = ResumeParserPlugHtmlZhilianInbox()
    htmlPath = '/Users/admin/Desktop/简历解析/智联招聘/智联招聘-插件-已下载模块-openFrom-2-李宁-直接报错.html'
    htmlStr = zhilian.func_read_file(htmlPath)
    moduleDict = zhilian.func_get_resume_module_dict(htmlStr)
    zhilian.func_parse_resume_html_module(moduleDict)
