from typing import Dict, Type, NamedTuple, Any, Callable, TypeVar

NamedTuple_T = TypeVar("NamedTuple_T", bound=Type[NamedTuple])
Json_Object = Dict[str, Any]


def unseralize_object(cls, value):
    if isinstance(cls, type(NamedTuple)):
        return create_object_hook(cls)(value)
    if isinstance(value, dict):
        return cls(**value)
    return cls(value)


def create_object_hook(
    named_tuple_cls: Type[NamedTuple_T]
) -> Callable[[Json_Object], NamedTuple_T]:
    """Return a Object hook to seralize the given named tuple class from JSON"""

    def create_object_hook(obj: Json_Object) -> NamedTuple_T:
        created_object = dict()
        for key, value_cls in named_tuple_cls._field_types.items():
            created_object[key] = unseralize_object(value_cls, obj[key])
        return named_tuple_cls._make(created_object)

    return create_object_hook
