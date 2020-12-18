# -*- coding: utf-8 -*-

import typing
import jinja2
from collections import OrderedDict
from pathlib_mate import PathCls as Path
from . import constant
from . import wtf
from pprint import pprint

def validate_exists(path):
    p = Path(path)
    if not p.exists():
        raise RuntimeError(f"{p.abspath} not exists!")


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
    target_file_duplicate_filter = set()
    for task_data in tasks:
        members = evaluate_members(task_data=task_data, group_data=group_data)
        source_file = Path(source_file_dir, task_data[constant.Syntax.FILE])
        source_file_content = source_file.read_text(encoding="utf-8")
        for member in members:
            account, realm, char = member.split(".")
            wtf_char = wtf.WtfCharacter(
                wow_dir_path=wow_dir_path, account=account, realm=realm, char=char
            )
            target_file = getattr(wtf_char, wtf_attr)
            if target_file.abspath not in target_file_duplicate_filter:
                print(f"copy '{source_file}' ---> '{target_file.abspath}'")
                if not dry_run:
                    target_file.atomic_write_text(source_file_content, overwrite=True)
                target_file_duplicate_filter.add(target_file.abspath)


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


def _apply_saved_variables(config_data,
                           group_data,
                           apply_data,
                           dry_run,
                           task_type,
                           source_file_dir,
                           wtf_attr):
    wow_dir_path = config_data[constant.Syntax.WOW_DIR_PATH]
    tasks = apply_data[task_type]
    target_file_duplicate_filter = set() # type: typing.Set[str]
    final_content_cache = dict() # type: typing.Dict[str, str]

    all_wtf_char_list = list() # type: typing.List[wtf.WtfCharacter]
    for member in group_data["_all"]:
        account, realm, char = member.split(".")
        wtf_char = wtf.WtfCharacter(
            wow_dir_path=wow_dir_path, account=account, realm=realm, char=char
        )
        all_wtf_char_list.append(wtf_char)

    for task_data in tasks:
        members = evaluate_members(task_data=task_data, group_data=group_data)
        allow_addons = task_data[constant.Syntax.ALLOW_ADDONS]

        wtf_char_list = list() # type: typing.List[wtf.WtfCharacter]
        for member in members:
            account, realm, char = member.split(".")
            wtf_char = wtf.WtfCharacter(
                wow_dir_path=wow_dir_path, account=account, realm=realm, char=char
            )
            wtf_char_list.append(wtf_char)

        for wtf_char in wtf_char_list:
            for addon_sv_file in allow_addons:
                source_file = Path(source_file_dir, addon_sv_file)
                validate_exists(source_file)
                target_file = Path(getattr(wtf_char, wtf_attr), addon_sv_file)

                if source_file.abspath not in final_content_cache:
                    tpl = jinja2.Template(source_file.read_text(encoding="utf-8"))
                    final_content = tpl.render(characters=wtf_char_list, all_characters=all_wtf_char_list)
                    final_content_cache[source_file.abspath] = final_content
                else:
                    final_content = final_content_cache[source_file.abspath]

                if target_file.abspath not in target_file_duplicate_filter:
                    print(f"render '{source_file}' -- write to -> '{target_file.abspath}'")
                    if not dry_run:
                        target_file.atomic_write_text(final_content, overwrite=True)
                    target_file_duplicate_filter.add(target_file.abspath)


def apply_account_saved_variables(config_data, group_data, apply_data, dry_run=True):
    return _apply_saved_variables(
        config_data, group_data, apply_data, dry_run,
        task_type=constant.Syntax.ACCOUNT_SAVED_VARIABLES,
        source_file_dir=constant.ACCOUNT_SAVED_VARIABLES_DIR,
        wtf_attr="account_saved_variables_dir",
    )


def apply_character_saved_variables(config_data, group_data, apply_data, dry_run=True):
    return _apply_saved_variables(
        config_data, group_data, apply_data, dry_run,
        task_type=constant.Syntax.CHARACTER_SAVED_VARIABLES,
        source_file_dir=constant.CHARACTER_SAVED_VARIABLES_DIR,
        wtf_attr="character_saved_variables_dir",
    )