# Scopus2HistCite

非常欣喜地发现这个小脚本在他诞生后的数年后仍然有人在使用，甚至在得到公众号`科研利器`王老师的推荐。
![enter description here](https://leoatchina-notes-1253974443.cos.ap-shanghai.myqcloud.com/Notes/2019/1/7/1546838896763.png)

最初的脚本是windows下面写的，使用的是python2。以现在的眼光看来，写的很`丑陋`
虽然我现在早已转到用`OSX`作为我的主力使用系统,但是`HISTCITE`毕竟只有`WINDOWS`版本.
准备抽空改进一下, 谢谢给我鼓励的人们.

# 原来的介绍
个人工作中，经常会有这样的情况：从一篇或者几篇文章出发，找出此`领域`中被`引用`比较多，`开山祖师`级别的文献，作文献二次检索是比较容易想到的思路。

二次检索可以用scopus网站，不过怎么找出`二次检索`之后，哪些文献比较重要呢？很容易想到有类似功能的Histocite，感谢[罗昭锋的博客](http://blog.sciencenet.cn/?304685)等老师的大力推广，我在多年前就已经使用过这个软件进行文献检索。

经过观察 scopus的导出格式和 histcite的导入格式，发现其实hisctcite所需要的信息在scopus里都有，但是要经过一系列的加工，把无用的信息给去除，还要进行一系列的关键字代替。

代替过程，需逐行读入原来的ris文件
1. 第一行，写入`FN Thomson Reuters Web of Knowledge™`。第二行 写入`VR 1.0`
2. 原来ris文件，每篇文献记录间用单行隔开
3. 每篇文献由数行组成，每行开头两个字符有相应的意义，转成相应的histcite标记
```
            'TI', # title
            'T2', # jounal
            'AU', # author,这个代替最麻烦
            'VL', # volumn
            'IS', # issue
            'SP', # start page
            'EP', # end page
            'PY', # public year
            'DO' # doi ?这个不重要

```
4. 具体代替思路可见下图，其实读源代码更清楚
![enter description here](https://leoatchina-notes-1253974443.cos.ap-shanghai.myqcloud.com/Notes/2019/1/7/1546839456058.png)


# 重构完毕, 改进点

- 用python3代替了python2
- 代码写的更加清楚点,不像原来那么"丑"
- 基本思路和原来一样,搞清楚不同的`mark`是什么意思,搞清楚一条文章记录的"起转承接",作相应的代替

# 使用方法

- 推荐使用[文献引文分析利器 HistCite 详细使用教程暨 HistCite Pro 首发页面](https://zhuanlan.zhihu.com/p/20902898)，
- git clone我的repo或者直接下载 python脚本
- 从scopus网站导出文献记录，有两个注意点
    1. 要换成英文版scopus
    ![enter description here](https://leoatchina-notes-1253974443.cos.ap-shanghai.myqcloud.com/Notes/2019/1/7/1546839507355.png)
    2. 导出时，要选择ris格式，要注意把References选上。
    ![enter description here](https://leoatchina-notes-1253974443.cos.ap-shanghai.myqcloud.com/Notes/2019/1/7/1546839518150.png)
    3. 导出的文献名是**scopus.ris**，放在和`Scopus2Histcite.py`同一个目录下， 运行这个脚本 `python3 Scopus2Histcite.py`
    4. 或者放到任意位置， `python3  Scopus2Histcite.py \path\to\your\risfile`
    5. 会在当前目录下生成`savedres.txt`，用前面修改版的HistCite Pro导入。