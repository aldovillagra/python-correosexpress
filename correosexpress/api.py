# -*- coding: utf-8 -*-
# This file is part of correos express. The COPYRIGHT file at the top level of
# this repository contains the full copyright notices and license terms.
from correosexpress.utils import correosexpress_url_envio
from correosexpress.utils import correosexpress_url_etiqueta
from correosexpress.utils import correosexpress_url_seguimiento
import requests
from requests.auth import HTTPBasicAuth


class API(object):
    """
    Generic API to connect to correos express
    """
    __slots__ = (
        'url',
        'username',
        'password',
    )

    def __init__(self, username, password, operation, debug=False):
        """
        This is the Base API class which other APIs have to subclass. By
        default the inherited classes also get the properties of this
        class which will allow the use of the API with the `with` statement

        Example usage ::

            from correosexpress.api import API

            with API(username) as correosexpress_api:
                return correosexpress_api.test_connection()

        :param username: correos express API username
        :param password: correos express API password
        :param operation: correos express API operation type => 'envio', 'etiqueta', 'seguimiento'
        """
        if operation == 'envio':
            self.url = correosexpress_url_envio(debug)
        elif operation == 'etiqueta':
            self.url = correosexpress_url_etiqueta(debug)
        elif operation == 'seguimiento':
            self.url = correosexpress_url_seguimiento(debug)
        self.username = username
        self.password = password

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        pass

    def connect(self, data):
        """
        Connect to the Webservices and return JSON data from Correos express

        :param xml: JSON data.

        Return JSON object
        """
        headers = {'Content-type': 'application/json'}
        return requests.post(
            self.url, data=data,
            auth=HTTPBasicAuth(self.username, self.password),
            headers=headers, verify=False)

    def test_connection(self):
        """
        Test connection to Correos express webservices
        Send XML to Correos express and return error send data
        """
        headers = {'Content-type': 'application/json'}
        resp = requests.post(
            self.url, data='',
            auth=HTTPBasicAuth(self.username, self.password),
            headers=headers, verify=False)
        if resp.status_code == 200:
            return 'OK'
        else:
            return resp.text
