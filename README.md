# Scopus2Histcite
非常欣喜地发现这个小脚本在他诞生后的数年后仍然有人在使用，甚至在知乎专栏上都有人推荐。
最初的脚本是windows下面写的，使用的是python2。以现在的眼光看来，写的很`丑陋`
虽然我现在早已转到用`OSX`作为我的主力使用系统,但是`HISTCITE`毕竟只有`WINDOWS`版本.
准备抽空改进一下, 谢谢给我鼓励的人们.
-----
重构完毕, 改进点
- 用python3代替了python2
- 代码写的更加清楚点,不像原来那么"丑"
- 基本思路和原来一样,搞清楚不同的"mark"是什么意思,搞清楚一条文章记录的"起转承接",作相应的代替

# 使用方法
- 推荐使用[罗昭锋老师博客](http://blog.sciencenet.cn/home.php?mod=space&uid=304685&do=blog&id=383399)上下载的修改版的HISTCITE
- 从scopus网站导出时有几个注意点 [我的简书上有截图](https://www.jianshu.com/p/47f9547187b4)
    1. 要换成英文版scopus
    2. 导出时，要选择ris格式，要注意把References选上。
    3. 导出的文献名是**scopus.ris**，放在这和`Scopus2Histcite.py`同一个目录下， 运行这个脚本
    4. 或者放到任意位置， `Scopus2Histcite.py \path\to\your\risfile`
    5. 会在当前目录下生成`savedres.txt`，用前面修改版的histcite导入。