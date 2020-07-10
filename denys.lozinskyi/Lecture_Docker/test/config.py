from urllib.parse import urljoin


class URLs:
    """ contains URLs and endpoints used in the project """

    base_url = 'http://simple-app:5002'

    # ENDPOINTS
    root_endpoint = '/'
    login_endpoint = '/login'
    protected_endpoint = '/protected'
    items_endpoint = '/items'
    refresh_endpoint = '/refresh'

    # Joint URLs (base url with endpoints)
    url_root = urljoin(base_url, root_endpoint)
    url_login = urljoin(base_url, login_endpoint)
    url_protected = urljoin(base_url, protected_endpoint)
    url_refresh = urljoin(base_url, refresh_endpoint)
    url_items = urljoin(base_url, items_endpoint)
