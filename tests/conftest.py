import typing

from pytest import fixture

from nirum.serialize import serialize_record_type, serialize_boxed_type
from nirum.deserialize import deserialize_record_type, deserialize_boxed_type


class offset:

    def __init__(self, value: float) -> None:
        self.value = value

    def __eq__(self, other) -> bool:
        return (isinstance(other, offset) and self.value == other.value)

    def __hash__(self) -> int:
        return hash(self.value)

    def __nirum_serialize__(self) -> typing.Mapping[str, typing.Any]:
        return serialize_boxed_type(self)

    @classmethod
    def __nirum_deserialize__(
        cls: type, value: typing.Mapping[str, typing.Any]
    ) -> 'offset':
        return deserialize_boxed_type(cls, value)


class point:

    __slots__ = (
        'left',
        'top'
    )
    __slot_types = {
        'left': offset,
        'top': offset
    }

    def __init__(self, left: offset, top: offset) -> None:
        self.left = left
        self.top = top

    def __repr__(self) -> str:
        return '{0.__module__}.{0.__qualname__}({1})'.format(
            type(self),
            ', '.join('{}={}'.format(attr, getattr(self, attr))
                      for attr in self.__slots__)
        )

    def __eq__(self, other) -> bool:
        attr_matched = all(
            getattr(self, attr) == getattr(other, attr)
            for attr in self.__slots__
        )
        return isinstance(other, point) and attr_matched

    def __nirum_serialize__(self) -> typing.Mapping[str, typing.Any]:
        return serialize_record_type(self)

    @classmethod
    def __nirum_deserialize__(
        cls: type, **values
    ) -> 'point':
        return deserialize_record_type(cls, values)


@fixture
def fx_boxed_type():
    return offset


@fixture
def fx_offset(fx_boxed_type):
    return fx_boxed_type(1.2)


@fixture
def fx_record_type():
    return point


@fixture
def fx_point(fx_record_type, fx_boxed_type):
    return fx_record_type(fx_boxed_type(3.14), fx_boxed_type(1.592))
