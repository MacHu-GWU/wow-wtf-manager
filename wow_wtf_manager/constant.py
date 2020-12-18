# -*- coding: utf-8 -*-

from pathlib_mate import PathCls as Path

PROJECT_ROOT_DIR = Path(__file__).absolute().parent.parent
CONFIG_ROOT_DIR = Path(PROJECT_ROOT_DIR, "config")
CONFIG_YML_FILE = Path(CONFIG_ROOT_DIR, "config.yml")
GROUP_YML_FILE = Path(CONFIG_ROOT_DIR, "group.yml")
APPLY_YML_FILE = Path(CONFIG_ROOT_DIR, "apply.yml")

ACCOUNT_MACROS_DIR = Path(CONFIG_ROOT_DIR, "account-macros-cache.txt")
ACCOUNT_BINDING_DIR = Path(CONFIG_ROOT_DIR, "account-bindings-cache.wtf")
ACCOUNT_CONFIG_DIR = Path(CONFIG_ROOT_DIR, "account-config-cache.wtf")
ACCOUNT_SAVED_VARIABLES_DIR = Path(CONFIG_ROOT_DIR, "account-saved-variables")

CHARACTER_ADDONS_DIR = Path(CONFIG_ROOT_DIR, "character-AddOns.txt")
CHARACTER_LAYOUT_DIR = Path(CONFIG_ROOT_DIR, "character-layout-local.txt")
CHARACTER_MACROS_DIR = Path(CONFIG_ROOT_DIR, "character-macros-cache.txt")
CHARACTER_CHAT_DIR = Path(CONFIG_ROOT_DIR, "character-chat-cache.txt")
CHARACTER_BINDING_DIR = Path(CONFIG_ROOT_DIR, "character-bindings-cache.wtf")
CHARACTER_CONFIG_DIR = Path(CONFIG_ROOT_DIR, "character-config-cache.wtf")

CHARACTER_SAVED_VARIABLES_DIR = Path(CONFIG_ROOT_DIR, "character-saved-variables")


def ensure_exists(list_of_dir):
    for p in list_of_dir:
        if not p.exists():
            raise Exception(f"{p.abspath} not exists!")


list_of_dir = [
    PROJECT_ROOT_DIR,
    CONFIG_ROOT_DIR,
    CONFIG_YML_FILE,
    GROUP_YML_FILE,
    APPLY_YML_FILE,

    ACCOUNT_MACROS_DIR,
    ACCOUNT_BINDING_DIR,
    ACCOUNT_CONFIG_DIR,

    CHARACTER_ADDONS_DIR,
    CHARACTER_LAYOUT_DIR,
    CHARACTER_MACROS_DIR,
    CHARACTER_CHAT_DIR,
    CHARACTER_BINDING_DIR,
    CHARACTER_CONFIG_DIR,
]
ensure_exists(list_of_dir)


class Syntax:
    # --- wow config things keyword
    ACCOUNT_MACROS = "account-macros"
    ACCOUNT_KEYBINDING = "account-keybinding"
    ACCOUNT_CONFIG = "account-config"
    ACCOUNT_SAVED_VARIABLES = "account-saved-variables"

    CHARACTER_ADDONS = "character-addons"
    CHARACTER_LAYOUT = "character-layout"
    CHARACTER_CHAT = "character-chat"
    CHARACTER_KEYBINDING = "character-keybinding"
    CHARACTER_MACROS = "character-macros"
    CHARACTER_CONFIG = "character-config"
    CHARACTER_SAVED_VARIABLES = "character-saved-variables"

    # --- task level keyword
    ALLOW_GROUPS = "allow-groups"
    IGNORE_GROUPS = "ignore-groups"
    FILE = "file"
    ALLOW_ADDONS = "allow-addons"

    # --- general config keyword
    WOW_DIR_PATH = "wow-dir-path"
