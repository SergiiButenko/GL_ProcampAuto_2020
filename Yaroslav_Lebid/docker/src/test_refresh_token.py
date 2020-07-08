import pytest
import time

class Token_Tests:
    def test_renew_access_token(self, sessionUnderTest):
        time.sleep(10) # Sleep for 2 minutes befor Token exp date check
        if not sessionUnderTest.is_token_alive():
            sessionUnderTest.renew_access_token()
        assert sessionUnderTest.is_token_alive()