import logging

import sublime

SETTINGS_FILE = "PackageDev.sublime-settings"

l = logging.getLogger(__name__)


def package_settings():
    """Return global package settings object or load it first if required."""
    try:
        return package_settings.settings
    except AttributeError:
        l.debug("Loading %s", SETTINGS_FILE)
        package_settings.settings = sublime.load_settings(SETTINGS_FILE)
        return package_settings.settings


def get_setting(key, default=None):
    return package_settings().get(key, default)
