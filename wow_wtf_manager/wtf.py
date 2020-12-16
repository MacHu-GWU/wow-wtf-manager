# -*- coding: utf-8 -*-

from pathlib_mate import PathCls as Path
from attrs_mate import attr, AttrsClass


@attr.s
class WtfCharacter(AttrsClass):
    wow_dir_path = attr.ib()
    account = attr.ib(default=None)
    realm = attr.ib(default=None)
    char = attr.ib(default=None)

    def __attrs_post_init__(self):
        self.account = self.account.upper()
        self.realm = self.realm.lower()[0].upper() + self.realm.lower()[1:]
        self.char = self.char.lower()[0].upper() + self.char.lower()[1:]

    @property
    def wtf_specific_account_dir(self) -> Path:
        return Path(self.wow_dir_path, "WTF", "Account", self.account)

    @property
    def wtf_specific_char_dir(self) -> Path:
        return Path(self.wow_dir_path, "WTF", "Account", self.account, self.realm, self.char)

    #--- account level ---
    @property
    def account_macros_file(self):
        return Path(self.wtf_specific_account_dir, "macros-cache.txt")

    @property
    def account_bindings_file(self):
        return Path(self.wtf_specific_account_dir, "bindings-cache.wtf")

    @property
    def account_config_file(self):
        return Path(self.wtf_specific_account_dir, "config-cache.wtf")

    #--- character level
    @property
    def character_addons_file(self):
        return Path(self.wtf_specific_char_dir, "AddOns.txt")

    @property
    def character_layout_file(self):
        return Path(self.wtf_specific_char_dir, "layout-local.txt")

    @property
    def character_macros_file(self):
        return Path(self.wtf_specific_char_dir, "macros-cache.txt")

    @property
    def character_bindings_file(self):
        return Path(self.wtf_specific_char_dir, "bindings-cache.wtf")

    @property
    def character_config_file(self):
        return Path(self.wtf_specific_char_dir, "config-cache.wtf")

    @property
    def character_chat_file(self):
        return Path(self.wtf_specific_char_dir, "chat-cache.txt")
