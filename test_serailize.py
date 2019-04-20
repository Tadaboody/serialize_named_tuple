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
    loaded = json.loads(flat_tuple_json)
    typed_loaded = serialize_named_tuples.make_typed(FlatTuple, loaded)
    assert type(typed_loaded) == FlatTuple
    assert type(typed_loaded.x) == int
    assert type(typed_loaded.y) == int


def test_seralize_nested_type():
    nested_tuple_json = '{"name":"arnold","data":{"x":0,"y":1}}'
    loaded = json.loads(nested_tuple_json)
    typed_loaded = serialize_named_tuples.make_typed(NestedTuple, loaded)
    assert type(typed_loaded) == NestedTuple
    assert type(typed_loaded.name) == str
    assert type(typed_loaded.data) == FlatTuple
    assert type(typed_loaded.data.x) == int
