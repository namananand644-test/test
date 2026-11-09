from app import calculate_total, apply_discount


def test_calculate_total():
    assert calculate_total(100, 2) == 200


def test_apply_discount():
    assert apply_discount(200, 10) == 180
