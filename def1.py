def add(prices,discount_items):
    total = sum(prices)
    Discount=total*(discount_items/100)
    Shopping_item=total-Discount
    return Shopping_item
Dress_items=[1000,2000,300,450]
bill_section=add(Dress_items,10)
print(bill_section)