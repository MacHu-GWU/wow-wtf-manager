# -*- coding: utf-8 -*-

import pytest
from wow_wtf_manager.config_init import resolve_group_data


def test_nesting():
    group_data = {
        "g1": [
            "a.a.a",
        ],
        "g2": [
            "g1",
            "b.b.b"
        ],
        "g3": [
            "g2",
            "c.c.c",
        ]
    }
    group_data_new = resolve_group_data(group_data)
    assert group_data_new["g1"] == ["a.a.a"]
    assert group_data_new["g2"] == ["a.a.a", "b.b.b"]
    assert group_data_new["g3"] == ["a.a.a", "b.b.b", "c.c.c"]
    assert group_data_new["_all"] == ["a.a.a", "b.b.b", "c.c.c"]


def test_circular_nest():
    group_data = {
        "g1": [
            "a.a.a",
            "g2",
        ],
        "g2": [
            "b.b.b",
            "g1",
        ],
    }
    with pytest.raises(RecursionError):
        resolve_group_data(group_data)

    group_data = {
        "g1": [
            "g2",
        ],
        "g2": [
            "g1",
        ],
    }
    with pytest.raises(RecursionError):
        resolve_group_data(group_data)


if __name__ == "__main__":
    import os

    basename = os.path.basename(__file__)
    pytest.main([basename, "-s", "--tb=native"])
