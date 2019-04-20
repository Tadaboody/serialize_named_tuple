from typing import Dict, Type, NamedTuple, Any, Callable, TypeVar

NamedTuple_T = TypeVar("NamedTuple_T", bound=Type[NamedTuple])
Json_Object = Dict[str, Any]


def create_object_hook(
    named_tuple_cls: Type[NamedTuple_T]
) -> Callable[[Json_Object], NamedTuple_T]:
    """Return a Object hook to seralize the given named tuple class from JSON"""
