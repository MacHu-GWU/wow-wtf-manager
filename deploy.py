# -*- coding: utf-8 -*-

"""
执行部署任务, 将设置按照 apply.yml 中的配置部署到魔兽世界客户端.

你可以通过注释来选择只部署一部分的设置.
"""

from wow_wtf_manager.config_init import config_data, group_data, apply_data
from wow_wtf_manager import apply

# apply.apply_account_macros(config_data, group_data, apply_data, dry_run=False)
# apply.apply_account_config(config_data, group_data, apply_data, dry_run=False)
# apply.apply_account_bindings(config_data, group_data, apply_data, dry_run=False)
# apply.apply_account_saved_variables(config_data, group_data, apply_data, dry_run=False)

# apply.apply_character_chat(config_data, group_data, apply_data, dry_run=False)
apply.apply_character_addons(config_data, group_data, apply_data, dry_run=False)
# apply.apply_character_layout(config_data, group_data, apply_data, dry_run=False)

# apply.apply_character_macros(config_data, group_data, apply_data, dry_run=False)
# apply.apply_character_bindings(config_data, group_data, apply_data, dry_run=False)
# apply.apply_character_config(config_data, group_data, apply_data, dry_run=False)
# apply.apply_character_saved_variables(config_data, group_data, apply_data, dry_run=False)

