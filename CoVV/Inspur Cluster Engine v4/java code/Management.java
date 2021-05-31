
package com.inspur.tsce4.login;

import com.inspur.tsce4.utils.JsonUtil;
import java.util.Date;
import java.util.HashMap;
import javax.servlet.http.Cookie;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import org.json.JSONException;
import org.json.JSONObject;

public class Management {
    HttpServletRequest request;
    HttpServletResponse response;
    Command command = new Command();
    private static HashMap<String, Date> clearUserList = new HashMap();
    JSONObject nullResJson = new JSONObject();

    public Management(HttpServletRequest request, HttpServletResponse response) {
        this.request = request;
        this.response = response;

        try {
            this.nullResJson.put("result", "error");
            this.nullResJson.put("info", "未获得操作结果");
        } catch (JSONException var4) {
            var4.printStackTrace();
        }

    }

    public void doResponse() {
        try {
            String operation = this.request.getParameter("op");
            JSONObject noOpErrorJson = new JSONObject();
            noOpErrorJson.putOpt("result", "error");
            noOpErrorJson.put("info", "找不到匹配的操作");
            if (operation != null && !"".equals(operation)) {
                if ("login".equals(operation)) {
                    this.login();
                } else if ("loginOut".equals(operation)) {
                    this.loginOut();
                } else if ("getCookie".equals(operation)) {
                    this.getCookie();
                } else if ("clearAUser".equals(operation)) {
                    this.clearAUser();
                } else {
                    JsonUtil.respnseJson(this.response, noOpErrorJson.toString());
                }
            } else {
                JsonUtil.respnseJson(this.response, noOpErrorJson.toString());
            }
        } catch (JSONException var3) {
            var3.printStackTrace();
        }

    }

    private void login() {
        String username = this.request.getParameter("username");
        String password = this.request.getParameter("password");
        JSONObject result = this.command.vertifyUser(username, password);
        if (result != null && result.length() != 0) {
            try {
                if (result.get("exitcode").equals(0)) {
                    Cookie cookieUser = new Cookie("username", username);
                    cookieUser.setMaxAge(604800);
                    cookieUser.setPath("/");
                    cookieUser.setHttpOnly(true);
                    this.response.addCookie(cookieUser);
                    String type = "";
                    if (username.equals("root")) {
                        type = "administrator";
                    } else {
                        type = "users";
                    }

                    Cookie userType = new Cookie("userType", type);
                    userType.setMaxAge(43200);
                    userType.setPath("/");
                    userType.setHttpOnly(true);
                    this.response.addCookie(userType);
                    Cookie cookieAuth = new Cookie("vertifyUser", "true");
                    cookieAuth.setMaxAge(43200);
                    cookieAuth.setPath("/");
                    cookieAuth.setHttpOnly(true);
                    this.response.addCookie(cookieAuth);
                    Cookie cookieDate = new Cookie("L_TIMES", Long.toString((new Date()).getTime()));
                    cookieDate.setMaxAge(604800);
                    cookieDate.setPath("/");
                    cookieDate.setHttpOnly(true);
                    this.response.addCookie(cookieDate);
                }
            } catch (JSONException var9) {
                var9.printStackTrace();
            }

            JsonUtil.respnseJson(this.response, result.toString());
        } else {
            JsonUtil.respnseJson(this.response, this.nullResJson.toString());
        }

    }

    private void loginOut() {
        JSONObject result = new JSONObject();
        Cookie cookieAuth = new Cookie("vertifyUser", "false");
        cookieAuth.setMaxAge(86400);
        cookieAuth.setPath("/");
        cookieAuth.setHttpOnly(true);
        this.response.addCookie(cookieAuth);

        try {
            result.put("result", "true");
            JsonUtil.respnseJson(this.response, result.toString());
        } catch (JSONException var4) {
            JsonUtil.respnseJson(this.response, this.nullResJson.toString());
        }

    }

    private void clearAUser() throws JSONException {
        JSONObject result = new JSONObject();
        String username = this.request.getParameter("username");
        clearUserList.put(username, new Date());

        try {
            result.put("result", "true");
            JsonUtil.respnseJson(this.response, result.toString());
        } catch (JSONException var4) {
            JsonUtil.respnseJson(this.response, this.nullResJson.toString());
        }

    }

    private void getCookie() {
        String key = this.request.getParameter("name");
        JSONObject result = new JSONObject();
        Cookie[] cookies = this.request.getCookies();
        Cookie cookie = null;
        Cookie userCookie = null;
        Cookie L_TIMES_cookie = null;
        if (cookies != null) {
            for(int i = 0; i < cookies.length; ++i) {
                if (cookies[i].getName().equals(key)) {
                    cookie = cookies[i];
                } else if (cookies[i].getName().equals("username")) {
                    userCookie = cookies[i];
                } else if (cookies[i].getName().equals("L_TIMES")) {
                    L_TIMES_cookie = cookies[i];
                }
            }
        }

        if (userCookie == null && key.equals("username")) {
            userCookie = cookie;
        }

        if (clearUserList.containsKey(userCookie.getValue()) && userCookie != null && key.equals("vertifyUser")) {
            Long now = (new Date()).getTime();
            Long addTime = ((Date)clearUserList.get(userCookie.getValue())).getTime();
            if (now - addTime > 43200000L) {
                clearUserList.remove(userCookie.getValue());
            } else if (addTime - Long.parseLong(L_TIMES_cookie.getValue()) > 0L) {
                Cookie cookieAuth = new Cookie("vertifyUser", "false");
                cookieAuth.setMaxAge(43200);
                cookieAuth.setPath("/");
                cookieAuth.setHttpOnly(true);
                this.response.addCookie(cookieAuth);
                cookie = null;
            }
        }

        try {
            if (cookie != null) {
                result.put("result", "true");
                result.put("value", cookie.getValue());
            } else {
                result.put("result", "false");
            }

            JsonUtil.respnseJson(this.response, result.toString());
        } catch (JSONException var10) {
            JsonUtil.respnseJson(this.response, this.nullResJson.toString());
        }

    }
}
