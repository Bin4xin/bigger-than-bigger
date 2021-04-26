# *Collection of verified vulnerabilities*

## [*Apache Solr Rce cve-2019-0193*](https://github.com/Bin4xin/bigger-than-bigger/tree/master/CoVV/ApacheSolr)

- 有回显：
    - 找到利用核心 -> payload写入 -> RCE
    - [*点击以进一步了解*](https://github.com/Bin4xin/bigger-than-bigger/blob/master/CoVV/ApacheSolr/README.MD#-%E6%9C%89%E5%9B%9E%E6%98%BEpayload)
- 无回显：
    - 找到利用核心 -> payload写入 -> RCE
    - [*点击以进一步了解*](https://github.com/Bin4xin/bigger-than-bigger/blob/master/CoVV/ApacheSolr/README.MD#-%E6%97%A0%E5%9B%9E%E6%98%BEpayload)

### # 恶意xml引用
引用地址`(https://raw.githubusercontent.com/Bin4xin/bigger-than-bigger/master/CoVV/ApacheSolr/solr.xml)
`

### # 两者payload对比

[*点击以进一步了解*](https://github.com/Bin4xin/bigger-than-bigger/blob/master/CoVV/ApacheSolr/README.MD#-%E5%8C%BA%E5%88%AB)

### 参考

[漏洞分析 - Apache Solr远程代码执行漏洞(CVE-2019-0193)](https://xz.aliyun.com/t/5965)