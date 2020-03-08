class Blockchain:
    def __init__(self):
        self.chain = []

    def add_block_to_chain(self, block):
        self.chain.append(block)
