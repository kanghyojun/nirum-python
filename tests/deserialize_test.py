from nirum.deserialize import deserialize_boxed_type


def test_deserialize_boxed_type(fx_boxed_type):
    v = 3.14
    assert fx_boxed_type(v) == deserialize_boxed_type(fx_boxed_type, v)
