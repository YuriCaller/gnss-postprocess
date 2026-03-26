# -*- coding: utf-8 -*-
"""
GNSS Post-Process PPK/PPP v2.0
Motor RTKLIB | Validación geodésica estricta | Ficha técnica IGN Perú
Autor: Ing. Yuri Fabian Caller Cordova — CIP 214377
"""
def classFactory(iface):
    from .plugin_main import GNSSPostProcessPlugin
    return GNSSPostProcessPlugin(iface)
