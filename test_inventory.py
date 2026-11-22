import inventory
import pytest

def test_calc_inventory_value():
    assert inventory.calc_inventory_value(inventory.products) == pytest.approx(1057.20)
def test_get_low_stock():
    assert inventory.get_low_stock(inventory.products) == [{'name': 'Keyboard', 'price': '25.50', 'stock': '8', 'min_stock': '10'}, {'name': 'Monitor', 'price': '189.90', 'stock': '3', 'min_stock': '6'}]
def test_calc_restock_cost():
    assert inventory.calc_restock_cost(inventory.products) == pytest.approx(620.70)
def test_get_most_expensive():
    assert inventory.get_most_expensive(inventory.products) == {'name': 'Monitor', 'price': '189.90', 'stock': '3', 'min_stock': '6'}
def test_format_product():
    assert inventory.format_product({"name": "Keyboard", "price": "25.50", "stock": "8", "min_stock": "10"}) =="Keyboard - $25.50 - 8 units"