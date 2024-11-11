import pytest
from function.lambda_function import calculate_price

def test_single_item_calculation():
    """Test calculation for a single item"""
    result = calculate_price(["burger"])
    assert result["statusCode"] == 200
    price_summary = result["body"]["price_summary"]
    assert price_summary["subtotal"] == "$10.99"
    assert price_summary["tax_8%"] == "$0.88"
    assert price_summary["total"] == "$11.87"

def test_multiple_items_calculation():
    """Test calculation for multiple items"""
    result = calculate_price(["burger", "pizza", "soft_drink"])
    assert result["statusCode"] == 200
    price_summary = result["body"]["price_summary"]
    assert price_summary["subtotal"] == "$26.97"  # 10.99 + 12.99 + 2.99
    assert price_summary["tax_8%"] == "$2.16"     # 26.97 * 0.08
    assert price_summary["total"] == "$29.12" 
