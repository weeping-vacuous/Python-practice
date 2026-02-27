
#def net_price(list_price,discount, tax):
 #   return list_price*(1-discount)*(tax+1)
def net_price(list_price,discount=0, tax=0.05):
    return list_price*(1-discount)*(tax+1)

print(net_price(500))