""":mod:`nirum.serialize`
~~~~~~~~~~~~~~~~~~~~~~~~~

"""
__all__ = 'serialize_boxed_type', 'serialize_record_type',


def serialize_boxed_type(data):
    return data.value


def serialize_record_type(data):
    def _try_serialize(value):
        try:
            s = value.__nirum_serialize__()
        except AttributeError:
            return value
        else:
            return s

    return {
        slot_name: _try_serialize(getattr(data, slot_name))
        for slot_name in data.__slots__
    }
