# -*- coding: utf-8 -*-
"""Test plugin for Picard Plugin API settings management.
"""
# Copyright (C) 2025 Bob Swift (rdswift)
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA
# 02110-1301, USA.

# pylint: disable=line-too-long
# pylint: disable=import-error
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals


from picard.plugin3.api import (
    BaseAction,
    PluginApi,
)


class TestSettings(BaseAction):
    NAME = 'Test API Settings'

    def __init__(self, api: PluginApi = None):
        super().__init__(api=api)
        self.api: PluginApi

    def callback(self, objs):
        self.api.logger.debug("Testing Test API Settings Plugin configuration management.")
        self.api.logger.info("Setting Test API Settings Plugin config 'bool_setting' to True")
        self.api.plugin_config['bool_setting'] = True
        self.api.logger.info("Getting Test API Settings Plugin config 'bool_setting': %s", self.api.plugin_config.get('bool_setting'))
        self.api.logger.info("Setting Test API Settings Plugin config 'bool_setting' to False")
        self.api.plugin_config['bool_setting'] = False
        self.api.logger.info("Getting Test API Settings Plugin config 'bool_setting': %s", self.api.plugin_config.get('bool_setting'))

        self.api.logger.info("Setting Test API Settings Plugin config 'int_setting' to 42")
        self.api.plugin_config['int_setting'] = 42
        self.api.logger.info("Getting Test API Settings Plugin config 'int_setting': %s", self.api.plugin_config.get('int_setting'))
        self.api.logger.info("Setting Test API Settings Plugin config 'int_setting' to -1")
        self.api.plugin_config['int_setting'] = -1
        self.api.logger.info("Getting Test API Settings Plugin config 'int_setting': %s", self.api.plugin_config.get('int_setting'))

        self.api.logger.info("Setting Test API Settings Plugin config 'float_setting' to 1.23")
        self.api.plugin_config['float_setting'] = 1.23
        self.api.logger.info("Getting Test API Settings Plugin config 'float_setting': %s", self.api.plugin_config.get('float_setting'))
        self.api.logger.info("Setting Test API Settings Plugin config 'float_setting' to -2.34")
        self.api.plugin_config['float_setting'] = -2.34
        self.api.logger.info("Getting Test API Settings Plugin config 'float_setting': %s", self.api.plugin_config.get('float_setting'))

        self.api.logger.info("Setting Test API Settings Plugin config 'str_setting' to 'Hello, World!'")
        self.api.plugin_config['str_setting'] = 'Hello, World!'
        self.api.logger.info("Getting Test API Settings Plugin config 'str_setting': %s", self.api.plugin_config.get('str_setting'))
        self.api.logger.info("Setting Test API Settings Plugin config 'str_setting' to 'All done.'")
        self.api.plugin_config['str_setting'] = 'All done.'
        self.api.logger.info("Getting Test API Settings Plugin config 'str_setting': %s", self.api.plugin_config.get('str_setting'))

        self.api.logger.info("Setting Test API Settings Plugin config 'list_setting' to ['one', 'two', 'three']")
        self.api.plugin_config['list_setting'] = ['one', 'two', 'three']
        self.api.logger.info("Getting Test API Settings Plugin config 'list_setting': %s", self.api.plugin_config.get('list_setting'))
        self.api.logger.info("Setting Test API Settings Plugin config 'list_setting' to ['A', 'B', 'C']")
        self.api.plugin_config['list_setting'] = ['A', 'B', 'C']
        self.api.logger.info("Getting Test API Settings Plugin config 'list_setting': %s", self.api.plugin_config.get('list_setting'))

        self.api.logger.info("Setting Test API Settings Plugin config 'dict_setting' to {'key1': 'value1', 'key2': 'value2'}")
        self.api.plugin_config['dict_setting'] = {'key1': 'value1', 'key2': 'value2'}
        self.api.logger.info("Getting Test API Settings Plugin config 'dict_setting': %s", self.api.plugin_config.get('dict_setting'))
        self.api.logger.info("Setting Test API Settings Plugin config 'dict_setting' to {'keyA': 'valueA', 'keyB': 'valueB'}")
        self.api.plugin_config['dict_setting'] = {'keyA': 'valueA', 'keyB': 'valueB'}
        self.api.logger.info("Getting Test API Settings Plugin config 'dict_setting': %s", self.api.plugin_config.get('dict_setting'))


