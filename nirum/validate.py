""":mod:`nirum.validate`
~~~~~~~~~~~~~~~~~~~~~~~~

"""
__all__ = 'validate_boxed_type', 'validate_record_type',


def validate_boxed_type(boxed, type_hint) -> bool:
    if not isinstance(boxed, type_hint):
        raise TypeError('{0} expected, found: {1}'.format(type_hint,
                                                          type(boxed)))
    return True


def validate_record_type(record) -> bool:
    record_types = getattr(record, '__nirum_field_types__')
    for attr, type_ in record_types.items():
        data = getattr(record, attr)
        if not isinstance(data, type_):
            raise TypeError(
                'expect {0.__class__.__name__}.{1} to be {2}'
                'found: {3}'.format(record, attr, type_, type(data))
            )
    else:
        return True
