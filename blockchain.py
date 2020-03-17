class Blockchain:
    def __init__(self):
        self.chain = []

    def add_block_to_chain(self, block):
        print("Block", block.index, "added to blockchain!")
        self.chain.append(block)
    def printMe(self):
        print()
        print()
        print("Blockchain:")
        for b in self.chain:
            b.printMe()
        print()
        print()
