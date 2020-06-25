package com.sshidlovsky.authentification.api.endpoints;

import java.io.File;

public enum EndpointsValues {

    LOGIN("http://localhost:5002/login"),
    ITEMS("http://localhost:5002/items"),
    REFRESH("http://localhost:5002/refresh");

    private final String value;

    private EndpointsValues(String value) {
        this.value = value;
    }

    public String getValue() {
        return value;
    }

}