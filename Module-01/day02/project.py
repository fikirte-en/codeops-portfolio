customers = [("Fikir",1000),("Demelash",500),("Asnaku",120000),("Abebe",30000),("zewdu",80)]

def tier(balance):
    if balance >= 1000:
        return "Premium"
    elif balance >= 500:
        return"Standard"
    else:
        return "Basic"
    
for name,balance in customers:
    print (f"{name}:{tier(balance)} {balance} ETB")

