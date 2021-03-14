# -*- coding: utf-8 -*-

from pathlib_mate import PathCls as Path
from wow_wtf_manager.wtf import WtfCharacter

def remove_all_account_config_cache():
    wow_path = Path(r"D:\HSH\Games\WOW Private\Client\World of Warcraft 3.3.5 enUS (Warman wod models)")
    for p in Path(wow_path, "WTF", "Account").select_file(recursive=True):
        if p.basename.endswith(".old") or p.basename.endswith("cache.md5"):
            p.remove()

remove_all_account_config_cache()