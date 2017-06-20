# -*- coding: utf-8 -*-
# This file is part of correosexpress. The COPYRIGHT file at the top level of
# this repository contains the full copyright notices and license terms.


def correosexpress_url(debug=False):
    """
    correos express URL connection

    :param debug: If set to true, use Envialia test URL
    """
    if debug:
        return 'https://test.correosexpress.com/wspsc/apiRestGrabacionEnvio/json/grabacionEnvio'
    else:
        return 'https://www.correosexpress.com/wpsc/apiRestGrabacionEnvio/json/grabacionEnvio'
