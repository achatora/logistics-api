from decimal import Decimal

import pytest

from app.shipment.item import Item


# test if item can be created
def test_item_can_be_created():
    item = Item("Laptop", Decimal("2.5"), 3)

    assert item.name == "Laptop"
    assert item.weight == Decimal("2.5")
    assert item.quantity == 3


# test if None rejected for name
def test_item_rejects_none_name():

    with pytest.raises(ValueError):
        Item(None, Decimal("2.5"), 3)


# test if 0 is rejected for quantity
def test_item_rejects_zero_quantity():

    with pytest.raises(ValueError):
        Item("Laptop", Decimal("2.5"), 0)


# test if < 0 is rejected for quantity
def test_item_rejects_less_than_zero_quantity():

    with pytest.raises(ValueError):
        Item("Laptop", Decimal("2.5"), -1)


# test if None is rejected for weight
def test_item_rejects_none_weight():
    with pytest.raises(ValueError):
        Item("Laptop", None, 3)


# test if 0 is rejected for weight
def test_item_rejects_zero_weight():
    with pytest.raises(ValueError):
        Item("Laptop", Decimal(0), 3)


# test if < 0 is rejected for weight
def test_item_rejects_less_than_zero_weight():
    with pytest.raises(ValueError):
        Item("Laptop", Decimal(-1), 3)


# test is total weight is calculated
def test_item_calculates_total_weight():
    item = Item("Laptop", Decimal("2.5"), 3)

    assert item.total_weight == Decimal("7.5")
