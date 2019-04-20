import serialize_named_tuples
import json

import typing


class FlatTuple(typing.NamedTuple):
    x: int
    y: int


class NestedTuple(typing.NamedTuple):
    name: str
    data: FlatTuple


def test_seralize_flat_type():
    flat_tuple_json = '{"x":0,"y":1}'
    loaded = json.loads(
        flat_tuple_json,
        object_hook=serialize_named_tuples.create_object_hook(FlatTuple),
    )
    assert type(loaded) == FlatTuple
