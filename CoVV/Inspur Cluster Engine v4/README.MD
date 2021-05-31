## *CNVD编号：CNVD-C-2021-127844 - 浪潮ClusterEngine V4.0存在逻辑缺陷漏洞*

- 2021年 5月21日 星期日 00时11分58秒 CST
    - 最近一直在看代码，正好前两天在网上冲浪的时候看到浪潮的一个RCE，就拿过来分析一下试试看
- CST
    - 上传相关代码

先看`web.xml`定义的servlet；
```xml
<servlet>
    <servlet-name>login</servlet-name>
    <servlet-class>
        com.inspur.tsce4.login.Servlet
    </servlet-class>
</servlet>
```
