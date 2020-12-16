# -*- coding: utf-8 -*-

import typing
from collections import OrderedDict
from pathlib_mate import PathCls as Path
from . import constant
from . import wtf


def validate_group_name(group_name, group_data):
    if group_name not in group_data:
        raise ValueError(f"{group_name} is not declared in group.yml")


def evaluate_members(task_data, group_data) -> typing.List[str]:
    allow_groups = task_data.get(constant.Syntax.ALLOW_GROUPS, [])
    ignore_groups = task_data.get(constant.Syntax.IGNORE_GROUPS, [])

    members_odct = OrderedDict()
    for group_name in allow_groups:
        validate_group_name(group_name, group_data)
        for member in group_data[group_name]:
            members_odct[member] = None  # set member

    for group_name in ignore_groups:
        validate_group_name(group_name, group_data)
        for member in group_data[group_name]:
            if member in members_odct:
                del members_odct[member]  # remove member

    members = list(members_odct)
    return members


def _apply(config_data,
           group_data,
           apply_data,
           dry_run,
           task_type,
           source_file_dir,
           wtf_attr):
    wow_dir_path = config_data[constant.Syntax.WOW_DIR_PATH]
    tasks = apply_data[task_type]
    for task_data in tasks:
        members = evaluate_members(task_data=task_data, group_data=group_data)
        source_file = Path(source_file_dir, task_data[constant.Syntax.FILE])
        for member in members:
            account, realm, char = member.split(".")
            wtf_char = wtf.WtfCharacter(
                wow_dir_path=wow_dir_path, account=account, realm=realm, char=char
            )
            target_file = getattr(wtf_char, wtf_attr)
            print(f"copy '{source_file}' ---> '{target_file.abspath}'")
            if not dry_run:
                Path(source_file).copyto(new_abspath=target_file.abspath, overwrite=True)


# --- account
def apply_account_macros(config_data, group_data, apply_data, dry_run=True):
    return _apply(
        config_data, group_data, apply_data, dry_run,
        task_type=constant.Syntax.ACCOUNT_MACROS,
        source_file_dir=constant.ACCOUNT_MACROS_DIR,
        wtf_attr="account_macros_file",
    )


def apply_account_bindings(config_data, group_data, apply_data, dry_run=True):
    return _apply(
        config_data, group_data, apply_data, dry_run,
        task_type=constant.Syntax.ACCOUNT_KEYBINDING,
        source_file_dir=constant.ACCOUNT_BINDING_DIR,
        wtf_attr="account_bindings_file",
    )


def apply_account_config(config_data, group_data, apply_data, dry_run=True):
    return _apply(
        config_data, group_data, apply_data, dry_run,
        task_type=constant.Syntax.ACCOUNT_CONFIG,
        source_file_dir=constant.ACCOUNT_CONFIG_DIR,
        wtf_attr="account_config_file",
    )


# --- character
def apply_character_addons(config_data, group_data, apply_data, dry_run=True):
    return _apply(
        config_data, group_data, apply_data, dry_run,
        task_type=constant.Syntax.CHARACTER_ADDONS,
        source_file_dir=constant.CHARACTER_ADDONS_DIR,
        wtf_attr="character_addons_file",
    )


def apply_character_bindings(config_data, group_data, apply_data, dry_run=True):
    return _apply(
        config_data, group_data, apply_data, dry_run,
        task_type=constant.Syntax.CHARACTER_KEYBINDING,
        source_file_dir=constant.CHARACTER_BINDING_DIR,
        wtf_attr="character_bindings_file",
    )


def apply_character_macros(config_data, group_data, apply_data, dry_run=True):
    return _apply(
        config_data, group_data, apply_data, dry_run,
        task_type=constant.Syntax.CHARACTER_MACROS,
        source_file_dir=constant.CHARACTER_MACROS_DIR,
        wtf_attr="character_macros_file",
    )


def apply_character_config(config_data, group_data, apply_data, dry_run=True):
    return _apply(
        config_data, group_data, apply_data, dry_run,
        task_type=constant.Syntax.CHARACTER_CONFIG,
        source_file_dir=constant.CHARACTER_CONFIG_DIR,
        wtf_attr="character_config_file",
    )


def apply_character_layout(config_data, group_data, apply_data, dry_run=True):
    return _apply(
        config_data, group_data, apply_data, dry_run,
        task_type=constant.Syntax.CHARACTER_LAYOUT,
        source_file_dir=constant.CHARACTER_LAYOUT_DIR,
        wtf_attr="character_layout_file",
    )


def apply_character_chat(config_data, group_data, apply_data, dry_run=True):
    return _apply(
        config_data, group_data, apply_data, dry_run,
        task_type=constant.Syntax.CHARACTER_CHAT,
        source_file_dir=constant.CHARACTER_CHAT_DIR,
        wtf_attr="character_chat_file",
    )
