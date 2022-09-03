import csv

from common.selenium_and_driver import selenium_And_driver


class pageOBject(object):
    def __int__(self,Driver=selenium_And_driver):
        self.driver = selenium_And_driver()

    def find_Element(self,*args):
        return self.driver.find_element(*args)
    #这是找单个元素的方法


    def find_Element(self,*args):
        return self.driver.find_elements(*args)
    #z这是找多个元素的方法

    def only_Element(self,my_text,*args):
        element_List =self.find_Elements(*args)
        for element in element_List:
            if element.text == my_text:
                return element.click()
    #这是从多个元素中找到自己想要元素的方法


    def subscript_Element(self,subscript,*args):
        element_List = self.find_Element(*args)
        return element_List[subscript].click()
    #这是从多个元素中找到自己所传下标元素并点击


    #CSV文件的读取

    def getCsvData(self,csv_file):
        file = open(file=csv_file, mode='r', encoding='gbk')
        # 把表格里面所有的数据读取,记录到reader对象
        reader = csv.reader(file)
        list = []
        for index, row in enumerate(reader, 1):
            list.append(row)
        return list

    #读取单行CSV数据
    #读取Excel/CSV表格数据,CSV_file读取的文件路径,line读取哪一行
    def getCsvDataByLine(self, csv_file, line):
        file = open(file=csv_file, mode='r', encoding='gbk')
        # 把表格里面所有的数据读取,记录到reader对象
        reader = csv.reader(file)
        for index, row in enumerate(reader, 1):
            # 判断行号是否和当前索引一样，如果一样，直接返回数据index，从1开始
            if index == line:
                file.close()
                return row


    def time_sleep(self,time):
        return time.sleep(time)


