import allure
from time import sleep


@allure.title('session access token expiration time and its renewal')
def test_access_token_expiration_and_renewal(test_session):
    """ verifies if the session access token gets expired in 120 seconds,
        and if it can be renewed
    """
    sleep(120)
    assert test_session.is_access_token_expired() is True
    test_session.renew_access_token()
    assert test_session.is_access_token_expired() is False
