package com.klysenko.authentication;

public final class EndPoints {

    private static String getHost() {
        String appHost = System.getenv("SIMPLE_APP_HOST");
        String appPort = System.getenv("SIMPLE_APP_PORT");
        if (appHost != null && appPort != null) {
            return "http://" + appHost + ":" + appPort;
        } else {
            return "http://localhost:5002";
        }
    }

    public static String getLogin() {
        return getHost() + "/login";
    }

    public static String getItems() {
        return getHost() + "/items";
    }

    public static String getRefresh() {
        return getHost() + "/refresh";
    }
}



