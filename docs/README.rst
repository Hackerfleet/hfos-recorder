HFOS - Recorder
===============

A navigational-data recorder with InfluxDB support (others planned, but not
recommended)

This plugin listens for HFOS navdata messages and records them to a configured
InfluxDB server.

Requirements
------------

This module has a few dependencies. To install them on Debian/Ubuntu:

.. code-block::

    apt-get install influxdb python3-influxdb
