---
layout: podcasts
title: "Welly开发者汤洋、吕笠：谁有热情谁就有ownership"
date: 2020-09-10
slug: 3
length: "59 mins"
img: 03-welly.png
tags: ["软件"]
description: "汤洋和吕笠在大学时代和几个小伙伴做了Welly，一个在MacOS上运行的BBS客户端，用于访问各大BBS论坛。十几年后的现在也一直在维护中，下载量达到了十万附近。今天我和这两位嘉宾在一起谈谈Welly制作缘由、制作趣闻、所有权，外加BBS社群、开源软件社群之轶事一二。"
audio: "https://d3ctxlq1ktw2nl.cloudfront.net/staging/2020-8-9/b27ceb1a-6382-af1b-edd4-30481ee08ef3.mp3"
---


{{< rawhtml >}}
    <audio class="customPlayer" src="https://d3ctxlq1ktw2nl.cloudfront.net/staging/2020-8-9/b27ceb1a-6382-af1b-edd4-30481ee08ef3.mp3" title="Welly开发者汤洋、吕笠：谁有热情谁就有ownership" data-artist="闭门造车" controls>
        Your browser does not support the <code>audio</code> element.
    </audio>
{{< /rawhtml >}}

汤洋和吕笠在大学时代和几个小伙伴做了Welly，一个在MacOS上运行的BBS客户端，用于访问各大BBS论坛。十几年后的现在也一直在维护中，下载量达到了十万附近。今天我和这两位嘉宾在一起谈谈Welly的制作缘由、制作趣闻、所有权，外加BBS社群、开源软件社群之轶事一二。

⚠️ 警告：本集含有一定浓度的MacOS和软件开发这两个方面的黑话。虽然不太影响收听效果，但是为了补偿在录音过程中忘记解释的名词，我在show notes里加了相关链接。

