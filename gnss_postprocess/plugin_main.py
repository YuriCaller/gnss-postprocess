# -*- coding: utf-8 -*-
import os
from qgis.PyQt.QtWidgets import QAction, QDockWidget
from qgis.PyQt.QtGui import QIcon
from qgis.PyQt.QtCore import Qt


class GNSSPostProcessPlugin:
    """Punto de entrada del plugin en QGIS."""

    def __init__(self, iface):
        self.iface      = iface
        self.plugin_dir = os.path.dirname(__file__)
        self.action     = None
        self.dock       = None

    def initGui(self):
        icon_path = os.path.join(self.plugin_dir, 'icons', 'icon.png')
        self.action = QAction(
            QIcon(icon_path) if os.path.exists(icon_path) else QIcon(),
            'GNSS Post-Process PPK/PPP',
            self.iface.mainWindow()
        )
        self.action.triggered.connect(self.toggle_panel)
        self.iface.addToolBarIcon(self.action)
        self.iface.addPluginToMenu('&GNSS Post-Process', self.action)

    def toggle_panel(self):
        if self.dock is None:
            from .ui.main_dialog import GNSSMainDialog
            self.dock = QDockWidget('GNSS Post-Process v2', self.iface.mainWindow())
            self.dock.setAllowedAreas(Qt.LeftDockWidgetArea | Qt.RightDockWidgetArea)
            self.dock.setMinimumWidth(460)
            self.widget = GNSSMainDialog(self.iface, self.plugin_dir)
            self.dock.setWidget(self.widget)
            self.iface.mainWindow().addDockWidget(Qt.RightDockWidgetArea, self.dock)
        else:
            self.dock.setVisible(not self.dock.isVisible())

    def unload(self):
        self.iface.removePluginMenu('&GNSS Post-Process', self.action)
        self.iface.removeToolBarIcon(self.action)
        if self.dock:
            self.iface.mainWindow().removeDockWidget(self.dock)
            self.dock = None
