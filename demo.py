
import time
from profile.TaskTimeLine import RecordStart,RecordEnd,InitTimeLine,SaveRecord



def 起床程序(record):   
    InitTimeLine() #一定要初始化一次,最好周期性的初始化,释放内存.
    RecordStart( "起床" )

    RecordStart( "睁开眼睛" )
    time.sleep(1)
    RecordEnd( "睁开眼睛" )

    RecordStart( "穿衣服" )
    time.sleep(1)
    RecordEnd( "穿衣服" )

    RecordStart( "洗脸" )
    time.sleep(1)
    RecordEnd( "洗脸" )

    RecordStart( "刷牙" )
    time.sleep(1)
    RecordEnd( "刷牙" )

    RecordStart( "吃早餐" )
    time.sleep(1)
    RecordEnd( "吃早餐" )
 
    RecordEnd( "起床" )

    SaveRecord() #保存性能记录