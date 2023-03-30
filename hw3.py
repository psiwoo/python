def get_fixed_price(dp):
    global dr
    result=dp*(100/(100-dr))
    return result
dr=int(input('할인율은? '))
dp=int(input('A 상품의 할인된 가격은? '))
aprice=get_fixed_price(dp)
dp=int(input('A 상품의 할인된 가격은? '))
bprice=get_fixed_price(dp)
print('A 상품의 정가는', aprice,'원')
print('B 상품의 정가는', bprice,'원')   
