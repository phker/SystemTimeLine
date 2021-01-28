import time
import os

'''
    使用示例
    Init()  # 先初始化, 每次记录一个.一般是业务开始的时候执行一次.
    check() # 第一步
    save()  # 第二步

    SaveRecord()
    
    def check():
        RecordStartPoint('check') # 第一行记录函数开始 确保save参数相同.
        *******
        RecordEndPoint('check') # 函数结束记录, 确保save参数相同.

    def save():
        RecordStartPoint('save') # 第一行记录函数开始 确保save参数相同.
        *******
        RecordEndPoint('save') # 函数结束记录, 确保save参数相同.
'''

timeline = []
# points=[]
starttime=0

def RecordPoint(ponitname,type):
    global timeline,starttime

    timeline.append( {
        "jobname":ponitname,
        "time":time.time() -  starttime,
        "type":type
    })


def InitTimeLine():
    global timeline,starttime

    timeline=[] 
    starttime = time.time()
    starttime = starttime +0

# 保存日志.
def SaveRecord():
    global timeline,starttime
    if (os.path.exists('timeline.log')):
        with open('timeline.log','w+',encoding='utf-8') as rwf:
            # rwf.write(str(points))
            # rwf.write('\n')
            rwf.write(str(timeline))
            rwf.write('\n')