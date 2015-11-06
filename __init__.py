# -*- coding: utf-8 -*-
"""
/***************************************************************************
 Chat
                                 A QGIS plugin
 This plugin will let you chat live on the QGIS gitter channel
                             -------------------
        begin                : 2015-11-06
        copyright            : (C) 2015 by Tim Sutton
        email                : tim@qgis.org
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load Chat class from file Chat.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .qgis_chat import Chat
    return Chat(iface)
