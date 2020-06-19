import pytest
from .utils import launchers
from .config import Configs


@pytest.fixture(scope='session')
def server_handler():
    """ SETUP: runs the test server at the start of the session
        TEARDOWN: stops it as the session concludes
    """
    server = launchers.start_server(Configs.local_link_to_server)
    yield
    launchers.stop_server(server)
