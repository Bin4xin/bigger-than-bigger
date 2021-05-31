package com.inspur.tsce4.login;

import com.inspur.tsce4.utils.ExecuteUtil;
import com.inspur.tsce4.utils.TSCEInit;
import org.json.JSONObject;

public class Command {
    private String vertifyScriptPath;

    public Command() {
        this.vertifyScriptPath = TSCEInit.scriptPath + "/userAuth.sh";
    }

    public JSONObject vertifyUser(String username, String password) {
        StringBuffer passwordBf = new StringBuffer();
        passwordBf.append("'");
        passwordBf.append(password);
        passwordBf.append("'");
        String passwordInfo = passwordBf.toString();
        JSONObject result = ExecuteUtil.doCommand(this.vertifyScriptPath + " " + username + " " + passwordInfo);
        return result;
    }
}
