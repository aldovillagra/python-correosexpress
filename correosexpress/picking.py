# -*- coding: utf-8 -*-
# This file is part of correosexpress. The COPYRIGHT file at the top level of
# this repository contains the full copyright notices and license terms.
from correosexpress.api import API
import datetime
import json
from collections import OrderedDict
from base64 import decodestring


class Picking(API):
    """
    Picking API
    """
    __slots__ = ()

    def create(self, data):
        """
        Create delivery to Correos express

        :param data: Dict
        :return: reference (str), label(base64), error (str)
        """
        reference = None
        label = None
        error = None

        for k in data.keys():
            if data.get(k, '') is False:
                data[k] = ''
        vals = OrderedDict({
            'solicitante': data.get('solicitante')[:100],
            'canalEntrada': data.get('canalEntrada', '')[:30],
            'numEnvio': data.get('numEnvio', '')[:16],
            'ref': data.get('ref')[:20],
            'refCliente': data.get('refCliente', '')[:20],
            'fecha': datetime.datetime.now().strftime('%d%m%Y'),
            'codRte': data.get('codRte'),
            'nomRte': data.get('nomRte')[:30],
            'nifRte': data.get('nifRte')[:20],
            'dirRte': data.get('dirRte')[:50],
            'pobRte': data.get('pobRte')[:50],
            'codPosNacRte': data.get('codPosNacRte')[:5],
            'paisISORte': data.get('paisISORte', '')[:2],
            'codPosIntRte': data.get('codPosIntRte', '')[:7],
            'contacRte': data.get('contacRte', '')[:50],
            'telefRte': data.get('telefRte', '')[:15],
            'emailRte': data.get('emailRte', '')[:50],
            'codDest': data.get('codDest', ''),
            'nomDest': '',
            'nifDest': data.get('nifDest', '')[:20],
            'dirDest': '',
            'pobDest': '',
            'codPosNacDest': data.get('codPosNacDest'),
            'paisISODest': data.get('paisISODest', '')[:2],
            'codPosIntDest': data.get('codPosIntDest', '')[:7],
            'contacDest': data.get('contacDest')[:50],
            'telefDest': data.get('telefDest')[:15],
            'emailDest': data.get('emailDest', '')[:50],
            'contacOtrs': data.get('contacOtrs', '')[:50],
            'telefOtrs': data.get('telefOtrs', '')[:15],
            'emailOtrs': data.get('emailOtrs', '')[:50],
            'observac': data.get('observac', '')[:80],
            'numBultos': data.get('numBultos', '')[:2],
            'kilos': data.get('kilos')[:6],
            'volumen': data.get('volumen', '')[:5],
            'alto': data.get('alto', '')[:5],
            'largo': data.get('largo', '')[:5],
            'ancho': data.get('ancho', '')[:5],
            'producto': data.get('producto')[:2],
            'portes': data.get('portes')[:1],
            'reembolso': data.get('reembolso', '')[:7],
            'entrSabado': data.get('entrSabado', '')[:1],
            'seguro': data.get('seguro', '')[:7],
            'numEnvioVuelta': data.get('numEnvioVuelta', '')[:16],
            'listaBultos': '',
            'codDirecDestino': '',
            'password': data.get('password', ''),
            'listaInformacionAdicional':
                [OrderedDict({'tipoEtiqueta': data.get('tipoEtiqueta', '1'),
                              'etiquetaPDF': ''})],
        })
        if not data.get('codDirecDestino', False):
            vals['nomDest'] = data.get('nomDest')[:40]
            vals['dirDest'] = data.get('dirDest')[:50]
            vals['pobDest'] = data.get('pobDest')[:50]
        else:
            vals['codDirecDestino'] = data.get('codDirecDestino')[7]
            vals['nomDest'] = data.get('nomDest', '')[:40]
            vals['pobDest'] = data.get('pobDest', '')[:50]
        listabultos = []
        orden = 0
        for bulto in data.get('lista_bultos', []):
            orden += 1
            listabultos.append(OrderedDict({
                'codUnico': bulto.get('codUnico', '')[:23],
                'orden': orden,
                'codBultoCli': bulto.get('codBultoCli', '')[:40],
                'referencia': bulto.get('referencia', '')[:30],
                'descripcion': bulto.get('descripcion', '')[:50],
                'observaciones': bulto.get('observaciones', '')[:50],
                'kilos': bulto.get('Kilos', '')[:6],
                'volumen': bulto.get('volumen', '')[:5],
                'alto': bulto.get('Alto', '')[:5],
                'largo': bulto.get('Largo', '')[:5],
                'ancho': bulto.get('Ancho', '')[:5],
            }))
        vals['listaBultos'] = listabultos
        result = self.connect(json.dumps(vals))
        if result.json.get('codigoRetorno') == 0:
            reference = result.json.get('datosResultado')
            labels = []
            for label in result.json.get('etiqueta'):
                # hacemos doble decode porque la cadena
                # viene codificada 2 veces :S
                labels.append(
                    decodestring(decodestring(label.get('etiqueta1'))))
        else:
            return reference, labels, result.json.get('mensajeRetorno')
        return reference, labels, error

    def label(self, data):
        """
        Get PDF label from Correos express service

        :param data: Dictionary of values
        :return: label (base64)
        """
        raise NotImplementedError
