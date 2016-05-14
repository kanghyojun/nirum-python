from pytest import raises

from nirum.validate import validate_boxed_type, validate_record_type


def test_validate_boxed_type():
    assert validate_boxed_type(3.14, float)
    with raises(TypeError):
        validate_boxed_type('hello', float)


def test_validate_record_type(fx_point):
    assert validate_record_type(fx_point)
