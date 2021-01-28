文档请查看 https://blog.csdn.net/phker/article/details/113254416

项目源代码 https://github.com/phker/SystemTimeLine

效果图
![image](https://img-blog.csdnimg.cn/20210128091457277.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3Boa2Vy,size_16,color_FFFFFF,t_70)

```python
import time
from profile.TaskTimeLine import RecordStart,RecordEnd,InitTimeLine,SaveRecord 

def 起床程序(record):   
    InitTimeLine() 
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
 
    RecordStart( "起床" )
```
