import serialize_named_tuples
import json

import typing


class InnerItem(typing.NamedTuple):
    x: int
    y: int


class OuterItem(typing.NamedTuple):
    name: str
    data: InnerItem


def test_seralize_inner_type():
    inner_item_json = "{'x':0,'y':1}"
    loaded = json.loads(
        inner_item_json,
        object_hook=serialize_named_tuples.create_object_hook(InnerItem),
    )
    assert type(loaded) == custom_named_tuples.InnerItem
