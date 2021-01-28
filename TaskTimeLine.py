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

# points=[]
starttime=0
tasknames = []
timeline = []
isrecord=False

def RecordStart(task):
    global timeline,starttime,isrecord
    if(isrecord == False) :
        return

    strtask = str(task) 
    index = 1
    while(strtask in tasknames): 
        index = index + 1
        strtask = str(task) + '(' + str(index) + ')' # 当函数被多次调用的时候, 这个index会自动增长. index也就是调用次数 
    

    timeline.append({
        "task":strtask,
        "startTime":time.time() -  starttime,
        "endTime":0,
        "status":0
    })
    tasknames.append(strtask)

def RecordEnd(task,success=1):
    '''
    在多线程的模式下 这里可能有bug, 因为endtime 不一定跟startime是配套的.多线程下,请自己保证task不会重复
    success=0 代表成功
    success=1 代表失败
    '''
    global timeline,starttime,isrecord
    if(isrecord == False) :
        return
    for x in timeline:
        if(x["task"].startswith(task) and x["endTime"] == 0):
            x["endTime"] = time.time() -  starttime
            x["status"] = success
    

def InitTimeLine():
    global timeline,starttime,isrecord,tasknames
    tasknames=[]
    timeline=[] 
    starttime = time.time()
    starttime = starttime +0
    isrecord = os.path.exists('timeline.log')

# 保存日志.
def SaveRecord():
    global timeline,starttime
    if (os.path.exists('timeline.log')):
        with open('timeline.log','w+',encoding='utf-8') as rwf:
            # rwf.write(str(points))
            # rwf.write('\n')
            rwf.write(str(timeline))
            rwf.write('\n')