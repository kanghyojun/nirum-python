from nirum.deserialize import deserialize_boxed_type, deserialize_record_type


def test_deserialize_boxed_type(fx_boxed_type):
    v = 3.14
    assert fx_boxed_type(v) == deserialize_boxed_type(fx_boxed_type, v)


def test_deserialize_record_type(fx_boxed_type, fx_record_type):
    left = fx_boxed_type(1.1)
    top = fx_boxed_type(2.2)
    deserialized = deserialize_record_type(fx_record_type, left=left, top=top)
    assert deserialized == fx_record_type(left=left, top=top)
