package com.sshidlovsky.authentification.api;

import com.fasterxml.jackson.databind.ObjectMapper;
import com.sshidlovsky.authentification.api.endpoints.EndpointsList;
import com.sshidlovsky.authentification.dto.JwtPayload;
import com.sshidlovsky.authentification.dto.RefreshResponse;
import com.sshidlovsky.authentification.dto.auth.AuthForm;
import com.sshidlovsky.authentification.dto.auth.AuthResponse;
import com.sshidlovsky.authentification.dto.item.ItemsResponse;

import org.springframework.http.HttpEntity;
import org.springframework.http.HttpHeaders;
import org.springframework.http.HttpMethod;
import org.springframework.http.ResponseEntity;
import org.springframework.util.Base64Utils;
import org.springframework.web.client.RestTemplate;

import lombok.SneakyThrows;

public class BaseApiImpl implements BaseApi {

    private String username;
    private String password;
    private AuthResponse authResponse;
    private RestTemplate restTemplate;

    public BaseApiImpl(String username, String password) {
        this.username = username;
        this.password = password;
        this.restTemplate = new RestTemplate();
    }

    public void login() {
        ResponseEntity<AuthResponse> authResponseEntity = restTemplate.postForEntity(
                EndpointsList.login,
                new AuthForm(username, password),
                AuthResponse.class);
        this.authResponse = authResponseEntity.getBody();
    }

    public ItemsResponse getItems() {
        refreshTokenIfExpired();

        HttpHeaders headers = new HttpHeaders();
        headers.add("Authorization", "Bearer " + authResponse.getAccessToken());
        HttpEntity httpEntity = new HttpEntity(headers);

        ResponseEntity<ItemsResponse> itemsResponseResponseEntity = restTemplate.exchange(
                EndpointsList.items,
                HttpMethod.GET,
                httpEntity,
                ItemsResponse.class);
        return itemsResponseResponseEntity.getBody();
    }

    public void refresh() {
        HttpHeaders headers = new HttpHeaders();
        headers.add("Authorization", "Bearer " + authResponse.getRefreshToken());
        HttpEntity httpEntity = new HttpEntity(headers);

        ResponseEntity<RefreshResponse> refreshResponseEntity = restTemplate.exchange(EndpointsList.refresh,
                HttpMethod.POST,
                httpEntity,
                RefreshResponse.class);
        authResponse.setAccessToken(refreshResponseEntity.getBody().getAccessToken());
    }


    public void refreshTokenIfExpired() {
        JwtPayload jwtPayload = getJwtPayload();
        if (jwtPayload.getExp() < System.currentTimeMillis() / 1000) {
            refresh();
        }
    }

    @SneakyThrows
    private JwtPayload getJwtPayload() {
        String jwtPayload = authResponse.getAccessToken().split("\\.")[1];
        return new ObjectMapper().readValue(Base64Utils.decodeFromString(jwtPayload), JwtPayload.class
        );
    }
}
