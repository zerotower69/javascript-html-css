# 测试18位的身份证号
import re
import time
import datetime

class JudgeRegExpOf18IDCardNumber:
    def __init__(self):
        self.year = 1800  # 年
        self.month = 1  # 月
        self.date = 1  # 日
        self.bigMonth = [1, 3, 5, 7, 8, 10, 12]  # 大月
        self.samllMonth = [4, 6, 9, 11]  # 小月
        self.judgeString = "18000100"
        self.ID = "0000180001000000"
        self.numOfJudgeWrong = 0
        self.numofWrongDate = 0
        self.numofAll = 0
        # 由于数据量过于庞大，删了，只测试 452722
        # self.preffixs=[str(preffix).zfill(6) for preffix in range(1000000)]  #身份证号前六位
        # 身份证号码后四位
        self.suffixs = [str(suffix).zfill(4) for suffix in range(10000)]+[str(suffix).zfill(
            3)+'X' for suffix in range(1000)]+[str(suffix).zfill(3)+'x' for suffix in range(1000)]
        self.file = open("./input18.txt", 'a')  # 打开文件
        self.judge = None
        # 编译正则
        self.pattern = re.compile(
            r'^[1-9]\d{5}((18|19|20|21)([0-9]{2}))(02(0[1-9]|[1-2][0-9])|(01|03|05|07|08|10|12)(0[1-9]|[1-2][0-9]|3[0-1])|(04|06|09|11)(0[1-9]|[1-2][0-9]|30))\d{3}[Xx\d]$')

    def addSelf(self):  # 日期向前加1
        self.date += 1

    def generateRightDate(self):  # 这是生成正确的日期
        if self.month == 2:
            if self.judgeYear():
                if self.date > 29:
                    self.date = 1
                    self.month += 1
            else:
                if(self.date > 28):
                    self.date = 1
                    self.month += 1
        elif (self.month in self.bigMonth):
            if(self.date > 31):
                self.date = 1
                self.month += 1
        elif self.month in self.samllMonth:
            if self.date > 30:
                self.date = 1
                self.month += 1
        if self.month > 12:
            self.month = 1
            self.year += 1
        return

    def generateAllDate(self):  # 生成所有的日期
        if(self.date > 31):
            self.month += 1
            self.date = 0
        if(self.month > 12):
            self.year += 1
            self.month = 1
        return
    # 闰年判断

    def judgeYear(self):
        if((self.year % 400 == 0) or ((self.year % 100 != 0) and (self.year % 4 == 0))):
            return True
        else:
            return False

    def print(self):
        print(str(self.year)+' '+str(self.month).zfill(2) +
              " "+str(self.date).zfill(2))
        return

    def getString(self):
        return str(self.year).zfill(4)+str(self.month).zfill(2)+str(self.date).zfill(2)

    def judgeStop(self):
        if self.year >= 2200:
            exit(0)

    def resetDate(self):
        self.year = 1800
        self.month = 1
        self.date = 0

    def validateDate(self):
        if(self.month == 2):
            if self.date < 30 and self.date != 0:
                return True
            else:
                return False
        elif self.month in self.bigMonth:
            if self.date < 32 and self.date != 0:
                return True
            else:
                return False
        elif self.month in self.samllMonth:
            if self.date < 31 and self.date != 0:
                return True
            else:
                return False

    def run(self):
        # 由于测试数据过多，我们只进行分段测试，也就是前六位做一段，7-14位一段 15-18位一段
        #又由于实际，我只是测试了7-14年和日期这一段，你也可以补充加入别的测试内容，但是要注意测试的内存占用和运行时间。
        while(self.year < 2200):
            if not self.validateDate():
                self.numofWrongDate += 1
            self.numofAll += 1
            self.ID = "452722"+self.getString()+"0000"
            self.judge = self.pattern.match(self.ID)
            if self.judge == None:
                self.numOfJudgeWrong += 1
                # self.file.write(self.ID+'\n')
            self.addSelf()
            self.generateAllDate()
        # self.resetDate()
        self.file.write("总数:"+str(self.numofAll) +
                        " 判断错误数:"+str(self.numOfJudgeWrong)+" 事实错误数:"+str(self.numofWrongDate)+"\n")
        self.file.close()


print("开始测试......")
test = JudgeRegExpOf18IDCardNumber()
start = time.time()
test.run()
end = time.time()
period = (end-start)
print("测试结束,共计用时"+str(period)+"s。")
