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
    record_types = getattr(
        record,
        '_{0.__class__.__name__}__slot_types'.format(record)
    )
    return all(isinstance(getattr(record, attr), type_)
               for attr, type_ in record_types.items())
