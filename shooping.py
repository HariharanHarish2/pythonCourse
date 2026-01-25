def add(prices):
    total=sum(prices)
    discount=total*0.10
    shopping=total-discount
    return shopping
shopping_price =[1000,2000,400,6000]
final_rate=add(shopping_price)
print(final_rate)