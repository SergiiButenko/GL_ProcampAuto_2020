import pytest
from .api import Session
from .testdata import testdata
from .utils import dispatchers


@pytest.fixture(scope='session', params=testdata.correct_credentials)
def test_session(request):
    dispatchers.server_dispatcher(timeout=5)
    session = Session(request.param)
    yield session
