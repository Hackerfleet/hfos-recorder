#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# HFOS - Hackerfleet Operating System
# ===================================
# Copyright (C) 2011-2019 Heiko 'riot' Weinen <riot@c-base.org> and others.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

__author__ = "Heiko 'riot' Weinen"
__license__ = "AGPLv3"

"""


Module Recorder
===============


"""

from influxdb import InfluxDBClient

from isomer.logger import debug, verbose
from isomer.component import ConfigurableComponent, handler


class Recorder(ConfigurableComponent):
    """
    The Recorder component receives new raw sensor data and
    repeats it over configurable tcp/udp/other means.

    """

    configprops = {
        'use_influx': {
            'type': 'boolean', 'default': True,
            'title': 'InfluxDB',
            'description': 'Use InfluxDB to store recorded data',
        },
        'influx_host': {'type': 'string', 'default': 'localhost'},
        'influx_port': {'type': 'integer', 'default': 8086},
        'influx_database': {'type': 'string', 'default': 'hfos_records'}
    }

    def __init__(self, *args):
        """
        Initialize the bus repeater component.

        :param args:
        """

        super(Recorder, self).__init__('RECORDER', *args)

        self.client = InfluxDBClient(
            host=self.configprops.influx_host,
            port=self.configprops.influx_port
        )

        databases_raw = self.client.get_list_database()

        databases = list((i['name'] for i in databases_raw))

        if self.configprops.influx_database not in databases:
            self.client.create_database(self.configprops.influx_database)

        self.client.switch_database(self.configprops.influx_database)

        self.current_position = {'lat': 0, 'lon': 0}

    @handler('read', channel='nmea')
    def read(self, data):
        """Handles incoming raw sensor data and records it to the specified database

        :param data: NMEA raw sentences incoming data
        """

        self.log('Received NMEA data:', data, lvl=debug)
        # self.log(data, pretty=True)

        # TODO: A sentence might contain multiple values, those should be mapped
        #   to the fields attribute accordingly.

        final_data = {
            'measurement': data.type,
            'time': data.timestamp,
            'coordinate': self.current_position,
            'fields': {
                data.value
            }
        }

        self.log('Recording final data:', final_data, pretty=True, lvl=debug)
        self.client.write_points(final_data)

    @handler('updateposition')
    def updateposition(self, event):
        """Updates the current recording geo-coordinate"""

        self.log('Updating position', lvl=verbose)
        self.current_position = event.vessel.geojson['coordinates']