class ClearSettings(BaseAction):
    NAME = 'Remove API Settings'

    def __init__(self, api: PluginApi = None):
        super().__init__(api=api)
        self.api: PluginApi

    def callback(self, objs):
        self.api.logger.debug("Removing Test API Settings Plugin configuration settings.")
        self.api.logger.info("Removing Test API Settings Plugin config 'bool_setting'")
        self.api.plugin_config.remove('bool_setting')
        self.api.logger.info("Getting Test API Settings Plugin config 'bool_setting': %s", self.api.plugin_config.get('bool_setting'))

        self.api.logger.info("Removing Test API Settings Plugin config 'int_setting'")
        self.api.plugin_config.remove('int_setting')
        self.api.logger.info("Getting Test API Settings Plugin config 'int_setting': %s", self.api.plugin_config.get('int_setting'))

        self.api.logger.info("Removing Test API Settings Plugin config 'float_setting'")
        self.api.plugin_config.remove('float_setting')
        self.api.logger.info("Getting Test API Settings Plugin config 'float_setting': %s", self.api.plugin_config.get('float_setting'))

        self.api.logger.info("Removing Test API Settings Plugin config 'str_setting'")
        self.api.plugin_config.remove('str_setting')
        self.api.logger.info("Getting Test API Settings Plugin config 'str_setting': %s", self.api.plugin_config.get('str_setting'))

        self.api.logger.info("Removing Test API Settings Plugin config 'list_setting'")
        self.api.plugin_config.remove('list_setting')
        self.api.logger.info("Getting Test API Settings Plugin config 'list_setting': %s", self.api.plugin_config.get('list_setting'))

        self.api.logger.info("Removing Test API Settings Plugin config 'dict_setting'")
        self.api.plugin_config.remove('dict_setting')
        self.api.logger.info("Getting Test API Settings Plugin config 'dict_setting': %s", self.api.plugin_config.get('dict_setting'))


class WriteSettingTypes(BaseAction):
    NAME = 'Test API Settings Types (write settings)'

    def __init__(self, api: PluginApi = None):
        super().__init__(api=api)
        self.api: PluginApi

    def callback(self, objs):
        self.api.logger.debug("Testing API plugin settings types (writing settings).")

        self.api.logger.info("Setting 'bool_setting' to True")
        self.api.plugin_config['bool_setting'] = True

        self.api.logger.info("Setting 'int_setting' to 42")
        self.api.plugin_config['int_setting'] = 42

        self.api.logger.info("Setting 'float_setting' to 1.23")
        self.api.plugin_config['float_setting'] = 1.23

        self.api.logger.info("Setting 'str_setting' to 'Hello, World!'")
        self.api.plugin_config['str_setting'] = 'Hello, World!'

        self.api.logger.info("Setting 'list_setting' to ['one', 'two', 'three']")
        self.api.plugin_config['list_setting'] = ['one', 'two', 'three']

        self.api.logger.info("Setting Test API Settings Plugin config 'dict_setting' to {'key1': 'value1', 'key2': 'value2'}")
        self.api.plugin_config['dict_setting'] = {'key1': 'value1', 'key2': 'value2'}


class ReadSettingTypes(BaseAction):
    NAME = 'Test API Settings Types (read settings)'

    def __init__(self, api: PluginApi = None):
        super().__init__(api=api)
        self.api: PluginApi

    def callback(self, objs):
        self.api.logger.debug("Testing API plugin settings types (reading settings).")

        for key in ['bool_setting', 'int_setting', 'float_setting', 'str_setting', 'list_setting', 'dict_setting']:
            value = self.api.plugin_config.get(key)
            self.api.logger.info(f".get('{key}')  {type(value)}  = {repr(value)}")


def enable(api: PluginApi):
    """Called when plugin is enabled."""
    api.register_file_action(TestSettings)
    api.register_track_action(TestSettings)
    api.register_album_action(TestSettings)

    api.register_file_action(ClearSettings)
    api.register_track_action(ClearSettings)
    api.register_album_action(ClearSettings)

    api.register_file_action(WriteSettingTypes)
    api.register_track_action(WriteSettingTypes)
    api.register_album_action(WriteSettingTypes)

    api.register_file_action(ReadSettingTypes)
    api.register_track_action(ReadSettingTypes)
    api.register_album_action(ReadSettingTypes)