感想、建议和参与，请发邮件到[gulugulufm@gmail.com](mailto:gulugulufm@gmail.com)，或者在豆瓣上[豆油Miki](https://www.douban.com/people/49489567/)。


### 🗣 出场人物

吕笠：[LinkedIn](https://www.linkedin.com/in/li-lu-77110715), [Medium](https://medium.com/@lilu_98243)

汤洋：[LinkedIn](https://www.linkedin.com/in/tangyang/), [Twitter](https://twitter.com/tangyang), [Telegram](https://t.me/ytang)

Miki ：[豆瓣](https://www.douban.com/people/49489567/), [Telegram](https://t.me/liquid_raspberry)


### 🔗 相关链接

Welly：在[Google Code](https://code.google.com/archive/p/welly/)

Welly：在[Mac App Store](https://apps.apple.com/cn/app/id1521402269)

Nally：在[Google Code](https://code.google.com/archive/p/nally/)

水木社区：[newsmth.net](https://www.newsmth.net/index.html)

未名空间：[mitbbs.com](https://www.mitbbs.com/)

批踢踢：[ptt.cc](https://www.ptt.cc/)

闭门造车播客的友情链接：[湾上说规划](https://podcasts.apple.com/us/podcast/%E6%B9%BE%E4%B8%8A%E8%AF%B4%E8%A7%84%E5%88%92/id1512902746)


### 🧐 名词解释

##### 开源软件和社区

- [Apache](https://www.apache.org/): 一个[开源软件基金会](https://zh.wikipedia.org/wiki/Apache软件基金会)
- [Apache Hadoop](https://hadoop.apache.org/): Apache管理的[一个项目](https://zh.wikipedia.org/wiki/Apache_Hadoop)
- [PMC](https://www.apache.org/dev/pmc.html#what-is-a-pmc): Project Management Committee，项目管理委员会
- [Github](https://github.com/)：一个[存放代码的网站兼开发者社群](https://zh.wikipedia.org/wiki/GitHub)
- [Google code](https://code.google.com/archive/)：谷歌提供的[开源软件管理平台](https://zh.wikipedia.org/wiki/Google開發人員)，现已变为只读状态

##### 苹果电脑的芯片

一般来说，一个准备好了的程序只能在特定的某一种芯片（CPU）上运行。但最近15年间苹果电脑曾经有两次芯片的改变，导致开发者需要对这种情况为程序做出改动。具体来说，
- 从90年代到2005年，苹果电脑使用[PowerPC](https://zh.wikipedia.org/wiki/PowerPC)芯片（播客中提到的名字是它的简称PPC)。
- 2005-2020年间，苹果MacBook使用[Intel x86](https://en.wikipedia.org/wiki/Apple–Intel_architecture)。为了帮助PowerPC的程序在Intel上也能运行，苹果发布了[Rosetta](https://zh.wikipedia.org/wiki/Rosetta)来帮助迁移。开发者这边的解决方案是发布[universal binary](https://zh.wikipedia.org/wiki/通用二进制)这种程序包，兼容两种CPU，使程序在两种CPU上都能运行。
- 2020年苹果宣布在所有的Mac上使用[ARM](https://zh.wikipedia.org/wiki/ARM架構)，行销手段上把Mac电脑和iPhone/iPad/Apple Watch等产品的芯片统一称为[Apple Silicon](https://zh.wikipedia.org/wiki/Apple_Silicon)。相对应的，博客中提到的Rosetta 2用来帮助把原有Intel版本的程序“翻译”成ARM版本。
更详细的综述可以参考阮一峰[苹果电脑为什么要换 CPU：Intel 与 ARM 的战争](http://www.ruanyifeng.com/blog/2020/06/cpu-architecture.html)。

##### 软件开发流程
- [fork](https://zh.wikipedia.org/wiki/分叉_(软件开发)): 完全复制一份，分叉成两个版本分别发展下去
- [patch](https://zh.wikipedia.org/wiki/Patch)：可以理解为源代码修改的记录
- [merge](https://zh.wikipedia.org/wiki/合并_(版本控制)): 合并其他人的代码，代表接受修改
- [commit](https://en.wikipedia.org/wiki/Commit_(version_control)): 提交代码
- [svn](https://zh.wikipedia.org/wiki/Subversion)：一个代码版本控制系统

##### 其他
- [API](https://zh.wikipedia.org/wiki/应用程序接口)：在节目中指苹果提供给开发者调用的各种功能
- [Growl](http://growl.info/)：Mac上用于发出提醒的工具
- [MSRA](https://www.msra.cn/): 微软亚洲研究院


### ⏳ 时间轴

01:18 开发者吕笠和汤洋

03:11 BBS不光是公告牌，更像是论坛、聊天室、即时通讯、email的合体

06:23 水木清华在05年的时候被fork成了两份

09:42 买了一台MacBook，发现在MacBook上没有相应的BBS灌水软件，就是这么开始的

13:21 给原先的团队想要贡献回去，但被无情地拒绝了

16:45 一个开源软件最开始都是为了满足自己的需求，因为我们要用，所以我们要做

24:04 Welly这样的软件，开源是最传统、最容易做出成果的方法

27:45 很多开源软件创造的初衷是希望有更多人使用，帮更多人解决问题

32:30 想让Welly在现在最新的系统上能正常运行其实是一件挺费劲的事

38:09 这个软件常用常新，始终跟随在时代的最前沿还是挺有意思的

40:49 Private API; Telnet BBS是没有任何格式信息的，全都要靠我们一些heuristics去猜

46:37 有的只是一腔热血（一个人的大学本科只有4年的时间）

50:21 第一次去参加WWDC这种大会的体验很难去用语言来形容

53:44 像一个澡堂子那样你一言我一语

57:18 微博和Twitter、请来联系闭门造车的Miki

58:12 友情链接：湾上说规划


### 🧨 花絮

{{< rawhtml >}}
    <audio class="customPlayer" src="https://storage.googleapis.com/firstory-709db.appspot.com/Record/ckcyy5sdwrbqi0870gfsgvdl9/1599570071932.mp3" title="我当时为了去WWDC差点连毕业照都没照上" data-artist="闭门造车·花絮" controls>
        Your browser does not support the <code>audio</code> element.
    </audio>
{{< /rawhtml >}}

{{< rawhtml >}}
    <audio class="customPlayer" src="https://storage.googleapis.com/firstory-709db.appspot.com/Record/ckcyy5sdwrbqi0870gfsgvdl9/1599570453113.mp3" title="WWDC里总能找到一个适合自己的地方" data-artist="闭门造车·花絮" controls>
        Your browser does not support the <code>audio</code> element.
    </audio>
{{< /rawhtml >}}

这期就到这里了。听到这里的话，不管你是从大学开始就混BBS的老用户，因为这期对从前的日子泛起过追忆，还是平时不玩BBS，觉得开启了新世界的大门，都可以到Mac App Store去试试Welly。感谢收听！
