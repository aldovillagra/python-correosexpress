# -*- coding: utf-8 -*-
# This file is part of correosexpress. The COPYRIGHT file at the top level of
# this repository contains the full copyright notices and license terms.


def correosexpress_url_envio(debug=False):
    """
    correos express URL connection

    :param debug: If set to true, use Envialia test URL

    """
    if debug:
        # return 'https://test.correosexpress.com/wspsc/apiRestGrabacionEnvio/json/grabacionEnvio'
        return 'https://www.correosexpress.com/wpsc/apiRestGrabacionEnvio/json/grabacionEnvio'
    else:
        return 'https://www.correosexpress.com/wpsc/apiRestGrabacionEnvio/json/grabacionEnvio'



def correosexpress_url_etiqueta(debug=False):
    """
    correos express URL connection

    :param debug: If set to true, use Envialia test URL

    """
    if debug:
        return 'https://www.test.cexpr.es/wspsc/apiRestEtiquetaTransporte/json/etiquetaTransporte'
    else:
        return 'https://www.cexpr.es/wspsc/apiRestEtiquetaTransporte/json/etiquetaTransporte'



def correosexpress_url_seguimiento(debug=False):
    """
    correos express URL connection

    :param debug: If set to true, use Envialia test URL

    """
    if debug:
        return 'https://www.correosexpress.com/wpsc/apiRestSeguimientoEnvios/rest/seguimientoEnvios'
    else:
        return 'https://www.correosexpress.com/wpsc/apiRestSeguimientoEnvios/rest/seguimientoEnvios'