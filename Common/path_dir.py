#coding=utf-8
import os
#梳理文件路径
path=os.path.abspath(__file__)


#给路径做两层切割,结果是元祖
path_dir=os.path.split(os.path.split(path)[0])[0]


#截屏的存放路径
screenshots_dir=os.path.join(path_dir+"/Outputs/screen_shots")





