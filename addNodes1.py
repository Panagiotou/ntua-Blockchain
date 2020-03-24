def read_transaction():
    print("Reading input transactions")
    f = open("5nodes_small/transactions" + str(1) + ".txt", "r")
    for j in range(10):
        line = f.readline()
        id, amount = (line).split()
        print(id, amount)
read_transaction()
