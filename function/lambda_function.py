import json
from datetime import datetime

def format_currency(amount):
    """Format amount to 2 decimal places with $ symbol"""
    return f"${amount:.2f}"

def calculate_price(order_items):
    # Menu with prices
    menu_prices = {
        'burger': 8.99,
        'pizza': 12.99,
        'soft_drink': 2.99,
        'fries': 3.99,
        'salad': 6.99,
        'ice_cream': 4.99
    }
    
    total = 0
    items_summary = []
    
    # Calculate total and prepare summary
    for item in order_items:
        item = item.lower()
        if item in menu_prices:
            total += menu_prices[item]
            items_summary.append({
                'item': item.title(),
                'price': format_currency(menu_prices[item])
            })
        else:
            return {
                'statusCode': 400,
                'body': {
                    'error': f'Invalid item: {item}',
                    'available_items': list(menu_prices.keys())
                }
            }
    
    # Calculate tax and total
    tax = round(total * 0.08, 2)
    final_total = round(total + tax, 2)
    
    # Create receipt
    receipt = {
        'receipt_details': {
            'datetime': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'order_id': f"ORD-{datetime.now().strftime('%Y%m%d%H%M%S')}"
        },
        'items': [f"{item['item']}: {item['price']}" for item in items_summary],
        'price_summary': {
            'subtotal': format_currency(total),
            'tax_8%': format_currency(tax),
            'total': format_currency(final_total)
        }
    }
    
    return {
        'statusCode': 200,
        'body': receipt
    }

def lambda_handler(event, context):
    """
    Lambda function to calculate food order total
    
    Expected event format:
    {
        "items": ["burger", "pizza", "soft_drink"]
    }
    """
    try:
        # Extract order items from event
        if 'items' not in event:
            return {
                'statusCode': 400,
                'body': {
                    'error': 'No items found in order',
                    'expected_format': {
                        'items': ['item1', 'item2']
                    }
                }
            }
        
        order_items = event['items']
        
        # Validate input
        if not isinstance(order_items, list):
            return {
                'statusCode': 400,
                'body': {
                    'error': 'Items should be a list',
                    'received': type(order_items).__name__
                }
            }
        
        if not order_items:
            return {
                'statusCode': 400,
                'body': {
                    'error': 'Order is empty'
                }
            }
        
        # Calculate and return response
        return calculate_price(order_items)
        
    except Exception as e:
        return {
            'statusCode': 500,
            'body': {
                'error': 'Internal server error',
                'message': str(e)
            }
        }