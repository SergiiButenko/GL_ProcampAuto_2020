import time
from liubov_poplavska.api.api import API


def test_token_expired_and_renew():
    api = API(username='test', password='test')
    api.login()
    time.sleep(120)
    if api.session.is_expired():
        api.session.renew_token()
    assert api.get_items() is None




