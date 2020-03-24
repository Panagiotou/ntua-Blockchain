class Blockchain:
    def __init__(self):
        self.chain = []

    def add_block_to_chain(self, block):
        print("Block added to blockchain!")
        block.printMe()
        print("Chain at the moment is")
        if(self.chain): self.printMe()
        self.chain.append(block)
    def printMe(self):
        print()
        print()
        print("Blockchain:")
        for b in self.chain:
            b.printMe()
        print()
        print()
        for b in self.chain:
            print(b.index, end=" ")
        print()
        print()
    def isInChain(self, hex):
        for b in self.chain:
            for t in b.listOfTransactions:
                if(t.transaction_id_hex == hex):
                    return True
        return False
    def getTransactions(self):
        all = []
        for b in self.chain:
            for t in b.listOfTransactions:
                all.append(t.transaction_id_hex)
        return all

    def isCorrect(self):
        inchain = []
        index = -1
        for b in self.chain:
            if(not b.index == index + 1):
                return False
            for t in b.listOfTransactions:
                if(t.transaction_id_hex in inchain):
                    return False
            index += 1
        return True
