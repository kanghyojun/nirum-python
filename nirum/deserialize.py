""":mod:`nirum.deserialize`
~~~~~~~~~~~~~~~~~~~~~~~~~~~

"""
__all__ = 'deserialize_boxed_type', 'deserialize_record_type',


def deserialize_boxed_type(cls, value):
    return cls(value=value)


def deserialize_record_type(cls, **values):
    return cls(**values)
