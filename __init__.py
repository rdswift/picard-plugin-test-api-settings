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
    NAME = 'Test API Settings: Read/Write'

    def __init__(self, api: PluginApi = None):
        super().__init__(api=api)
        self.api: PluginApi

    def callback(self, objs):
        self.api.logger.debug("# Testing Test API Settings Plugin configuration management.")

        self.api.logger.debug("# Initial settings (default values if not already set)")
        for key in ['bool_setting', 'int_setting', 'float_setting', 'str_setting', 'list_setting', 'dict_setting']:
            self.api.logger.info(f"api.plugin_config['{key}'] = {repr(self.api.plugin_config[key])}")

        test_settings = [
            ('bool_setting', True),
            ('bool_setting', False),
            ('int_setting', 42),
            ('int_setting', -1),
            ('float_setting', 1.23),
            ('float_setting', -2.34),
            ('str_setting', "Hello, World!"),
            ('str_setting', "All done."),
            ('list_setting', ['one', 'two', 'three']),
            ('list_setting', ['A', 'B', 'C']),
            ('dict_setting', {'key1': 'value1', 'key2': 'value2'}),
            ('dict_setting', {'keyA': 'valueA', 'keyB': 'valueB'}),
        ]

        self.api.logger.debug("# Test adding/changing settings")
        for key, value in test_settings:
            self.api.logger.info(f"Setting api.plugin_config['{key}'] = {repr(value)}")
            self.api.plugin_config[key] = value
            self.api.logger.info(f"The value of api.plugin_config['{key}'] is now {repr(self.api.plugin_config[key])}")


class ClearSettings(BaseAction):
    NAME = 'Test API Settings: Remove Settings'

    def __init__(self, api: PluginApi = None):
        super().__init__(api=api)
        self.api: PluginApi

    def callback(self, objs):
        self.api.logger.debug("Removing Test API Settings Plugin configuration settings.")
        for key in ['bool_setting', 'int_setting', 'float_setting', 'str_setting', 'list_setting', 'dict_setting']:
            self.api.logger.info(f"Removing api.plugin_config['{key}']")
            self.api.plugin_config.remove(key)


class ReadSettingTypes(BaseAction):
    NAME = 'Test API Settings: Check Types'

    def __init__(self, api: PluginApi = None):
        super().__init__(api=api)
        self.api: PluginApi

    def callback(self, objs):
        self.api.logger.debug("Testing API plugin settings types.")

        for key in ['bool_setting', 'int_setting', 'float_setting', 'str_setting', 'list_setting', 'dict_setting']:
            value = self.api.plugin_config[key]
            self.api.logger.info(f"api.plugin_config['{key}'] {type(value)} = {repr(value)}")


def enable(api: PluginApi):
    """Called when plugin is enabled."""

    api.plugin_config.register_option('bool_setting', True)
    api.plugin_config.register_option('int_setting', 42)
    api.plugin_config.register_option('float_setting', 1.23)
    api.plugin_config.register_option('str_setting', "Hello, World!")
    api.plugin_config.register_option('list_setting', ['one', 'two', 'three'])
    api.plugin_config.register_option('dict_setting', {'key1': 'value1', 'key2': 'value2'})

    api.register_file_action(TestSettings)
    api.register_track_action(TestSettings)
    api.register_album_action(TestSettings)

    api.register_file_action(ReadSettingTypes)
    api.register_track_action(ReadSettingTypes)
    api.register_album_action(ReadSettingTypes)

    api.register_file_action(ClearSettings)
    api.register_track_action(ClearSettings)
    api.register_album_action(ClearSettings)
