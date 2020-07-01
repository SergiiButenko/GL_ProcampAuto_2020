import pytest
import allure
from requests import HTTPError
from ..utils import helpers
from ..testdata import testdata


@pytest.fixture
def resource_creation_fixture(test_session):
    """
        SETUP for tests requiring preliminary creation of a resource.
        Uses authorization_fixture for getting an access token.
        Yields resource ID, the resource created as a json, and the access token to the tests related
    """
    resource = testdata.resource
    server_response, resource_id = test_session.create_resource(test_session.access_token, resource)
    if helpers.status_code_is_2xx(server_response) is False:
        raise Exception('Error is SETUP: Resource creation failed')
    yield resource_id, resource


@allure.title('Creation of the resource')
def test_resource_creation(test_session):
    """ Verifies that a resource can be created given a proper token obtained after authorization """
    server_response, _ = test_session.create_resource(access_token=test_session.access_token, resource=testdata.resource)
    assert helpers.status_code_is_2xx(server_response)


@allure.title('Reading of the resource by its ID')
def test_resource_reading(test_session, resource_creation_fixture):
    """ Verifies a resource can be read by its ID given a proper token obtained after authorization """
    resource_id, created_resource = resource_creation_fixture
    server_response, resource_content = test_session.read_resource(test_session.access_token, resource_id)
    assert helpers.status_code_is_2xx(server_response)
    assert resource_content == created_resource


@allure.title('Deletion of the resource by its ID')
def test_resource_deletion(test_session, resource_creation_fixture):
    """ Verifies a resource can be deleted by its ID given a proper token obtained after authorization """
    resource_id, _ = resource_creation_fixture
    server_response = test_session.delete_resource(test_session.access_token, resource_id)
    assert helpers.status_code_is_2xx(server_response)
    with pytest.raises(HTTPError):
        server_response = test_session.delete_resource(test_session.access_token, resource_id)
        server_response.raise_for_status()


@allure.title('Creation of the resource with no token')
@pytest.mark.parametrize('token', testdata.empty_tokens)
def test_resource_creation_with_bad_token(test_session, token):
    """ Verifies impossibility to create a resource with no or an empty access token """
    server_response, _ = test_session.create_resource(token, testdata.resource)
    with pytest.raises(HTTPError):
        server_response.raise_for_status()
