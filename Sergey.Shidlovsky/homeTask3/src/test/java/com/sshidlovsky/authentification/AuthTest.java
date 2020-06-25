package com.sshidlovsky.authentification;

import com.sshidlovsky.authentification.dto.item.ItemsResponse;
import com.sshidlovsky.authentification.api.BaseApi;
import com.sshidlovsky.authentification.api.BaseApiImpl;

import org.junit.Test;

import static java.lang.Thread.sleep;
import static org.junit.Assert.assertNotNull;

public class AuthTest {

    private BaseApi baseApi = new BaseApiImpl("test", "test");

    @Test
    public void shouldGetItemsWithValidAccessToken() {
        baseApi.login();
        ItemsResponse items = baseApi.getItems();
        assertNotNull(items);
    }

    @Test
    public void shouldRefreshTokenAndGetItems() throws InterruptedException {
        baseApi.login();
        sleep(2 * 60000);
        ItemsResponse items = baseApi.getItems();
        assertNotNull(items);
    }
}
