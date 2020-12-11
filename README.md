# TrImage2Text-开源的单机版OCR 识别率媲美大厂

## 介绍
TrImage2Text，基于开源项目 [Tr](https://github.com/myhub/tr) 的OCR识别。
由于项目 [Tr]加入了对Windows的支持，可以直接调用此项目接口进行识别。
UI部分借鉴了 [Image2Text](https://github.com/shuoGG1239/Image2Text)项目
整合后，不用调用API接口，不用注册申请，没有调用次数的限制，非常便于调试或日常使用。   


## 特性
* 中文识别  
快速高识别率，可以媲美甚至超过百度等API接口
 
* 文字检测  
支持一定角度的旋转  

* 单机  
不用调用API接口，不用繁琐的申请，安装即可使用。

* 注意  
由于调用的[Tr](https://github.com/myhub/tr)的限制，启动的时候需要联网验证，如需离线或授权请联系原作者。


## 安装需求
 
### 运行平台  
* ✔ Python 3.6+  
* ✔ Windows10

## 安装说明  
1. 安装python3.7  
    强烈推荐安装[anaconda](https://repo.anaconda.com/archive/),可以省去安装很多依赖，要安装windows64位的，比如[anaconda](https://repo.anaconda.com/archive/Anaconda3-2020.07-Windows-x86_64.exe)

2.  Windows系统需要安装[VC_redist.x64.exe](https://download.visualstudio.microsoft.com/download/pr/89a3b9df-4a09-492e-8474-8f92c115c51d/B1A32C71A6B7D5978904FB223763263EA5A7EB23B2C44A0D60E90D234AD99178/VC_redist.x64.exe
)

3. 安装依赖包  
``` shell script
pip install QCandyUi
pip install pyperclip
```  

4. 运行  
直接运行main方法
``` shell script
python main.py
```

5. 使用  
操作方法可以参考[Image2Text](https://github.com/shuoGG1239/Image2Text)的操作说明，很便捷

## 联系方式
Email: 250809345@qq.com

## Lisence  
Apache 2.0

## 鸣谢
* 感谢 [myhub](https://github.com/myhub) 和它的开源项目[Tr](https://github.com/myhub/tr) 
* 感谢 shuoGG1239的开源项目[Image2Text](https://github.com/shuoGG1239/Image2Text) 
  
如果你也喜欢这个项目，不妨给个star (^.^)✨