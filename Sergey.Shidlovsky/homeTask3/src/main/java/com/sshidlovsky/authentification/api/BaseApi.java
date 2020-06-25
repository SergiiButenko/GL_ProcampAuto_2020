package com.sshidlovsky.authentification.api;

import com.sshidlovsky.authentification.dto.item.ItemsResponse;

public interface BaseApi {
    void login();
    void refresh();
    ItemsResponse getItems();
}
