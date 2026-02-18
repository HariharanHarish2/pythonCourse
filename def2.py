def hero(prices):
    total=sum(prices)
    discount=total*0.10
    final_count=total-discount
    return final_count
shooping_items=[200,300,450]
total_prices=hero(shooping_items)
print(total_prices)